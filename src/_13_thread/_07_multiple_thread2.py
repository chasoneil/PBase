# use threading
# advance thread usage

# more : https://blog.csdn.net/qq_66544550/article/details/140911528

import threading
import time

def worker(name):
    print(name,"start working...")
    time.sleep(2)
    print(name,"stop working...")

print("Main thread start...")
t = threading.Thread(target=worker, args=("Thread1",))
t.start()

# wait for thread to finish
t.join()
print("Main thread stop...")