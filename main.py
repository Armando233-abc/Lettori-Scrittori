import threading


lettori = 0
file = ""
mutex = threading.Semaphore(1)
scrivi = threading.Semaphore(1)

# funzioni 
def lettore():
    global lettori, file
    mutex.acquire()
    lettori += 1
    if lettori == 1:
        scrivi.acquire()
    mutex.release()
    file = open("lettura.txt", "r").read()
    print("il lettore ha letto")
    mutex.acquire()
    lettori -= 1
    if lettori == 0:
        scrivi.release()

    mutex.release()
    


def scrittore():
    scrivi.acquire()
    file = open("lettura.txt", "a")
    file.write("lo scrittore ha scritto\n")
    file.close()
    scrivi.release()


# main
lettore()
lettore()

scrittore()