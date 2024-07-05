import threading
import time
def f_square(n):
    for i in n:
        time.sleep(0.5)
        print("Square=",n*n)
def f_cube(n):
    for i in n:
        time.sleep(0.3)
        print("Cube=",n*n*n)
a=[1,2,3,4]
t1=threading.Thread(target=f_square,args=(a,))
t2=threading.Thread(target=f_cube,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()