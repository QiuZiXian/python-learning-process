# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'QiuZiXian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2020/9/1  16:39
# @abstract    :	scheduler.shutdown(wait=False)

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import pandas as pd
my_sender='1467288927@qq.com'    # 发件人邮箱账号
my_pass = 'bnrvxpcephbhhdig'              # 发件人邮箱密码(QQ邮箱授权码)
my_user='我自己@qq.com,我自己8@163.com'      # 收件人邮箱账号，我这边发送给自己

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.xxoo.com">这是一个链接</a></p>
"""

a=pd.DataFrame({'数列1':(12,12,12,12),'数列2':(32,32,32,32),'数列3':(43,43,43,43),'数列4':(54,54,54,54)})
a.index={'行1','行2','行3','行4'} #这里dataframe类型a就是要输出的表格
sub="test"
d='' #表格内容
for i in range(len(a)):
    d=d+"""
    <tr>
      <td>""" + str(a.index[i]) + """</td>
      <td>""" + str(a.iloc[i][0]) + """</td>
      <td width="60" align="center">""" + str(a.iloc[i][1]) + """</td>
      <td width="75">""" + str(a.iloc[i][2]) + """</td>
      <td width="80">""" + str(a.iloc[i][3]) + """</td>
    </tr>"""
html = """\
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>

<body>
<div id="container">
<p><strong>测试程序邮件发送:</strong></p>
<div id="content">
 <table width="30%" border="2" bordercolor="black" cellspacing="0" cellpadding="0">
<tr>
  <td width="40"><strong>统计</strong></td>
  <td width="50"><strong>数列1</strong></td>
  <td width="60" align="center"><strong>数列2</strong></td>
  <td width="50"><strong>数列3</strong></td>
  <td width="80"><strong>数列4</strong></td>
</tr>"""+d+"""
</table>
</div>
</div>
</div>
</body>
</html>
      """
def mail():
    ret=True
    try:
        msg=MIMEText(html,'html','utf-8')#'plain'为文本,'html为网页
        msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        #msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To']=my_user
        msg['Subject']="菜鸟教程发送邮件测试"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,['42608897@qq.com', 'ljxy925@126.com'],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号(list列表)、发送邮件正文
        server.quit()  # 关闭连接

    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False

    return ret
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")


# # 比如你的数据是
# arr = [
#     {"name":"aaa", "age":14, "qq":"77756576"},
#     {"name":"bbb", "age":17, "qq":"75653356"},
#     {"name":"ccc", "age":19, "qq":"46665655"}
# ]
## 构建表头
# head = arr[0].keys()
# table = '<tr>\n'
# for v in head:
#     table += f'<th>{v}</th>\n'
## 表格正文内容
# table += '</tr>\n'
# for li in arr:
#     table += '<tr>\n'
#     for v in li.values():
#         table += f'<td>{v}</td>\n'
#     table += '</tr>\n'
#
# html = f'''
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8" />
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
#     <title> 页面名称 </title>
# </head>
# <body>
#     <table border="1" style="border-collapse: collapse;">
#         {table}
#     </table>
# </body>
# </html>
# '''
# print(html)