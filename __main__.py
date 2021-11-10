import socket


def start_my_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 2000))

    server.listen(4)
    print("working...")
    while True:
        try:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode("utf-8")
            content = load_page_from_get_request(request_data=data)

            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            print("Close with KeyboardInterrupt")
            server.close()


def load_page_from_get_request(request_data):
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")  # headers
    HDRS_404 = "HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")
    try:
        path = request_data.split(" ")[1]
    except Exception as e:
        print('EXCEPTION IN PATH: ------ ', e)
        print("request_data: ------- ", request_data)
        return HDRS_404 + "Uuups. Something is crushed".encode("utf-8")

    response = ""
    try:
        with open("temps" + path, "rb") as file:
            response = file.read()
        return HDRS + response
    except FileNotFoundError:
        return HDRS_404 + "Uuups. Page Not Found".encode("utf-8")
    except Exception as e:
        print('EXCEPTION: ------ ', e)
        print("request_data: ------- ", request_data)
        return HDRS_404 + "Uuups. Something is crushed".encode("utf-8")


if __name__ == "__main__":
    start_my_server()