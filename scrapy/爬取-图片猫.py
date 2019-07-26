import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()
with open("cat_img.jpg", "wb") as fw:  # 切记类型，当前用二进制
    fw.write(cat_img)
