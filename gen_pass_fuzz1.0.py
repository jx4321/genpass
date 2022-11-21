# -*- coding:utf-8 -*-
import argparse
import itertools
import random
import string

def gen_randstr():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    return rand_str


def genpass_sim(name_list,num_list,filename,pl=5):
    pass_list = []
    for name in name_list:
        for num in num_list:
            password = name + num
            if len(password) >= pl:
                pass_list.append(password)
    output(filename,pass_list)
    # return pass_list

def genpass_com(name_list,num_list,chr_list,filename,r=1,pl=5):
    pass_list = []
    new_chr_list = list(itertools.permutations(chr_list, r))
    for name in name_list:
        for num in num_list:
            for chr1 in new_chr_list:
                chr2 = ''.join(list(chr1))
                password = name + num + chr2
                if len(password) >= pl:
                    # print(password)
                    pass_list.append(password)
    for name in name_list:
        for chr1 in chr_list:
            chr2 = ''.join(list(chr1))
            for num in num_list:
                password = name + chr2 + num
                if len(password) >= pl:
                    # print(password)
                    pass_list.append(password)
    output(filename,pass_list)
    # return pass_list

def output(filename,pass_list):
    with open(filename,'a+',encoding='utf-8') as f:
        for password in pass_list:
            f.write(password+'\n')


def help():
    parser = argparse.ArgumentParser("\n")
    parser.add_argument('--simple', '-s', help='生成简单的密码，不包含特殊字符', action="store_true")
    parser.add_argument('--complex', '-c', help='生成复杂的密码，包含特殊字符', action="store_true")
    parser.add_argument('--fix', '-f', help='简单密码与复杂密码均存在', action="store_true")
    parser.add_argument('--num', '-n', help='生成复杂密码时，控制特殊字符的数量，默认为1，建议最大不超过3')
    parser.add_argument('--passlen', '-pl', help='生成密码的最小长度，默认为5')
    args = parser.parse_args()
    return args




if __name__ == '__main__':
    name_list = ['a','Aa','password','Password','P@ssw0rd']
    num_list = ['123','123456','01','001','02','002','888','666','999','000','1','2']
    chr_list = ['?','@','#','_','!','$',',','.']
    pass_list = []
    filename = 'password_'+gen_randstr()+'.txt'
    args = help()
    # 指定密码长度的情况
    if args.passlen:
        # 简单密码
        if args.simple:
            pass_list = genpass_sim(name_list, num_list, filename, args.passlen)
        # 指定生成复杂密码的情况
        if args.num:
            # 复杂密码
            if args.complex:
                pass_list = genpass_com(name_list, num_list, chr_list,filename, args.num, args.passlen)
            # 混合密码
            if args.fix:
                pass_list1 = genpass_sim(name_list, num_list,filename, args.passlen)
                pass_list2 = genpass_com(name_list, num_list, chr_list,filename, args.num, args.passlen)
                # pass_list = pass_list1.extend(pass_list2)
        # 未指定生成复杂密码
        else:
            # 复杂密码
            if args.complex:
                pass_list = genpass_com(name_list, num_list, chr_list,filename, r=1, pl=args.passlen)
            # 混合密码
            if args.fix:
                pass_list1 = genpass_sim(name_list, num_list,filename, args.passlen)
                pass_list2 = genpass_com(name_list, num_list, chr_list,filename, r=1, pl=args.passlen)
                # pass_list = pass_list1.extend(pass_list2)
    # 未指定密码长度的情况
    else:
        # 简单密码
        if args.simple:
            pass_list = genpass_sim(name_list, num_list,filename)
        # 指定生成复杂密码的情况
        if args.num:
            # 复杂密码
            if args.complex:
                pass_list = genpass_com(name_list, num_list, chr_list,filename, args.num,)
            # 混合密码
            if args.fix:
                pass_list1 = genpass_sim(name_list, num_list,filename)
                pass_list2 = genpass_com(name_list, num_list, chr_list,filename, args.num)
                # pass_list = pass_list1.extend(pass_list2)
        # 未指定生成复杂密码
        else:
            # 复杂密码
            if args.complex:
                pass_list = genpass_com(name_list, num_list, chr_list,filename, r=1)
            # 混合密码
            if args.fix:
                pass_list1 = genpass_sim(name_list, num_list,filename)
                pass_list2 = genpass_com(name_list, num_list, chr_list,filename, r=1)
                # pass_list = pass_list1.extend(pass_list2)