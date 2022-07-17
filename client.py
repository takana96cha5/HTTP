import socket

def main():
    request = 'GET / HTTP/1.1\nHost: localhost\n\n'
    response = http_client(request)
    print(response)

def http_client(http_request:str) -> str:
    """python で実装された最小のHTTPクライアント"""
    encoded_request = http_request.encode('utf-8') 

    # 通信プロコトルの定義
    HOST = "localhost"
    PORT = 8000
    IP_v4 = socket.AF_INET 
    TCP_socket = socket.SOCK_STREAM

    # リクエスト送信
    client = socket.socket(IP_v4, TCP_socket)
    client.connect((HOST, PORT))
    client.send(encoded_request)

    # レスポンス受信
    http_response = client.recv(1024)
    client.close()
    return http_response

if __name__ == "__main__" :
    main()
