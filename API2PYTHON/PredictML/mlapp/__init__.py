from flask import Flask
app = Flask(__name__)
class PrefixMiddleware(object):
    # class for URL sorting
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        # in this line I'm doing a replace of the word flaskredirect which is my app name in IIS to ensure proper URL redirect
        if environ['PATH_INFO'].lower().replace('/predictml', '').startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'].lower().replace(
                '/predictml', '')[len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]


app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False
import mlapp.mod_cust_identification.controllers