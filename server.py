import http.server
import socketserver

PORT = 25580
# PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("server started, listening to port: ", PORT)
    httpd.serve_forever()