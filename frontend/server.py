import http.server
import socketserver

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        elif self.path == '/favicon.ico':
            self.path = 'favicon.ico'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = RequestHandler
PORT = 8000
HOST = "127.0.0.1"
print(bcolors.OKGREEN + "Serving at {}:{}".format(HOST, PORT) + bcolors.ENDC)
server = socketserver.TCPServer(("",PORT), handler_object)

server.serve_forever()
