from webob import Request, Response
from jinja2 import Environment, FileSystemLoader
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from whitenoise import WhiteNoise
from .middleware import Middleware
from parse import parse
import inspect
import os


class Faloodeh:
    def __init__(self,  templates_dir="templates", static_dir="static"):
        self.templates_env = Environment(loader=FileSystemLoader(os.path.abspath(templates_dir)))
        self.exception_handler = None
        self.routes = {}
        self.whitenoise = WhiteNoise(self.wsgi_app, root=static_dir)
        self.middleware = Middleware(self)
        self.port = '8080'
        self.host = '127.0.0.1'

    def add_route(self, path, handler):
        assert path not in self.routes, "Such route already exists."

        self.routes[path] = handler

    def route(self, path):
        assert path not in self.routes, "Such route already exists."

        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper
    

    def template(self, template_name, context=None):
        if context is None:
            context = {}

        return self.templates_env.get_template(template_name).render(**context)


    def test_session(self, base_url="http://testserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session


    def add_exception_handler(self, exception_handler):
        self.exception_handler = exception_handler


    def wsgi_app(self, environ, start_response):
        environ['SERVER_PORT'] = str(self.port)
        environ['SERVER_NAME'] = str(self.host)
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)


    def __call__(self, environ, start_response):
        path_info = environ["PATH_INFO"]

        if path_info.startswith("/static"):
            environ["PATH_INFO"] = path_info[len("/static"):]
            return self.whitenoise(environ, start_response)

        return self.middleware(environ, start_response)

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named

        return None, None

    def handle_request(self, request):
        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            if inspect.isclass(handler):
                handler = getattr(handler(), request.method.lower(), None)
                if handler is None:
                    raise AttributeError("Method now allowed", request.method)

            handler(request, response, **kwargs)
        else:
            self.default_response(response)

        return response


    def default_response(self, response):
        response.status_code = 404
        response.text = "404 Not found."