# -*- coding:utf-8 -*-
import argparse
import itertools
import random
import string


def gen_randstr():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return rand_str

def readfile(txt):
    txt_list = []
    with open(txt, 'r', encoding="utf-8") as f1:
        for line in f1.readlines():
            if line.startswith(u"\ufeff"):
                line = line.encode("utf8")[3:].decode("utf8")
            if '    ' in line or '\n' in line:
                line = line[:-1]
            txt_list.append(line)
    return txt_list

def genpass_sim(name_list,num_list,hchr_list,filename,pl=5):
    pass_list = []
    for name in name_list:
        for num in num_list:
            password = name + num
            if len(password) >= int(pl):
                pass_list.append(password)

    for name in name_list:
        for hchr1 in hchr_list:
            password = name + hchr1
            if len(password) >= int(pl):
                pass_list.append(password)
    output(filename,pass_list)
    #return pass_list

def genpass_com(name_list,num_list,qchr_list,hchr_list,filename,pl=5):
    pass_list = []
    # new_chr_list = list(itertools.permutations(chr_list, int(r)))
    for name in name_list:
        for num in num_list:
            for chr1 in hchr_list:
                # chr2 = ''.join(list(chr1))
                password = name + num + chr1
                if len(password) >= int(pl):
                    # print(password)
                    pass_list.append(password)
    for name in name_list:
        for chr2 in qchr_list:
            # chr2 = ''.join(list(chr1))
            for num in num_list:
                password = name + chr2 + num
                if len(password) >= int(pl):
                    # print(password)
                    pass_list.append(password)
    output(filename,pass_list)
    #return pass_list

def output(filename,pass_list):
    with open(filename,'a+',encoding='utf-8') as f:
        for password in pass_list:
            f.write(password+'\n')

def help():
    parser = argparse.ArgumentParser("密码由三部分组成，名、数字、特殊字符，巧妙的信息收集再组合，也许会有奇效\n")
    parser.add_argument('--simple', '-s', help='生成简单的密码，不包含特殊字符', action="store_true")
    parser.add_argument('--complex', '-c', help='生成复杂的密码，包含特殊字符', action="store_true")
    parser.add_argument('--fix', '-f', help='简单密码与复杂密码均存在', action="store_true")
    parser.add_argument('--namefile', '-nf', help='读取密码组成中名这部分的文件')
    parser.add_argument('--numfile', '-numf', help='读取密码组成中数字这部分的文件,可以同时输入多个,用英文逗号分割')
    parser.add_argument('--passlen', '-pl', help='生成密码的最小长度，默认为5')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    # 字符在后
    # hchr_list = ['@','?','_','#','$',',','!@#','#@!',',.','@,']
    hchr_list = readfile('dicts/hchr.txt')
    # 字符在前
    # qchr_list = ['@','_','#','?','','!@#','#@!']
    qchr_list = readfile('dicts/qchr.txt')
    num_list = []
    pass_list = []
    filename = 'password_'+gen_randstr()+'.txt'
    args = help()
    if args.namefile:
        name_list = readfile(args.namefile)
        name_list = list(set(name_list))
    else:
        name_list = readfile('dicts/common/common_name.txt')
        name_list = list(set(name_list))
    if args.numfile:
        if ',' in args.numfile:
            numfile = args.numfile.split(",")
            for file1 in numfile:
                num_list1 = readfile(file1)
                num_list.extend(num_list1)
            num_list = list(set(num_list))
        else:
            num_list = readfile(args.numfile)
            num_list = list(set(num_list))
    else:
        num_list = readfile('dicts/common/common_num.txt')
        num_list = list(set(num_list))

    # 指定密码长度的情况
    if args.passlen:
        # 简单密码
        if args.simple:
            pass_list = genpass_sim(name_list, num_list,hchr_list, filename, args.passlen)
        # 复杂密码
        if args.complex:
            pass_list = genpass_com(name_list, num_list, qchr_list,hchr_list,filename, args.passlen)
        # 混合密码
        if args.fix:
            pass_list1 = genpass_sim(name_list, num_list,hchr_list,filename, args.passlen)
            pass_list2 = genpass_com(name_list, num_list, qchr_list,hchr_list,filename, args.passlen)
    # 未指定密码长度的情况
    else:
        # 简单密码
        if args.simple:
            pass_list = genpass_sim(name_list, num_list,hchr_list,filename)
        # 复杂密码
        if args.complex:
            pass_list = genpass_com(name_list, num_list, qchr_list,hchr_list,filename)
        # 混合密码
        if args.fix:
            pass_list1 = genpass_sim(name_list, num_list,hchr_list,filename)
            pass_list2 = genpass_com(name_list, num_list, qchr_list,hchr_list,filename)
            #pass_list1.extend(pass_list2)
            #print('共生成5位密码：'+str(len(pass_list1))+'个')
            #for passs in pass_list1:
	           # print(passs)
