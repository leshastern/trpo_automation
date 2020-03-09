from http.server import HTTPServer, CGIHTTPRequestHandler
import socket
import time

server_address = ("127.0.0.1", 8080)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()