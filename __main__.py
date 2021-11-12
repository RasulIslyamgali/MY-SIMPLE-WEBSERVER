import datetime
import json
import socket
from db import *



def start_my_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 2000))

    server.listen(4)
    print("working...")
    while True:
        try:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode("utf-8")
            print("data from client: ", data)
            if "POST" in data:
                data_for_db = data.split("=")
                if len(data_for_db) == 9:
                    IIN = data_for_db[1].split("%22")[0]
                    status_exist_iin = check_exist_status_IIN(IIN=int(IIN), db_name="data_about_candidat_HCSBK.db", table_name="Candidat_Data")
                    print("IIN", IIN)
                    print("status_exist_iin", status_exist_iin)
                    print("LEN IIN ", len(IIN))
                    if len(IIN) == 12 and not status_exist_iin:
                        save_new_candidat(IIN=int(IIN))
                elif len(data_for_db) == 10:
                    if data_for_db[1] != "&FIO":
                        index_spliter = data_for_db[1].index("&")
                        DATA_KEY = data_for_db[1][index_spliter + 1:]

                        IIN = data_for_db[1][:len(data_for_db[1]) - (len(DATA_KEY) + 1)]
                        print("IIN 2", IIN)
                        DATA_VALUE = " ".join(data_for_db[2].split("%22")[0].split("%20"))
                        status_exist_iin = check_exist_status_IIN(IIN=int(IIN), db_name="data_about_candidat_HCSBK.db",
                                                                  table_name="Candidat_Data")
                        print("status_exist_iin 2 ", status_exist_iin)
                        if len(IIN) == 12 and status_exist_iin:
                            insert_data_to_db(IIN=int(IIN), row_name=DATA_KEY, value=DATA_VALUE)
                        else:
                            save_new_candidat(IIN=int(IIN))
                            print("DATA_KEY", DATA_KEY)
                            print("DATA_VALUE", DATA_VALUE)
                            insert_data_to_db(IIN=int(IIN), row_name=DATA_KEY, value=DATA_VALUE)
                print("data_for_db", data_for_db)
                print("len: ", len(data_for_db))
                print("i caought POST data: ", data)
            HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n".encode("utf-8")
            with open("temps/success_send_data.html", "rb") as file:
                response = file.read()
            content = HDRS + response
            if "FIO" in data:
                data = data.split("/home.html?")[-1].split("HTTP/1.1")[0].split("&")
                print(data)
                dict_for_json = {}
                for i, d in enumerate(data):
                    if i == 7:
                        break
                    try:
                        key, value = d.split("=")
                    except ValueError:
                        break
                    value = value.split("+")
                    value = " ".join(value)
                    dict_for_json[key] = value
                with open(f"data_json_{datetime.datetime.today().strftime('%Y%m%d%M%S')}.json", "w") as file:
                    json.dump(dict_for_json, file, ensure_ascii=False, indent=4)
                client_socket.send(content)
                client_socket.shutdown(socket.SHUT_WR)
                continue
            content = load_page_from_get_request(request_data=data)

            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
            print("data === ", data)

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