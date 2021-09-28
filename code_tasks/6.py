from helpers.__db import db_mock_with_exception
from http.server import BaseHTTPRequestHandler
from helpers import http_server


# urllib3 for url parse


class PasswordHandler(BaseHTTPRequestHandler):
    # Handler for the POST password request
    def do_POST(self):
        print('Get post received')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)

        db_api_resp = db_mock_with_exception(post_body)
        self.wfile.write(db_api_resp.encode())
        return


if __name__ == "__main__":
    server = http_server.Server(handler=PasswordHandler)
    server.run()
