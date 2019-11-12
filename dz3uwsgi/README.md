# Python uwsgi framework
# Usage
uwsgi: --http :9090 --wsgi-file wsgi.py
Connect via broser to http://127.0.0.1/your_urls

To create a web-page you need:

Dict config URLS needed for routing. Enter the required routings in the format  
```
{
    '/': 'index',
    '/login/': 'login',
    }
```
Where 'index', 'login' are functions in views.py  
Create view function for your page in views.py. Function must have first positional argument 'view' string, and he must return dict like a ```{'status_code': 200,"template": my_template.read(),'extra_headers': {'Content-Type': 'text/html'}} ``` 
First arg must be status_code, second -> file_template.read(), third-> {'Content-Type': 'text/html'} (or anothers extra headers)  
Example:  
```
def index(view, template='templates.login.html'):
    my_template = open(template, 'r')
    return {'status_code': 200,
             "template": my_template.read(),
             'extra_headers': {'Content-Type': 'text/html'}
    }
```
