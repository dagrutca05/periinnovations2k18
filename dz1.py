

print("Топ моих любимых фильмов")
films=["1+1","Зеленая миля","Игры разума","Властелин колец","Один дома","Хоббит","Доктор стрендж"]
print(films)
a = int(input("""Что хотите добавить в конец списка?: 
	1.добавить элемент в конец списка
	2.в любой участок списка
	3.удаление элемента из списка
	4.вывод целиком списка
	5.создание копиии списка"""))
if a=="1":
	print(films.append(input()))
	print(films)
elif a=="2":
	element=int(input())
	print(films.insert(element,input()))
elif a=="3":
	print(films.remove(input()))

elif a=="5":
	print(films.copy(input()))
	print(films)
elif a=="4":
	print(films.revers(input()))
a = 1 
while a > 0:
	print(films)