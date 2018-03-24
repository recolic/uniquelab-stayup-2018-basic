#!/usr/bin/env python3
import http.server, socketserver
import hashlib
import random
import subprocess

listen_port = 25566

def makedata(_size):
    res = subprocess.run(['./makedata', "--size", _size], check=True, stdout=subprocess.PIPE)
    return res.stdout

class my_handler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
    def do_GET(self):
        print('serving path "{}"'.format(self.path))
        ar = self.path.split('/')
        if len(ar) != 3 or ar[0] != '' or ar[1] != 'makedata':
            self.send_response(404)
            self.end_headers()
            self.wfile.write('404 not found'.encode('utf-8'))
            return
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        self.wfile.write(makedata(ar[2]))
#        self.wfile.close() # Seems no need

try:
    server = http.server.HTTPServer(('', listen_port), my_handler)
    print('Listening *:' + str(listen_port))
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
