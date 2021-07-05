import re

reg = '[A-F0-9a-f]{2}[-:]?[A-F0-9a-f]{2}[-:.]?[A-F0-9a-f]{2}[-:]?[A-F0-9a-f]{2}[-:.]?[A-F0-9a-f]{2}[-:]?[' \
      'A-F0-9a-f]{2}'
str = "3:130通用关于本机名称曹坤的 iPhone>软件版本14.6型号名称 iPhone 12型号号码 MGGU3CHJA序列号 " \
      "FFYDJ2PSODYL有限保修到期日期:2021/10/22>歌曲视频569照片7563应44:90:bb:3f:f6:b5用程序122总容量128GB可用容量48.37GB无线局域网地址44:90:bb:3f:f6:b5蓝牙440::32:92: "
print(type(re.findall(reg, str)))
mac = [i for i in re.findall(reg, str)]
print(mac)
