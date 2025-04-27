from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/main.html':
            super().do_GET()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

with HTTPServer(('', PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()