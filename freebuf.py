
import requests
import re

rq = reuqests.get("http://www.freebuf.com")
rq.encoding = "utf-8"
rqre = re.findall('<dl>.*?</dl>',rq.text)
for dl in rqre:
  dt = re.search('<dt>.*?</dt>',dl)
  name = re.search('<span class="name.*?</span>',dl)
  text = re.search('<dd class="text.*?</dd>',dl)
  t = re.search('   .*?   ',dt)
  print "标题：" + t
