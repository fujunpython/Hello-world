# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 13:32:49 2016

@author: chenjunfu
"""
###############python2.7适用

#frn记录数据域
frn = '9f4f21840f0c15736d00546e2f01598aaaff1377fb0ea4ff11fdf904d51e9101010080ff00e8010100e001ab00'
#规则1 注意0x不能丢
head1 = '0x'+frn[0:8]
c_head1 = bin(eval(head1))
c_head1 = c_head1[2:]
for i,item in enumerate(c_head1):
    if (((i+1)%8 == 0) and (int(item) == 0)):#注意一下int
        c_head1_index = i
        break
true_head = c_head1[:c_head1_index]
##规则2

count_list = []
for i,item in enumerate(true_head):
    
    if (int(item) == 1) and ((i+1)%8 != 0):
        count_list.append(str(i+1-(i+1)/8))
        
## dictionary_rule
#只做前几个规则
dict = {'r1':2 ,'r2':'not defined','r3':1,'r4':3,'r5':8,'r6':6,'r7':4}


    
def r1(str):
    data_source_identication = str
    print '数据源识别码:',str
    
def r3(str):
    time =int(str,16)
    time =float(time)/2**7
    print '运行时间:',time
    
def r5(str):
    str1 = str[:8]
    str2 = str[8:]
    if str1[0] != ('f'or'e'or'd'or'c'or'b'or'a'or'9'or'8'):
        lat = float(int(str1,16))*180/2**25
    else:
        Str1='0x' + str1
        lat = -float(((0xffffffff - eval(Str1) + 1))*180)/2**25
    if str2[0] != ('f'or'e'or'd'or'c'or'b'or'a'or'9'or'8'):
        lon = float(int(str2,16))*180/2**25
    else:
        Str2='0x' + str2
        
        lon = -float(((0xffffffff - eval(Str2) + 1)*180))/2**25
    print '正经度代表东经，正维度代表北纬'
    print '纬度',lat
    print '经度',lon
def r6(str):
    str1 = str[:6]
    str2 = str[6:]
    if str1[0] != ('f'or'e'or'd'or'c'or'b'or'a'or'9'or'8'):
        x = float(int(str1,16))/2
    else:
        Str1='0x' + str1
        x = -float((0xffffff - eval(Str1) + 1))/2
    if str2[0] != ('f'or'e'or'd'or'c'or'b'or'a'or'9'or'8'):
        y = float(int(str2,16))/4
    else:
        Str2='0x' + str2
        y = -float((0xffffff - eval(Str2) + 1))/2
    print 'X',x
    print 'Y',y
    
    
def r7(str):
    str1 = str[:4]
    str2 = str[4:]
    if str1[0] != ('f'or'e'or'd'or'c'or'b'or'a'or'9'or'8'):
        Vx = float(int(str1,16))/4
    else:
        Str1='0x' + str1
        Vx = -float((0xffff - eval(Str1) + 1))/4
    if str2[0] != ('f'or'e'or'd'or'c'or'b'or'a'or'9'or'8'):
        Vy = float(int(str2,16))/4
    else:
        Str2='0x' + str2
        Vy = -float((0xffff - eval(Str2) + 1))/4
    print 'VX',Vx
    print 'VY',Vy
count_list1 = count_list[:5]
search_dict = []
for c in count_list1:

    key ='r' + c
    search_dict.append(key)

list1 = [dict[x] for x in search_dict]
usable_frn = frn[8:]
#分段
rule_list = []
lenth = 0
for i in list1 :
    lenth = lenth + i
    rule_list.append(usable_frn[2*(lenth-i):2*(lenth)])


r1(rule_list[0])
r3(rule_list[1])
r5(rule_list[2])
r6(rule_list[3])
r7(rule_list[4])