print("""Вам 20 лет и вы - трудоголик.
 Вы работаете M (<16) часов в день.
  Каждый месяц нагрузка на работе увеличивается, и вам приходиться работать на 5 минут в день больше. 
  Как только рабочий день вырастит до 18 часов - вы умрете от переутомления. """)
print('Если вы работаете 16 часов и больше с каждым годом \
	ваша смерть приближается')
age=240
a=int(input('Сколько часов в день вы работаете'))
a=a*60
while a<1080:
	age+=1
	a+=5
	if a>=1080:
		print("Вы умерли в возрасте", age/12, "Лет")

	

	#i=int(input("Введите ваши часы работы: "))
	#pp=int(((18-i)*(12*5))/60) 
	#print(pp,"лет вам осталось жить")