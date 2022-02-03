import socket
import ipaddress
print("""(`| / /|(`-|-/\|\ |
_)|/ /-|_) | \/| \|""")
print("IP:")
print(" [1].сканер портов")
print(" [2].узнать свой айпи")
print(" [3].узнать айпи сайта")
print(" [4].проверить айпи адрес на приватность")
while 1 == 1:
    chs = input(">>>")
    if chs == "1":
        ipi = input("введите айпи:")
        def scan_port(ip,port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            try:
                connect = sock.connect((ip,port))
                print('Порт:',port,'открыт.')
                sock.close()
            except:
                pass
        ip = (ipi)
        for i in range(1000):
            scan_port(ip,i)
    if chs == "2":
        my_ip = socket.gethostbyname_ex(socket.gethostname())
        print("Ваш айпи:", my_ip[2][0])
    if chs == "3":
        pichs = input("Введите сайт:")
        ip = socket.gethostbyname(pichs)
        print(ip)
    if chs == "4":
        ipch = input("Введите своё айпи:")
        ipa = ipaddress.ip_address(ipch)
        print(ipa.is_private, "Ваш адрес приватный?")
        print(ipa.is_global, "Ваш адрес глобальный?")
        
        
        
        
        
        
