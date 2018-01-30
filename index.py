height = float(input("Введите ваш рост: "))
weight = float(input("Введите ваш вес: "))
print("Выберите ваш пол","1.М или 2.Ж")

ind = weight / heigt**2
pol = int(input())
if pol ==1:
if ind <16:
	print("Дрыщ")
elif 16 < ind < 18.5:
    print("Почти норм")
elif ind < 18.5 and ind > 25:
	print("Терпимо")
elif ind >26 or ind !=60:
	print("Пончик")
else:
	print("Неоределено")