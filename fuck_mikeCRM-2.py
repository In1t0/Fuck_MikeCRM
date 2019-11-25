#!/usr/bin/python2
#coding=utf-8
import re
import io
import sys
import time
import jieba
import datetime
import argparse
from selenium import webdriver
from dateutil.parser import parse

#Basic
list1=[u'学号',u'名字',u'姓名',u'性别',u'班级',u'专业',u'专业班级',u'辅导员',u'手机号',u'联系方式',u'QQ',u'QQ号','qq',u'职务',u'手机']
list2=['19900912',u'张三',u'张三',u'男',u'19自动化3班',u'自动化',u'19自动化3班',u'李四','13811012138',u'13811012138','123456','123456','123456',u'学生','13811012138']
linked = dict(zip(list1,list2))

def GetTime():
    now = datetime.datetime.now()
    StrfTime = now.strftime('%H:%M')
    StrfTime2 = now.strftime('%H:%M:%S')
    print ("当前时间->"+StrfTime2+"<-")
    SleepingTime = (parse(RunTime)-parse(StrfTime2)).total_seconds()
    rangeTimes = int(float(SleepingTime))
    for i in range(rangeTimes):
        i=rangeTimes-i
        sys.stdout.write("将在{0}秒后运行\r".format(i))
        sys.stdout.flush()
        time.sleep(1)

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
    print (determine)
    if determine:
        FillIn()
    else:
        time.sleep(0.5)
        GetSource()

def DetermineAutoSubmit():
    xm = u'姓名'
    determine = xm in str
    print (determine)
    if determine:
        FillInATsubmit()
    else:
        GetSource()
        time.sleep(0.5)

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
    ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 69 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3 NetType/WIFI Language/zh_CN'
    profiel = webdriver.FirefoxProfile()
    profiel.set_preference('general.useragent.override', ua)
    parser = argparse.ArgumentParser(prog='python2.7 fuck_mikeCRM-2.py', description="FuckingMikeCRM!")
    parser.add_argument('-u', dest='url', help="目标麦克表单地址")
    parser.add_argument('-A',dest='auto',help="-A y 启用自动提交")
    parser.add_argument('-t',dest='time',help="程序启动时间,可以精确到秒哦.格式12:00或12:00:00")
    if len(sys.argv) <= 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    url = args.url
    autoSubmit = args.auto
    RunTime = args.time
    if '-u' in sys.argv:
        if (autoSubmit == 'y'):
            if '-t' in sys.argv:
                GetTime()
                bs = webdriver.Firefox(firefox_profile=profiel)
                bs.get(url)
                GetSourceAutoSubmit()
            else:
                bs = webdriver.Firefox(firefox_profile=profiel)
                bs.get(url)
                GetSourceAutoSubmit()
        else :
            if (autoSubmit == 'n'):
                if '-t' in sys.argv:
                    GetTime()
                    bs = webdriver.Firefox(firefox_profile=profiel)
                    bs.get(url)
                    GetSource()
                else:
                    bs = webdriver.Firefox(firefox_profile=profiel)
                    bs.get(url)
                    GetSource()
