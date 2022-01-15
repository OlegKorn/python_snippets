import requests, os, re, time
import wget 


file = "G:/Pictures/anna x/links.txt"
path = "G:/Pictures/anna x/"

def download():
    c = 0

    urls = open(file).readlines()
    
    for i in urls:
        url = i.split(": ")[1].strip().replace('"', "")
        album = re.search(r'galleries/(.*?)/', url).group(1)
        file_name = album + "_" + str(c)

        try:
            session = requests.Session()
            r = requests.get(url, stream=True)
            image = r.raw.read()
            open(f"{path}{file_name}.jpg", "wb").write(image)
                            
            c += 1

            print(f"{c} - {url}")
                        
        except Excsseption as e:
            print(f"{e}\n{url}\n")
            pass
    
download()

