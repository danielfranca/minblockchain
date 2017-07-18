import http.server
import socketserver


class HTTPHandler(http.server.BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()        
    
    def home(self):
        pass

    def mine(self):
        pass

    def genesis(self):
        pass

    def discover(self):
        pass

    def do_GET(self):
        self._set_headers()

        if path == '/':
            self.home()
        elif path == '/mine':
            self.mine()
        elif path == '/genesis':
            self.genesis()
        elif path == 'discover':
            self.discover()
        #self.wfile.write(b"<html><body><h1>Nothing </h1><p>A paragraph goes here</p></body></html>")


def run_http_server(port: int) -> None:
    server = socketserver.TCPServer(("", port), HTTPHandler)
    print("serving at port", port)
    server.serve_forever()
