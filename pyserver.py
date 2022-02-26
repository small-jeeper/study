import os
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HTTPGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        filsl =[slug for slug in self.path.split("/") if slug != '']
        text = 'Был получен GET-запрос'
        if len(filsl) != 0 and filsl[0] == 'hello':
            text = 'world'
        print(filsl)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.render(text)

    def render(self, text):
        indexPath = os.path.join('.', 'template', 'index.html')
        with open(indexPath, 'r', encoding="utf8") as file:
            template = file.read()
            template = template.replace("{div_placeholder_1}", text)

        self.wfile.write(template.encode())

run(handler_class=HTTPGetHandler)