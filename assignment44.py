import time
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
mytime = (2016,7,27,15,45,23,0,0,0)
print(time.localtime(time.mktime(mytime)))

# OUTPUT
1538166261.7738233
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=29, tm_hour=1, tm_min=54, tm_sec=21, tm_wday=5, tm_yday=272, tm_isdst=0)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=29, tm_hour=1, tm_min=54, tm_sec=21, tm_wday=5, tm_yday=272, tm_isdst=0)
# Sat Sep 29 01:54:21 2018
# time.struct_time(tm_year=2016, tm_mon=7, tm_mday=27, tm_hour=15, tm_min=45, tm_sec=23, tm_wday=2, tm_yday=209, tm_isdst=0)