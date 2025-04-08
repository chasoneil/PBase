
import threading
import time

def worker():
    try:
        print("worker started!")
        time.sleep(2)
        print("worker finished!")
    except TypeError:
        print("caught error!")

print("main thread start...")

# 这里的target写worker() 还是worker都是正确的
t = threading.Thread(target=worker, args=())
t.start()

t.join()
print("main thread finished!")
