"""
Python common modules
- Runtime service related modules: copy / pickle / sys / ...
- Math related modules: decimal / math / random / ...
- String processing module: codecs / re / ...
- File processing related modules: shutil / gzip / ...
- Operating system service related modules: datetime / os / time / logging / io / ...
- Process and thread related modules: multiprocessing / threading / queue
- Network application related modules: ftplib / http / smtplib / urllib / ...
- Web programming related modules: cgi / webbrowser
- Data processing and encoding modules: base64 / csv / html.parser / json / xml / ...

"""

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(strtime)
mydate = time.strptime('2018-1-1', '%Y-%m-%d')
print(mydate)

shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system('ls -l')
os.chdir('/Users/Hao')
os.system('ls -l')
os.mkdir('test')