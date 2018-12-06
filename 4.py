import socket
import platform
hostname = 'localhost'
pesan =''
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50015))
print 'mesin penjawab otomatis siap'
while pesan.lower() !='q' :
    pesan = raw_input('pertanyaan: ')
    s.send(pesan)
    if pesan.lower()=='quit':
            print('SIAP !!!')
            s.close()
            break
    elif pesan.lower() !='q':
        response =s.recv(1024)
        print 'jawab:' , response
s.close()
