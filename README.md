# 前言

依经验总结，密码一般由三部分组成：
名（人名、单位名、系统名等，通用的有a、Aa、password、Password、P@ssw0rd）
数字（常见的有123、123456、1、2、01、001、02、002、000）
字符（常见的拼接密码的字符有['?','@','#','_','!','$',',','.']，常见的位数是1-3位）

其中：
1.名有全称、全称/简称混合、全简称、首字符大小写等区分
2.数字和字符的位置位于第二位和第三位，两者位置可以交换，字符一般是1-3位
3.非复杂类型的密码，特殊字符可以没有，或者数字没有

依次规律，结合实战，有了此小工具。

# 使用说明

````
gen_name.py
用于生成密码中名称的脚本，在name.txt文件中写入收集到的中文汉字名，即可生成对应的拼音。生成的拼音有三种，全拼、首字全拼+后续简拼、全简拼的组合。
gen_pass_fine1.0.py
用于生成密码字典，指定密码复杂度的情况下，默认参数运行，会生成常见名+数字+组合好的特殊字符，并且密码长度不小于5位的密码字典，也可以指定相关参数生成其他密码字典
说明如下：
>python3 gen_pass_fine1.0.py -h
usage: 密码由三部分组成，名、数字、特殊字符，巧妙的信息收集再组合，也许会有奇效
 [-h] [--simple] [--complex] [--fix] [--namefile NAMEFILE]
                                             [--numfile NUMFILE] [--passlen PASSLEN]

optional arguments:
  -h, --help            show this help message and exit
  --simple, -s          生成简单的密码，不包含特殊字符
  --complex, -c         生成复杂的密码，包含特殊字符
  --fix, -f             简单密码与复杂密码均存在
  --namefile NAMEFILE, -nf NAMEFILE
                        读取密码组成中名这部分的文件
  --numfile NUMFILE, -numf NUMFILE
                        读取密码组成中数字这部分的文件,可以同时输入多个,用英文逗号分割
  --passlen PASSLEN, -pl PASSLEN
                        生成密码的最小长度，默认为5
  
 例如：
 指定其他名+其他数字，生成密码长度不低于6位，简单、复杂密码均有的密码字典
>python3 gen_pass_fine1.0.py -nf gen_name.txt -numf num_other.txt,num_year.txt -f -pl 6

dicts目录：
gen_name.txt 生成的名字典
hchr.txt 在密码组合中位于最后一位的特殊字符组合
name.txt 收集的中文汉字的名字典
num_year.txt 密码组合中年份数字字典
qchr.txt 在密码组合中位于中间位置的特殊字符组合

dicts/common目录：
默认的名、数字字典，不指定参数时会调用。
 
````

# 最后

密码组合、密码字典不是越多越好，在已知信息情况下，尽量精确最重要。