# -*- coding: UTF-8 -*-
from __future__ import unicode_literals  # this demo.py is write in python3 style
# demo version 0.3.4

# Full function support python 3.x & 2.x
# support win linux Mac (Mac support in theory,did not tested yet)
# DO NOT support powershell
# How to install:
#     1. Copy the ColorfulPyPrint directory into YOUR_PYTHON_INSTALL_DIR/Lib/site-packages/
#     2. from ColorfulPyPrint import *
# Usage: please execute this demo

# 全部功能支持python 3.x 和 2.x (py2.x请自行处理unicode问题)
# 支持win linux Mac(Mac理论上支持,未测试)
# 不支持powershell
# 安装方法为复制ApOutput文件夹到 你的Python安装目录/Lib/site-packages/
# 并在项目中添加 from ColorfulPyPrint import * (详见下方demo)

# 外部输出模块:
# WebqqClient 发送消息到QQ号或者讨论组
# AlidayuSMS 通过阿里大鱼的短信接口发送短信到手机

# import
from ColorfulPyPrint import *

# print version number
from ColorfulPyPrint import __version__  # print version (do NOT add this line in your actual project)

infoprint('version:', __version__)

# sqlmap-style output

infoprint('some information')
infoprint('显然支持中文(Chinese support)')
infoprint(['support non', b'str', 'type', ('actually,you can print anything', {'key': 'value'})])

# (v0.1.8+) Multi paras support,very useful in some places
example_array = ['a', 'b', 'c', 'd', 'e']
infoprint('the length of array:', example_array, 'is', len(example_array))
errprint('some error')

# importantprint will play a beep by default
importantprint('some important info with beep(default)')
# manually set is_beep=False to disable the beep
importantprint('some important info WITHOUT beep,use is_beep=False to close beep', is_beep=False)
# for the other functions, beep is disabled by default, use is_beep=True to enable it


# verbose level is set to 1 by default, warnprint and dbgprint would NOT be print
infoprint('--- current verbose:', apoutput_current_verbose_level())
infoprint('you CANNOT see the warnprint(level3) and dbgprint(level3) here')
warnprint('This line would NOT be print by default')  # default verbose level for warnprint is 2
dbgprint('This line would NOT be print by default')  # default verbose level for dbgprint is 3

# use apoutput_set_verbose_level(new_level) to change verbose level
# well, such long function name can avoid conflict
apoutput_set_verbose_level(2)
# use apoutput_current_verbose_level() to get current verbose level
infoprint('--- changing verbose level to', apoutput_current_verbose_level())
warnprint('great! now you can see me')  # 2 == 2
infoprint('you CANNOT see the dbgprint(level3) here')
dbgprint('This line is still invisible in level 2')
apoutput_set_verbose_level(3)
infoprint('--- changing verbose level to', apoutput_current_verbose_level())
dbgprint('level 3 you can see dbgprint')

# you can custom some output's verbose level using v=[any integer number]
infoprint('--- current verbose:', apoutput_current_verbose_level())
infoprint('you CANNOT see an custom verbose6 infoprint here')
infoprint('an verbose level 6 output(CAN NOT SEE in verbose level 3)', v=6)
apoutput_set_verbose_level(6)
infoprint('--- changing verbose level to', apoutput_current_verbose_level())
infoprint('an verbose level 6 output', v=6)

# output with date
infoprint('some information, output with date', timelevel=2)
# output without timestamp
warnprint('some warning, output without timestamp', timelevel=0)

# ###################################################
# Now, you can provide an custom object to act as extra output destination(s)
# the only requirement is an '.write()' method, eg: obj.write(something)

# print to external destination:
# ####### webQQ client ########
# please see https://github.com/Aploium/WebQQ_API for more information
from ColorfulPyPrint.extra_output_destination.webqq_client import WebqqClient

warnprint('the following demo requires an self-hosted webQQ msg sender server,please see '
          'https://github.com/Aploium/WebQQ_API '
          'for more information')
server = 'qcloud.aploium.com'
target = 'Xno0Pu7bnCB'
token = 'apl'
try:
    q_client = WebqqClient(server, token=token, target=target)
    q_client.send_to_discuss('webqq_init')
    add_extra_output_destination(q_client, important_level=2)
    importantprint('an important msg that will be sent to your qq')
    errprint('an error msg that will be sent to your qq')
    infoprint('an info msg that will [NOT] be sent to your qq')
    infoprint('(manual configure important level to 3) an info msg that will be sent to your qq', i=3)
except Exception as e:
    clean_extra_output_destination()  # reset the extra output settings
    errprint('Unable to connect to the webqq server:', e)
clean_extra_output_destination()

# ######### alidayu sms sender #########
# please see http://www.alidayu.com for more information
from ColorfulPyPrint.extra_output_destination.aliyun_sms import AlidayuSMS
import json  # json is required to convert json-str to json-object

demo_app_key = input('Please input your app_key: ')
demo_app_secret = input('Please input your app_secret: ')
demo_rec_num = input('Please input your cell phone number:  ')
demo_partner_id = input('Please input your partner_id (optional),press enter to keep blank: ')
demo_sms_free_sign_name = input('Please input your sign, eg. 身份验证: ')
demo_sms_template_code = input('Please input the template code, eg. SMS_5376067: ')
demo_sms_default_param = json.loads(input('Please input the params format, in json: '))
demo_sms_default_msg_key = input('Please input the default key containing sms content: ')

sms = AlidayuSMS(demo_app_key, demo_app_secret,
                 default_rec_num=demo_rec_num,
                 default_sms_free_sign_name=demo_sms_free_sign_name,
                 default_sms_template_code=demo_sms_template_code,
                 default_partner_id=demo_partner_id
                 )
sms.set_default_sms_param(demo_sms_default_param, demo_sms_default_msg_key)

add_extra_output_destination(sms, important_level=2)
importantprint('an important msg that will be sent to your phone')
clean_extra_output_destination()
