#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��̵���
���ڣ�2020��11��24��
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=='ʯͷ':
        name=0
    elif name=='ʷ����':
        name=1
    elif name=='ֽ':
        name=2
    elif name=='����':
        name=3
    elif name=='����':
        name=4
    return name
    """����Ϸ�����Ӧ����ͬ������"""

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    pass #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
     #"""
    # ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
     #"""
   if number==0:
       number='ʯͷ'
   elif number==1:
       number='ʷ����'
   elif number==2:
       number='ֽ'
   elif number==3:
       number='����'
   elif number==4:
       number='����'
   return number
   # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
   # ��Ҫ���Ƿ��ؽ��

   # pass #��дִ�д���,������ɺ�passɾ��


def rpsls(c,a):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    #player_choice=(input("���������ѡ��"))

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    # player_choice_number=name_to_number(player_choice)
    # c=player_choice_number
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # a = random.randint(0,4)
    # comp_number=a
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    # b=number_to_name(comp_number)
    # ����Ļ����ʾ�����ѡ����������
    # print("�����ѡ��Ķ����ǣ�",b)
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    if  c==0 and a==(4 or 3):
        print("��Ӯ��")
    elif c==1 and a==(0 or 4):
        print("��Ӯ��")
    elif c==2 and a==(0 or 1):
        print("��Ӯ��")
    elif c==3 and a==(1 or 2):
        print("��Ӯ��")
    elif c==4 and a==(2 or 3):
        print("��Ӯ��")
    elif c == 0 and a == (2 or 1):
        print("�����Ӯ��")
    elif c == 1 and a == (2 or 3):
        print("�����Ӯ��")
    elif c == 2 and a == (4 or 3):
        print("�����Ӯ��")
    elif c == 3 and a == (4 or 0):
        print("�����Ӯ��")
    elif c == 4 and a == (0 or 1):
        print("�����Ӯ��")
    elif c == 2 and a == 3:
        print("�����Ӯ��")
    elif c == 2 and a == 0:
        print("��Ӯ��")
    elif c == 3 and a == 2:
        print("��Ӯ��")
    elif c == 0 and a == 2:
        print("�����Ӯ��")
    elif a == c:
        print("���ͼ��������һ����")
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

   # pass #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
player_choice = (input("���������ѡ��\n"))
print("----------------")
print("����ѡ���ǣ�",player_choice)
player_choice_number = name_to_number(player_choice)
c = player_choice_number
a = random.randint(0, 4)
comp_number = a
b = number_to_name(comp_number)
print("�����ѡ��Ķ����ǣ�",b)
rpsls(c,a)