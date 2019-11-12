import ast
import os
import collections

from nltk import pos_tag


def does_the_word_fit(name):
    return (name.startswith('__') and name.endswith('__'))


def generate_trees(path, with_file_names=False, with_file_content=False):
    file_names = search_python_files(path)
    trees = []

    for filename in file_names:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None

        if with_file_names:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)

    filtered_trees = [tree for tree in trees if tree]
    return filtered_trees


def print_status(decorator_arg):
    def my_decorator(func):
        def wrapped(*args, **kwargs):
            function_value = func(*args, **kwargs)
            print(decorator_arg)
            return function_value

        return wrapped

    return my_decorator


def len_of_func(func):
    def wrapper(*args, **kwargs):
        function_value = func(*args, **kwargs)
        print(len(function_value))
        return function_value

    return wrapper


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


@len_of_func
def search_python_files(path):
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        if len(filenames) < 100:
            for file in files:
                if file.endswith('.py'):
                    filenames.append(os.path.join(dirname, file))
        return filenames
    

@print_status('trees generated')
def get_trees(Path="", with_filenames=False, with_file_content=False):
    filenames = search_python_files(Path)
    print('total %s files' % len(filenames))
    return generate_trees(filenames, with_filenames, with_file_content)


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def split_snake_case_name_to_words(name):
    return [word for word in name.split('_') if word]


def get_all_words_in_path(path):
    trees = [tree for tree in get_trees(path) if tree]
    function_names = [func for func in flat([get_all_names(tree) for tree in trees]) if
                      not does_the_word_fit(func)]
    return flat([split_snake_case_name_to_words(function_name) for function_name in function_names])


@print_status('functions extracted')
def get_top_verbs_in_path(path, top_size=10):
    trees = [tree for tree in get_trees(None, path) if tree]
    flat_names = flat([[node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                       for tree in trees])
    not_private_function = [func for func in flat_names
                            if not does_the_word_fit(func)]
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in not_private_function])
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    trees = get_trees(path)
    flat_names = flat([[node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
                       for tree in trees])
    function_names = [file for file in
                      flat_names if not does_the_word_fit(file)]
    return collections.Counter(function_names).most_common(top_size)


def get_top_verbs_in_projects(projects=None):
    top_verbs_in_projects = []
    if projects is None:
        projects = [
            'django',
            'flask',
            'pyramid',
            'reddit',
            'requests',
            'sqlalchemy',
        ]
    for project in projects:
        path = os.path.join('.', project)
        top_verbs_in_projects += get_top_verbs_in_path(path)
    return top_verbs_in_projects


def main():
    query = get_top_verbs_in_projects()
    print('total %s words, %s unique' % (len(query), len(set(query))))
    for word, occurence in collections.Counter(query).most_common(200):
        print(word, occurence)


if __name__ == '__main__':
    main()
