import http.server, socketserver
import hashlib
import random

listen_port = 25565
data_size = 100
pswd_modified_rate = 1

def get_md5(text):
    obj = hashlib.md5(text.encode())
    return obj.hexdigest()

def index_to_id(index):
    assert(index > 0 and index < 100000)
    return 'U2017' + str(index).zfill(5)

def random_spaces():
    res = ' '
    for _ in range(random.randint(0, 5)):
        res += ' '
    return res

def gen_id_pswd(uid):
    global data_size
    random.seed(uid)

    result_str = '# UniqueLab Question Data for {}, by Recolic<root@recolic.net>\n\n id, password\n'.format(uid)

    for i in range(data_size):
        i += 1
        if random.random() < pswd_modified_rate:
            tmp_str = random_spaces() + index_to_id(i) + random_spaces() + get_md5('wmy' + uid + index_to_id(i))
        else:
            tmp_str = random_spaces() + index_to_id(i) + random_spaces() + get_md5(index_to_id(i))
        result_str += tmp_str
        result_str += '\n'
    return result_str


class my_handler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
    def do_GET(self):
        print('serving path "{}"'.format(self.path))
        ar = self.path.split('/')
        if len(ar) != 3 or ar[0] != '' or ar[2] != 'id_pswd.dat':
            self.send_response(404)
            self.end_headers()
            self.wfile.write('404 not found'.encode('utf-8'))
            return
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        self.wfile.write(gen_id_pswd(ar[1]).encode('utf-8'))
#        self.wfile.close() # Seems no need

try:
    server = http.server.HTTPServer(('', listen_port), my_handler)
    print('Listening *:' + str(listen_port))
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()