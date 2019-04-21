#coding=utf-8
import re
import io
import time
import self
import jieba
from selenium import webdriver

#基本信息
list1=[u'学号',u'名字',u'姓名',u'性别',u'班级',u'专业',u'专业班级',u'辅导员',u'手机号',u'联系方式',u'QQ',u'QQ号','qq',u'职务',u'手机']
list2=['XXXXXXXX',u'XXXXXX',u'XXXXXXX',u'X',u'XXXXXXXX',u'XXXXX',u'XXXXX',u'XXX','XXXXXXXXX',u'XXXXXXX','XXXXXXXX','XXXXXXX','XXXXX',u'XXXXX','XXXXXX']
guanlian = dict(zip(list1,list2))

#要在看到表单页面之后再加载源码！


#更改UserAgent绕过只能在微信内填写表单
ua='Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3 NetType/WIFI Language/zh_CN'
profiel = webdriver.FirefoxProfile()
profiel.set_preference('general.useragent.override',ua)
bs=webdriver.Firefox(firefox_profile=profiel)


print ('Input your url:')
url = raw_input()
print url

#打开网址
bs.get(url)
#html = bs.page_source
print (u'==================================================\n继续运行请输入 1 ')
panduan = input()
if panduan == 1:
    
    url=bs.current_url
    bs.get(url)
    html = bs.page_source
    #获取源码&正则表达式获取中文内容
    f = io.open('./source.txt',mode="w",encoding='utf-8')
    f.write(html)
    str = re.sub("[\!,\%,\[,\],\,,\.,\:,\<,\>,\",\-,\=,\/,\?,\;,\_,\$,\#,\",\\,\{,\},\*,\(,\),\\\\,\（,\）,\：,\s+]","", html)

    #结果写入result.txt文件
    f = io.open('./result.txt',mode="w",encoding='utf-8')
    f.write(str)

    #结果赋值给字符串
    f = io.open('./result.txt','r',encoding='utf-8')
    str = f.read()
    f.close()

    #head, sep, tail = str.partition(u'请') #删除请后面的内容
    #print head

    #读取一个字典
    jieba.load_userdict("./zidian.txt")
    fenge = list(jieba.lcut(str))

    #顺序不改变的情况下匹配各个字符串
    matching = [l for l in fenge if l in list1]

    #麦克表单源码的原因，相同的字符串会出现两次
    b = len(matching)/2

    for i in range(b):
        bs.find_elements_by_class_name('fbi_input')[i].send_keys(guanlian.get(matching[i]))
        print (matching[i])+':'+(guanlian.get(matching[i]))
       # print guanlian.get(matching[i])
    print '++++++++++'
    print '+ !DONE! +'
    print '++++++++++'
