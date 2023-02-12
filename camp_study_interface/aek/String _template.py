from  string import  Template
ss = {"token":"1111111222"}

url = "http://www.baidu.com?token=${token}"
print(Template(url).substitute(ss))