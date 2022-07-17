import http.server
import socketserver

def main():
    http_server()

def http_server():
    """python で実装された最小のHTTPサーバー"""

    HOST = "localhost"
    PORT = 8000
    Hnandler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer((HOST, PORT), Hnandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__ == "__main__" :
    main()