import urllib.request
import re

url = input('Enter the url please: \n')

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

# To find paragraphs
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

# To print paragraphs
num = 0
for each_para in paragraphs:
	print("(%d) "%num+each_para+"\n")
	num += 1

