from .server.server import Session
import socket
import threading
import time



class WSGIServer:
    def __init__(self, host: str, port: int, app):
        self.host = host
        self.port = port
        self.app = app

    def serve_forever(self):
        server_socket = socket.socket()
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)

        try:
            while True:
                client_socket, address = server_socket.accept()
                print(f"Socket established with {address}.")
                session = Session(client_socket, address, self.app)
                t = threading.Thread(target=session.run)
                t.start()
        except KeyboardInterrupt:
            print('server closed by CTRL+C !!!')
            exit()


def faloorun(host: str, port: 8686, app):
    print(f'[ server is running on "http://{host}:{port}/, at {time.ctime(time.time())} successfully! ]')
    print(' powered by Amir Mohammad Dehghan')
    run_server_by_wsgi = WSGIServer(host, port, app)
    run_server_by_wsgi.serve_forever()
