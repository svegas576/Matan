a = {1,2,3,4,5}
b = {-2,-1,0,1,2}
c = {2/3, 5/6, 7/8, 3/4, -4/7}
print(a,b,c)
print(a.isdisjoint(b))      #имеют ли множества общие элементы
print(b.isdisjoint(c))
print (a.intersection(b))   #пересечение множеств a и b
print (b.intersection(a,c))  #пересечение множеств a,b,c
a.difference_update(b)      #вычитание
print(a)
print(a.difference(b,c))    #множество из всех элементов a, не принадлежащих ни одному из b,c
print(a.symmetric_difference(c))    #множество из элементов, встречающихся в a, но не встречающихся в c
a.update(b,c)                #объединение множеств a,b,c
print(a)
