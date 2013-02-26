import re

working=True
while(working):
    with open ('metro.txt') as baza:
        base=baza.read()
    with open ('metro2.txt') as baza:
        base1=baza.read()
    a=input("введите название станции, от которой отправляетесь: \n")
    a=a.lower()
    beg=base.find(a)
    while not base.count(a) and not base1.count(a):
        a=input("станция "+ a + " не найдена, введите другое значение: \n")
    b=input("введите название станции, до которой хотите добраться: \n")
    b=b.lower()
    while not base.count(b) and not base1.count(b):
        b=input("станция "+ b+ " не найдена, введите другое значение: \n")
    print("от"+24*" "+"|до"+23*" "+"|время")
    print(26*"-"+"+"+25*"-"+"+"+5*"-")
    c='технологический институт'
    if base.count(a) and base.count(b):
        beg=base.find(a)
        end=base.find(b)
        if(beg < end):
            marsh=base[beg+28:end+28]
        else:
            marsh=base[end+28:beg+28]
    elif base1.count(a) and base1.count(b):
        beg=base1.find(a)
        end=base1.find(b)
        if(beg < end):
            marsh=base1[beg+28:end+28]
        else:
            marsh=base1[end+28:beg+28]
    elif base.count(a)and base1.count(b):
        beg=base.find(a)
        end=base1.find(b)
        mid=base.find(c)
        mid1=base1.find(c)
        if(beg < mid) and (end < mid1):
            marsh=base[beg+28:mid+28]+base1[end+28:mid1+28]
        elif(beg > mid) and (end < mid1):
            marsh=base[mid+28:beg+28]+base1[end+28:mid1+28]    
        elif(beg > mid) and (end > mid1):
            marsh=base[beg+28:mid+28]+base1[mid1+28:end+28]
        else:
            marsh=base[mid+28:beg+28]+base1[mid1+28:end+28]
    else:
        beg=base1.find(a)
        end=base.find(b)
        mid=base1.find(c)
        mid1=base.find(c)
        if(beg < mid) and (end < mid1):
            marsh=base[beg+28:mid+28]+base1[end+28:mid1+28]
        elif(beg > mid) and (end < mid1):
            marsh=base[mid+28:beg+28]+base1[end+28:mid1+28]    
        elif(beg > mid) and (end > mid1):
            marsh=base[beg+28:mid+28]+base1[mid1+28:end+28]
        else:
            marsh=base[mid+28:beg+28]+base1[mid1+28:end+28]
        
        
    print(marsh)
    v=re.findall('(\d+)',marsh)        
    s=0
    for i in range (len(v)):
        s += int(v[i])
    print("примерное время в пути:  ",s, "мин.")
    p=input("ввести другие значения?(да/нет)")
    if p not in ("yes", "Y", "да", "Да"):
        working=False
 
