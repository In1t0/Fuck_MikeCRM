# Fuck_MikeCRM  
首先把源码里的 list2 基本信息XXXXXX改成自己的。  
**##请务必使用Linux系统，windows下的运行问题请自行解决##** <br> 
**@JadeTwan**  <br>
**1.1版本绕过了某些表单只能在微信里填写的限制，改进了文本框的定位方式。** <br>
**2.0版本优化了交互方式** <br>
想要活动章，但是手速不行？ 想参加活动，但是大部分名额被工作人员内定？ 现在只要是Powered by MikeCRM的表单，大部分都能被自动的填写啦！ 如果可以的话，请传播它！<br>

**请先安装jieba和selenium**  <br>
**将geckodriver复制或移动至/usr/bin下，并赋予运行权限。**<br>
使用python2.7  <br>
```bash
$ python fuck_mikeCRM-2.py 
usage: python2.7 fuck_mikeCRM-2.py [-h] [-u URL] [-A AUTO] [-t TIME]

FuckingMikeCRM!

optional arguments:
  -h, --help  show this help message and exit
  -u URL      目标麦克表单地址
  -A AUTO     -A y 启用自动提交
  -t TIME     程序启动时间,可以精确到秒哦.格式12:00或12:00:00
```
  
//之后会打开firefox浏览器，然后进入表单页面。  
--Building prefix dict from the default dictionary ...  
--Loading model from cache /tmp/jieba.cache  
--Loading model cost 0.109 seconds.  
--Prefix dict has been built succesfully.  
//这一段在调用jieba 对网页源码进行一次分词  
  
--姓名:XXXXXXX  
--性别:X  
--专业班级:XXXXX  
--学号:XXXXXXXX  
--联系方式:XXXXXXX  
--QQ:XXXXXXXX  
--辅导员:XXX  
  
