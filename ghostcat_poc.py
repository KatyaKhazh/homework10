import socket  # библиотека для работы с сетевыми соединениями

target_host = "127.0.0.1"  # адрес целевого сервера
target_port = 8009        # стандартный порт AJP

try:
    # создаём TCP-сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)  # таймаут 3 секунды

    # пытаемся подключиться к серверу
    result = sock.connect_ex((target_host, target_port))

    if result == 0:
        print("[+] Порт 8009 (AJP) открыт.")
        print("[!] Возможна уязвимость CVE-2020-1938 (Ghostcat), если используется уязвимая версия Tomcat.")
    else:
        print("[-] Порт 8009 закрыт или недоступен.")

    sock.close()

except Exception as e:
    print("Ошибка при проверке:", e)
