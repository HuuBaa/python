from wsgiref.simple_server import make_server
from hello import application
httpd=make_server('', 8080, application)
print('Server HTTP on port 8080')
httpd.serve_forever()

