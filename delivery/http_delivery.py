from http.server import BaseHTTPRequestHandler, HTTPServer

class PayloadRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, payload, *args):
        self.payload = payload
        super().__init__(*args)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(self.payload.encode())

def start_http_server(payload: str, port: int):
    def handler(*args):
        PayloadRequestHandler(payload, *args)

    server = HTTPServer(('0.0.0.0', port), handler)
    print(f"[+] HTTP Server started on port {port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] HTTP Server stopped.")
        server.server_close()
