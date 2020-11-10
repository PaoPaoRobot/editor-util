import wget
import os
data_url_prefix = 'https://ras.papercept.net/proceedings/IROS20/'

import urllib.request
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for i in range(3958, 9999, 1):
    name = str(i).zfill(4)
    file_name = name + ".pdf"
    print(file_name)
    try:
        urllib.request.urlretrieve(data_url_prefix+file_name, file_name)
    except Exception:
        continue

    
