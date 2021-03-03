import socket
import re 
import inspect

def connect_to_server(ip, port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))
    return s

def start_server():
    s = socket.socket()
    s.bind(('127.0.0.1', 8000))
    s.listen(5)
    return s


def get_source(host, page, s):
    CRLF = '\r\n' #specijalni znakovi koji oznacavaju kraj kraj (tj novi red) \r povratak na pocetak reda \n novi red
    request = 'GET /' + page + ' HTTP/1.1' #svaki get request poslan serveru se sastoji od Get/ + stranica + vrsta requesta(http/1.1)
    request += CRLF 
    request += 'Host: ' + host + CRLF #host je stranica iz koje cemo izvlacit ono sto zelimo
    request += CRLF

    s.sendall(str.encode(request)) #ascii tablica za posebne srednjoeuropske znakove
    return s.recv(100000).decode()

def get_links(source,link_list):
    
    beg = 0
    while True:    
        beg_link = source.find('href="', beg)
        if beg_link == -1:
            return link_list
        end_link = source.find('"', beg_link + 6)
        link = source[beg_link + 6:end_link]
        beg = end_link + 1
        if link not in link_list:
            link_list.append(link)
        
    return link_list
        
link_list = []
s = connect_to_server("www.watchthatpage.com", 80) #80 for HTTP and 443 for HTTPS
source = get_source("www.watchthatpage.com","watchPages.jsp" ,s )
link_list=(get_links(source,link_list))


for x in range(0,30):
    source = get_source("www.watchthatpage.com",link_list[x] ,s )
    link_list=(get_links(source,link_list))
    

link_list=link_list[:50]
print(link_list)
s.close()
