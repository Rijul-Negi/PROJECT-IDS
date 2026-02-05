import time 
import os
import psutil
from threading import Thread
from Sniffer import pack_info_extract

proc = psutil.Process(os.getpid())
proc.cpu_percent()
start = time.time()

pack_info_extract()
end = time.time()

print(end-start," time taken") 
print(proc.cpu_percent()) 
print(proc.memory_info().rss/1024/1024, "MB ") 