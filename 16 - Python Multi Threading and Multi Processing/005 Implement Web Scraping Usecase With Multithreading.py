'''
real-world example:multithreading for i/o bound tasks
scenario:web screaping
web scraping often invloves making numerous network request tp fectch
web page.these taks are io bound because they spend a lot of time waiting
for responces from servers.mutlithreading can significntly 
improve the perfromence by allowing multiple web pages to be fectched concurrently
'''
import threading
import requests
from bs4 import BeautifulSoup
urls=[
'https://smith.langchain.com/o/08b2e92d-cb1e-441c-90ca-5bea9adadc8f/projects',
'https://smith.langchain.com/o/08b2e92d-cb1e-441c-90ca-5bea9adadc8f',
'https://smith.langchain.com/o/08b2e92d-cb1e-441c-90ca-5bea9adadc8f/dashboards?paginationModel=%7B%22pageIndex%22%3A0%2C%22pageSize%22%3A10%7D'
]
def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"fetch{(len(soup.text))} charcaters from{url}")
threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print("all web pages fetched")