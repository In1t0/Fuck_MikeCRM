# Fuck_MikeCRM  
**@JadeTwan**  
**1.1版本绕过了某些表单只能在微信里填写的限制，改进了文本框的定位方式。**  
想要活动章，但是手速不行？ 想参加活动，但是大部分名额被工作人员内定？ 现在只要是Powered by MikeCRM的表单，大部分都能被自动的填写啦！ 如果可以的话，请传播它！

**请先安装jieba和selenium**  
使用python2.7  
		**用法**   
  
python fuck_mike.py  
--Input your url:  
-->>输入表单地址  
//之后会打开firefox浏览器，然后进入表单页面。  
--继续运行请输入 1  //此处是为了让人有机会确认表单是否正常加载，以及处理一些未知情况。  
-->>1  
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
--++++++++++  
--+ !DONE! +  
--++++++++++  
  
//未添加自动提交功能，需要的同学请自行添加。  
