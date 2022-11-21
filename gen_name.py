# -*- coding:utf-8 -*-
import pypinyin

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


def genname(txt):
    name_list = readfile(txt)
    with open("gen_name.txt", 'a+') as file:
        file.truncate(0)
        for name in name_list:
            pinyin_list = pypinyin.lazy_pinyin(name)
            # 生成三种格式的拼音
            quanpin = ''.join(pinyin_list)
            fixpin = ''.join([pinyin_list[n] if n==0 else pinyin_list[n][0] for n in range(len(pinyin_list))])
            simpin = ''.join([pinyin_list[n][0] for n in range(len(pinyin_list))])
            # 首字母大写
            Bquanpin = quanpin.capitalize()
            Bfixpin = fixpin.capitalize()
            Bsimpin = simpin.capitalize()
            file.write(quanpin+'\n'+fixpin+'\n'+simpin+'\n'+Bquanpin+'\n'+Bfixpin+'\n'+Bsimpin+'\n')
            #print(quanpin+'\n'+fixpin+'\n'+simpin+'\n'+Bquanpin+'\n'+Bfixpin+'\n'+Bsimpin)

if __name__ == '__main__':
    genname('dicts/name.txt')

