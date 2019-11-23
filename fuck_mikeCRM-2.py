#!/usr/bin/python2
#coding=utf-8
import re
import io
import sys
import jieba
import argparse
from selenium import webdriver


#Basic
list1=[u'学号',u'名字',u'姓名',u'性别',u'班级',u'专业',u'专业班级',u'辅导员',u'手机号',u'联系方式',u'QQ',u'QQ号','qq',u'职务',u'手机']
list2=['19900912',u'张三',u'张三',u'男',u'19自动化3班',u'自动化',u'19自动化3班',u'李四','13811012138',u'13811012138','123456','123456','123456',u'学生','13811012138']
linked = dict(zip(list1,list2))

def GetSource():
    global str
    global b
    global matching
    url=bs.current_url
    bs.get(url)
    html = bs.page_source
    f = io.open('./source.txt',mode="w",encoding='utf-8')
    f.write(html)
    str = re.sub("[\!,\%,\[,\],\,,\.,\:,\<,\>,\",\-,\=,\/,\?,\;,\_,\$,\#,\",\\,\{,\},\*,\(,\),\\\\,\（,\）,\：,\s+]","", html)
    f = io.open('./result.txt',mode="w",encoding='utf-8')
    f.write(str)
    f = io.open('./result.txt','r',encoding='utf-8')
    str = f.read()
    f.close()
    jieba.load_userdict("./zidian.txt")
    BreakUp = list(jieba.lcut(str))
    matching = [l for l in BreakUp if l in list1]
    b = len(matching)/2
    Determine()

def GetSourceAutoSubmit():
    global str
    global b
    global matching
    url=bs.current_url
    bs.get(url)
    html = bs.page_source
    f = io.open('./source.txt',mode="w",encoding='utf-8')
    f.write(html)
    str = re.sub("[\!,\%,\[,\],\,,\.,\:,\<,\>,\",\-,\=,\/,\?,\;,\_,\$,\#,\",\\,\{,\},\*,\(,\),\\\\,\（,\）,\：,\s+]","", html)
    f = io.open('./result.txt',mode="w",encoding='utf-8')
    f.write(str)
    f = io.open('./result.txt','r',encoding='utf-8')
    str = f.read()
    f.close()
    jieba.load_userdict("./zidian.txt")
    BreakUp = list(jieba.lcut(str))
    matching = [l for l in BreakUp if l in list1]
    b = len(matching)/2
    DetermineAutoSubmit()

def Determine():
    xm = u'姓名'
    determine = xm in str
    print determine
    if determine:
        FillIn()
    else:
        GetSource()

def DetermineAutoSubmit():
    xm = u'姓名'
    determine = xm in str
    print determine
    if determine:
        FillInATsubmit()
    else:
        GetSource()

def FillIn():
    for i in range(b):
        bs.find_elements_by_class_name('fbi_input')[i].send_keys(linked.get(matching[i]))
        print (matching[i]) + ':' + (linked.get(matching[i]))

def FillInATsubmit():
    for i in range(b):
        bs.find_elements_by_class_name('fbi_input')[i].send_keys(linked.get(matching[i]))
        print (matching[i]) + ':' + (linked.get(matching[i]))
        bs.find_element_by_id('form_submit').click()

if __name__ == '__main__':
    global bs
    parser = argparse.ArgumentParser(prog='python2.7 fuck_mikeCRM-2.py', description="FuckingMikeCRM!")
    parser.add_argument('-u', dest='url', help="目标麦克表单地址")
    parser.add_argument('-A',dest='auto',help="-A y 启用自动提交")
    if len(sys.argv) == 0:
        sys.argv.append('-h')
    args = parser.parse_args()
    url = args.url
    autoSubmit = args.auto
    if '-u' in sys.argv:
        if (autoSubmit=='y'):
            ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 69_69 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3 NetType/WIFI Language/zh_CN'
            profiel = webdriver.FirefoxProfile()
            profiel.set_preference('general.useragent.override', ua)
            bs = webdriver.Firefox(firefox_profile=profiel)
            bs.get(url)
            GetSourceAutoSubmit()
        else:
            ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14.1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3 NetType/WIFI Language/zh_CN'
            profiel = webdriver.FirefoxProfile()
            profiel.set_preference('general.useragent.override', ua)
            bs = webdriver.Firefox(firefox_profile=profiel)
            bs.get(url)
            GetSource()
    else:
        print "无目标麦克表单地址, -h 查看使用说明"
