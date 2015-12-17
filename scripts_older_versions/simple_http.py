#!/usr/bin/env python3
import os, sys, netifaces as ni
from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import call

class WelcomeHandler(BaseHTTPRequestHandler):
    error_message_format = '<h1>Har har</h1>'
    def do_GET(self):
        #super().do_GET()
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes(htmlpage, 'UTF-8'))
        else:
            self.send_error(404, notfound)

if __name__ == '__main__':
    ip = ni.ifaddresses('eth0')[2][0]['addr']
    port = int(sys.argv[1])
    htmlpage = '<html><head><title>SAF Web</title></head><body><p>Simple server</p>\
    </body></html>'
    notfound = "File not found"
    call(['/opt/httpComponent/send_trace.o', str(os.getpid()), '1'])
    httpserver = HTTPServer((ip, port), WelcomeHandler)
    httpserver.serve_forever()