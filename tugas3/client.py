import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpeg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':
    # Isi list URL yang ingin didownload
    list_url = [
        'https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg',
        'https://www.its.ac.id/wp-content/uploads/2019/02/Logo-its-biru-transparan.png',
        'https://seeklogo.com/images/I/institut-teknologi-sepuluh-nopember-logo-DD303AEE34-seeklogo.com.png'
    ]
    for i in range(len(list_url)):
        t = threading.Thread(target=download_gambar, args=(list_url[i], ))
        t.start()