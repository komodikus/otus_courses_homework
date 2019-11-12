import os
dirname = os.path.dirname(__file__)
filename_login = os.path.join(dirname, 'templates\\login.html')
filename_index = os.path.join(dirname, 'templates\\index.html')


def login(template=filename_login):
    my_template = open(template, 'r')
    return {'status_code': 200,
             "template": my_template.read(),
             'extra_headers': {'Content-Type': 'text/html'}
    }


def index(template=filename_index):
    my_template = open(template, 'r')
    return {'status_code': 200,
             "template": my_template.read(),
             'extra_headers': {'Content-Type': 'text/html'}
    }


