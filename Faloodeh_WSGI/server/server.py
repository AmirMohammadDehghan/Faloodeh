from .http_parse import HttpRequestParser
from .wsgi import WSGIRequest, WSGIResponse
import time


class Session:
    def __init__(self, client_socket, address, app):
        self.client_socket = client_socket
        self.address = address
        self.app = app
        self.parser = HttpRequestParser(self)
        self.request = WSGIRequest()
        self.response = WSGIResponse()

    def run(self):
        while True:
            if self.response.is_sent:
                break
            data = self.client_socket.recv(1024)
            # print(f"[ Received {data}  at {time.ctime(time.time())}. ]")
            self.parser.feed_data(data)
        self.client_socket.close()
        print(f"[ Socket with {self.address} closed at {time.ctime(time.time())}. ]")

    # parser callbacks
    def on_url(self, url: bytes):
        print(f"[ Received url: {url} , at {time.ctime(time.time())}. ]")
        self.request.http_method = self.parser.http_method.decode("utf-8")
        self.request.path = url.decode("utf-8")

    def on_header(self, name: bytes, value: bytes):
        print(f"[ Received header: ({name}, {value}),  at {time.ctime(time.time())}. ]")
        self.request.headers.append(
            (name.decode("utf-8"), value.decode("utf-8"))
        )

    def on_body(self, body: bytes):
        print(f"[ Received body: {body},  at {time.ctime(time.time())}. ]")
        self.request.body.write(body)
        self.request.body.seek(0)

    def on_message_complete(self):
        print(f"[ Received request completely at {time.ctime(time.time())}. ]")
        environ = self.request.to_environ()
        body_chunks = self.app(environ, self.response.start_response)
        print("App callable has returned by Faloodeh.")
        self.response.body = b"".join(body_chunks)
        self.client_socket.send(self.response.to_http())
