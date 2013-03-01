import re

working=True
while(working):
    with open ('metro.txt') as baza:
        base=baza.read()
    with open ('metro2.txt') as baza:
        base1=baza.read()
    try:
        a=input("введите название станции, от которой отправляетесь: \n")
        a=a.lower()
        beg=base.find(a)
        i=0
        #проверка на существование станции в одной из двух строк при условии, что
        #значение не пустое
        while not base.count(a) and not base1.count(a) or len(a)<6:
            a=input("станция "+ a + " не найдена, введите другое значение: \n")
            i+=1
            if i==3:
                raise ValueError
        b=input("введите название станции, до которой хотите добраться: \n")
        b=b.lower()
        while not base.count(b) and not base1.count(b) or len(b)<6:
            b=input("станция "+ b+ " не найдена, введите другое значение: \n")
            i+=1                                         #условие для ограничения попыток ввода
            if i==3:
                raise ValueError
        print("от"+24*" "+"|до"+23*" "+"|время")
        print(26*"-"+"+"+25*"-"+"+"+5*"-")
        c='технологический институт'
        '''много условий, для того, чтобы определить маршрут через технологический институт,
        если станции находятся на разных ветках'''
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
                marsh=base[mid+28:beg+28]+base1[mid1+28:end+28]
            else:
                marsh=base[mid+28:beg+28]+base1[mid1+28:end+28]
        else:
            beg=base1.find(a)
            end=base.find(b)
            mid=base1.find(c)
            mid1=base.find(c)
            if(beg < mid) and (end < mid1):
                marsh=base1[beg+28:mid+28]+base[end+28:mid1+28]
            elif(beg > mid) and (end < mid1):
                marsh=base1[mid+28:beg+28]+base[end+28:mid1+28]    
            elif(beg > mid) and (end > mid1):
                marsh=base1[mid+28:beg+28]+base[mid1+28:end+28]
            else:
                marsh=base1[mid+28:beg+28]+base[mid1+28:end+28]
            
            
        print(marsh)
        v=re.findall('(\d+)',marsh)        
        s=0
        for i in range (len(v)):
            s += int(v[i])
        print("примерное время в пути:  ",s, "мин.")
        p=input("ввести другие значения?(да/нет): \n")
    except ValueError:   #обработка исключения, есл
        
        p=input("Вы 4 раза ввели неверное значение, хотите ли вы продолжить работу программы?(да/нет):\n")
    if p not in ("yes", "Y", "да", "Да"):
        working=False
 
