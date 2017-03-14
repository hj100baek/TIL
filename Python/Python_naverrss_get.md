```python
import feedparser
import os
import urllib3
import re

#naver에서 가져온 rss를 local git에 저장
directory = "C:\\Users\\hj\\Documents\\GitHub\\TIL\\naver_rss\\"
#naver에서 가져올 rss에서 내용은 별도 iframe으로 되있어서 별도 주소 필요
url_prefix = "http://blog.naver.com/PostView.nhn?blogId=skyalzza&logNo="
#d = feedparser.parse('http://rss.ohmynews.com/rss/economy.xml')
#naver에서 가져올 rss주소
d = feedparser.parse('http://blog.rss.naver.com/skyalzza.xml')
http = urllib3.PoolManager()

for post in d.entries:
    print(post.published[:12])
    print(post.link[len(post.link)-12:])
    print(post.title)
    file_title = post.title.replace("?","").replace("/","").replace(":","").replace(" ","")
    file_title = file_title + "_"+post.link[len(post.link)-12:]
    file = open(os.path.join(directory, file_title+".md"),"wb")
    #contents = post.description.encode('utf-8')
    urllink  = url_prefix + post.link[len(post.link)-12:]

    contents = http.request('GET', urllink).data
    contents = contents.decode("ms949").encode("utf-8") #한글안깨지게하기 위함

    extract_lines = bytes('##'+post.title+'\n', encoding = 'utf-8')
    extract_flag = "off"
    linebyline = contents.splitlines()
    for line in linebyline:
        if "postViewArea" in str(line) :
            extract_lines = extract_lines + line
            extract_flag = "on"
            #print(extract_lines)

        if extract_flag == "on" :
            extract_lines = extract_lines + line
            #print(extract_lines)

        if extract_flag == "on" and "</div>" in str(line) :
             extract_lines = extract_lines + line
             #print(extract_lines)
             extract_flag = "off"
             break

    file.write(extract_lines)
    file.close()
```
