print("Написать программу, которая принимает на вход целое число и выводит значение факториала этого числа.")
n = input("Факториал числа ") 
n = int(n) 
fac = 1 
i = 0 
while i < n:
     i += 1
     fac = fac * i 
print ("равен", fac)