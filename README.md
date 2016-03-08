# ColorfulPyPrint
---
`version: 0.3.4`  
  
A sqlmap-style python colorful console output module, with verbose control,also able to print to qq/sms/SMTP/HTTP  
一个sqlmap风格的python控制台彩色输出模块  
支持verbose控制,自带一些外部输出模块(可以将输出内容发送为QQ消息/短信/SMTP邮件(尚未写好)/HTTP请求(尚未写好))  

Full function support python 3.x & 2.6 2.7 (you should handle unicode yourself in py2.x)  
support win linux Mac (Mac support in theory,did not tested yet)  
support PyCharm's console  
warnprint() doesn't work in powershell, it will print the normal white characters  

全部功能支持python 3.x 和 2.x (请自行处理py2.x的unicode问题)  
支持win linux Mac(Mac理论上支持,未测试)  
warnprint()不支持powershell  

Install
---
### English:  
 - 1. Copy the ColorfulPyPrint directory(I mean,the sub one with __init__.py) into YOUR_PYTHON_INSTALL_DIR/Lib/site-packages/  
 - 2. Can not use pip (for now)
    
### 中文:  
 - 1. 复制ColorfulPyPrint文件夹(项目里面带有__init__.py的子文件夹)到 你的Python安装目录/Lib/site-packages/  
 - 2. 不能使用pip来安装(自己写的小轮子嘛~)  

# Usage
---
Please execute(and see the source of) the demo for more detail  

### simple
```python
from ColorfulPyPrint import *
ColorfulPyPrint_set_verbose_level(3)  
infoprint('some info')  
dbgprint('some dbg') # default dbgprint will NOT show unless verbose level >=3  
warnprint('some warn') # default warnprint will NOT show unless verbose level >=2  
importantprint('some important notices') # with 1s beep  
```
  
### with custom verbose control:  
```python
from ColorfulPyPrint import *
ColorfulPyPrint_set_verbose_level(6)  
dbgprint('blah5', v=5) # will be printed
infoprint('blah6', v=6) # will be printed
dbgprint('blah7', v=7) # will NOT be printed
```  
 

# Extra output destinations
Program is able to send a copy of your output to any object with a .write() method  
That means you can send the output to file/QQ/email/sms/http and any destinations you want  
And more, you can choose to send only those critical outputs to extra destinations,
by given an important_level to an object, only those outputs reach the important_level limit will be sent,
please execute(and see the source of) the demo for more detail  

### 以QQ消息的形式发送
This module is for chinese users only, because QQ is an chinese local IM  
使用此模块需要手动架设一个WebQQ消息服务端(非常傻瓜化),请戳[WebQQ_API](https://github.com/Aploium/WebQQ_API)  
使用方法请看demo.py中webQQ client部分,大约从85行开始  
  
  
### 发送为短信(阿里大鱼短信接口)
This module is for chinese users only, because alidayu is an chinese local SMS provider  
使用此模块需要先在[阿里大鱼网站](http://www.alidayu.com)上注册成开发者(真是良心,个人开发者也可以用,短信模板的审核也很快)  
使用方法请看demo.py中alidayu sms sender部分,大约从108行开始  
本模块依赖requests包,请使用`pip install requests`或`pip3 install requests`安装requests  


# ScreenShot 
![image](https://raw.githubusercontent.com/Aploium/ColorfulPyPrint/master/demo.png)
