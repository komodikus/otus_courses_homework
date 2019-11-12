import ast
import nltk
import re


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def read_temp_file():
    with open('temporary.txt', 'r', encoding="utf-8") as attempt_handler:
        main_file_content = attempt_handler.read()
    return main_file_content

def get_functions_names_from_file():
    tree = ast.parse(read_temp_file())
    return [x.name for x in ast.walk(tree) if isinstance(x, ast.FunctionDef)]


def get_all_variables_names():
    tree = ast.parse(read_temp_file())
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def split_snake_case_name_to_words(name):
    return [n for n in name.split('_') if n]


def get_all_words():
    readed_file = read_temp_file()
    readed_file = re.sub("[!@#$%^&*()='/:\"\[\]~(\-\-(\\)><?)`]", '', readed_file)
    readed_file = re.sub("[(__),\._\-\n]", ' ', readed_file)
    readed_file = [value for value in readed_file.split(' ') if value if not value.isdigit()]
    return readed_file


def get_all_verbs():
    words = get_all_words()
    verbs = [value[0] for value in nltk.pos_tag(words) if value[1].startswith("VB")]
    return verbs


def get_all_nouns():
    words = get_all_words()
    nouns = [value[0] for value in nltk.pos_tag(words) if value[1].startswith("NN")]
    return nouns



















