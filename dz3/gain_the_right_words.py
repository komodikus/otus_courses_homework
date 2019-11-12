import collections

from get_all_text_files_from_path import parse_file
from get_repo import clone_repo_in_github
from acquire import *


def get_top_function_words(top_size):
    function_names = flat(
        [split_snake_case_name_to_words(function_name) for function_name in get_functions_names_from_file()])
    return collections.Counter(function_names).most_common(top_size)


def get_top_variables_names(top_size):
    variables_names = flat(
        [split_snake_case_name_to_words(variable_name) for variable_name in get_all_variables_names()])
    return collections.Counter(variables_names).most_common(top_size)


def get_top_verbs_names(top_size):
    verbs_names = get_all_verbs()
    return collections.Counter(verbs_names).most_common(top_size)


def get_top_nouns_names(top_size):
    nouns_names = get_all_nouns()
    return collections.Counter(nouns_names).most_common(top_size)


def get_top_words_selected_part_of_speech(directory='D:\\Git', searched_item='def', top_size=5,
                                          git_url='https://github.com/komodikus/otus-1-lesson-dz'):
    parse_file(path=clone_repo_in_github(git_url=git_url, directory=directory))
    top_words = 0
    if searched_item == 'def':
        top_words = get_top_function_words(top_size)
    elif searched_item == 'var':
        top_words = get_top_variables_names(top_size)
    elif searched_item == 'verb':
        top_words = get_top_verbs_names(top_size)
    elif searched_item == 'noun':
        top_words = get_top_nouns_names(top_size)
    return top_words





