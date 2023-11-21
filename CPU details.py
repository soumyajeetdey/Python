'''
write a program to display the below information  ( psutil library)

-CPU percentage
-virtual memory
-swap memory
-disk partitions
-disk usage
-display boot time
- users who are logged in
- display all the processes running

'''

import psutil
import datetime
print("CPU percentage :",psutil.cpu_percent())
print("Virtual memory :",psutil.virtual_memory())
print("Swap memory stat :",psutil.swap_memory())
print("Disk partitions :", psutil.disk_partitions())
print("Disk usage :",psutil.disk_usage())
print("Boot time :",psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
print("Users logged in :",psutil.users())
print("Processes running",psutil.process_iter())
