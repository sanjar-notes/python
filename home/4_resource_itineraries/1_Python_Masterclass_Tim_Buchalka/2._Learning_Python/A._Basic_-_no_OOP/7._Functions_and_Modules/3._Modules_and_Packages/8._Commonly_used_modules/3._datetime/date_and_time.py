import time
start = time.strftime('%H:%M:%S', time.localtime())
i =0
while True:
    if (start != time.strftime('%H:%M:%S', time.localtime())):
        print('Ops per second:',i/10**3, '\bk')
        break
    i+=1
