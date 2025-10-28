# python 中的时间
# python 中的时间模块
import time

# 1. 获取时间当前时间戳
time_stamp = time.time()
print(time_stamp)
# 输出： 1743476882.3974473

# 2. 获取当前的时间
local_time = time.localtime(time.time())
print(local_time)
# 输出： time.struct_time(tm_year=2025, tm_mon=4, tm_mday=1, tm_hour=11, tm_min=10, tm_sec=33, tm_wday=1, tm_yday=91, tm_isdst=0)

# 3. 格式化当前时间1
f_time1 = time.asctime(time.localtime(time.time()))
print(f_time1)
# 输出：Tue Apr  1 11:12:20 2025

# 4. 按照指定的格式格式化时间
f_time2 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(f_time2)
# 输出：2025-04-01 11:15:45

# 5. 将格式化的时间转化成时间戳
t = "2025-04-01 11:15:45"
time_stamp1 = time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S"))
print(time_stamp1)
# 输出：1743477345.0

# -------------------------------
# python 提供另外一个 calendar

import calendar

# 如果想获取全年的日历 calendar.calendar(2025)
cal = calendar.month(2025, 4)
print("2025年4月的日历：")
print(cal)

'''
输出：
2025年4月的日历：
     April 2025
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
'''