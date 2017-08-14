import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import http.cookiejar

# params  CategoryId=808 CategoryType=SiteHome ItemListActionName=PostList PageIndex=3 ParentCategoryId=0 TotalPostCount=4000
def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'User-Agent':user_agent}
    data = urllib.parse.urlencode(values)
    request = urllib.request.Request(url=url+'?'+data,headers=headers)
    cookie = http.cookiejar.MozillaCookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response_result = opener.open(request).read()
    html = response_result.decode('utf-8')
    return html

def toModel(bsObj):
    m={}
    m['title']=bsObj.select_one(selector='div #cate_title_block')
    return m

def getMth(url):
    print(url)
    html=BeautifulSoup(getHtml(url=url,values={}), 'html.parser')
    m=toModel(html)
    print(m)

#print(requestCnblogs(1))
#getMth('https://www.tianyancha.com/company/186998025')
getMth('http://www.cnblogs.com/')