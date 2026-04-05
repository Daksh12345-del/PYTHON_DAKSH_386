import multiprocessing
import requests
def downloadFile(url,name):
    response = requests.get(url)
    open(f"file{name}.jpg","wb").write(response.content)

url="https://picsum.photos/200/300"
for i in range(5):
    downloadFile(url,i)