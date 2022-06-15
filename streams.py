import threading
import requests
import shutil
import os

def down(nomer, url):
    print(str(nomer) + 'поток ('+url+')\n')
    (dirname,filename) = os.path.split(url) #get filename from url
    
    r = requests.get(url, stream=True) #get file from get request
    
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw,f)
    print(str(nomer) + 'поток закончил загрузку\n')


urls = input('enter links separated by spaces ').split() #or array
for nomer, url in enumerate(urls):
    threading.Thread(target = down, args=[nomer+1, url]).start()


#threading decorator

def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args = args, kwargs=kwargs)
        my_thread.start()
    return wrapper

#just @thread for threading 