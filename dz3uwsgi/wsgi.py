from dz3uwsgi.config import URLS


def normalize_url(url):
    if url[-1] == '/' and url != '/':
        url = url[:-1]
        return url
    return url


def application(env, start_response):
    url = normalize_url(env['PATH_INFO'])
    view_name = URLS.get(url)
    function_name = 'views.' + view_name + '()'
    view_response = eval(function_name)
    if not view_name:
        status_code = '404 Not Found'
        content = b'Not Found'
    else:
        status_code = view_response['status_code']
        extra_header = view_response['extra_headers']
        content = view_response['template']
    start_response(status_code, extra_header)
    return content
