from http.server import SimpleHTTPRequestHandler, HTTPServer

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)  # Serve on port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting http server on port 8000...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
