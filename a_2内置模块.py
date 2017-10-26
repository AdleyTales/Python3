import urllib2

res = urllib2.urlopen("https://api.douban.com/v2/book/2129650")

print(res.read())