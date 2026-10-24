#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:
    webbrowser.open(f'http://localhost:{PORT}')
    print(f'Server running at http://localhost:{PORT}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
