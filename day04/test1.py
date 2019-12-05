import urllib.request
import chardet
import re

if __name__ == '__main__':
    page = urllib.request.urlopen('http://photo.sina.com.cn/')
    htmlCode = page.read()
    # print(chardet.detect(htmlCode))
    encod = chardet.detect(htmlCode).get('encoding')
    # print(encod)
    data = htmlCode.decode(encod)
    # print(data)
    # print(htmlCode.decode('utf-8'))

    # pageFile = open('pageCode.txt','wb')
    # pageFile.write(htmlCode)
    # pageFile.close()

    reg = r'src="(.+?\.jpg)"'
    reg_img = re.compile(reg)
    imglist = reg_img.findall(data)
    x = 0
    for img in imglist:
        print(img)
        urllib.request.urlretrieve('http://ppic.meituba.com/uploads/160322/8-1603220U50O23.jpg', '%s.jpg'  % x)
        x += 1