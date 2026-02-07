import time 
import os
import psutil
from multiprocessing import Process
from threading import Thread
from Sniffer import pack_info_extract

proc = psutil.Process(os.getpid()) #perf
proc.cpu_percent() #perf

t1 = Thread(target=pack_info_extract)
p1 = Process(target='PlaceHolder')

start = time.time() #perf

t1.start()
p1.start()


end = time.time() #perf

print(end-start," time taken") 
print(proc.cpu_percent()) 
print(proc.memory_info().rss/1024/1024, "MB ") 

# Threading - network information 
# Multi-processing - ML model