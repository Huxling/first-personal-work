import requests
import re

head = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
                                                                #头文件，防止反爬
cursor = '0'
source = '1614136297251'
list1 = []
list_re = []
m = 500                                                        #爬取五千条评论
for i in range(0, m):
    url = "https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" \
            + cursor +"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=" + source
    html = requests.get(url, headers=head).content.decode()
    list1 = re.findall('"content":"(.*?)"', html, re.S)        #爬取新的十个评论
    list_re = list_re + list1                                  #将新的十个评论和总的爬取的评论合并
    print("进度:%d" % (i))
    cursor ="".join(re.findall('"last":"(.*?)"', html, re.S))  #通过正则获取last值，赋给cousor
    source = str(int(source)+1)                                #每次source值加一
str_result = "\n".join(list_re)
with open('result.txt', 'w', encoding='utf-8') as fi:
    fi.write(str_result)
print('保存成功')