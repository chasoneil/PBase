# multiple thread
# use _thread (python2 -> thread) OR threading
# use start_new_thread to create a thread

import _thread
import time

def duty(name):
    print(name, "start do duty...")
    time.sleep(3.0)
    print(name, "finish duty")

print("program start!")
try:
    _thread.start_new_thread( duty, ("Thread1",))
    _thread.start_new_thread( duty, ("Thread2",))
except:
    print("Start thread exception!")

# 如果这里不延时，那么主线程结束子线程也跟着结束
# 子线程不会输出
time.sleep(5.0)
print("program end!")