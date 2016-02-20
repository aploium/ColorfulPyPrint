# ColorfulPyPrint
---
`version: 0.2.2`  
  
A sqlmap-style python colorful console output module, with verbose control  
一个sqlmap风格的python控制台彩色输出模块  
支持verbose控制  

Full function support python 3.x & 2.6 2.7  
support win linux Mac (Mac support in theory,did not tested yet)  
DO NOT support powershell  

全部功能支持python 3.x 2.6 2.7  
支持win linux Mac(Mac理论上支持,未测试)  
不支持powershell  
# Install
---
### English:  
 - 1. Copy the ColorfulPyPrint directory(I mean,the sub one with __init__.py) into YOUR_PYTHON_INSTALL_DIR/Lib/site-packages/  
 - 2. Can not use pip (for now)
    
### 中文:  
 - 1. 复制ColorfulPyPrint文件夹(项目里面带有__init__.py的子文件夹)到 你的Python安装目录/Lib/site-packages/  
 - 2. 不能使用pip来安装(自己写的小轮子嘛~)  

# Usage
---
Please execute(and see) the demo for more detail  

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
 

# ScreenShot 
![image](https://raw.githubusercontent.com/Aploium/ColorfulPyPrint/master/demo.png)