from Faloodeh_WSGI import faloorun


def application(environ, start_response):
    body = b'Hello world! this is test...\n'
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [body]

if __name__ == '__main__':
    faloorun('127.0.0.1', 8000, application)