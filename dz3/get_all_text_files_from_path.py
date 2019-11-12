import os


def parse_file(path, searched_file_extensions='.py'):
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith(searched_file_extensions) and not file.startswith('__'):
                print(file)
                with open('temporary.txt', 'a', encoding='utf-8') as file_to_write, \
                        open(os.path.join(dirname, file), 'r', encoding='utf-8') as file_to_read:
                        file_to_write.write(file_to_read.read())
    return 'temporary.txt'


# delete repo
