print("Имя первого друга :")
name1 = input()

print("Имя второго друга :")
name2 = input()

print("Имя третьего друга :")
name3 = input()

if (len(name1)) > (len(name2)) > (len(name3)):
  print("У друга с именем " + name1 + " имя длиннее")

if (len(name2)) > (len(name1)) > (len(name3)):
  print("У друга с именем " + name2 + " имя длиннее")

if (len(name3)) > (len(name2)) > (len(name1)):
  print("У друга с именем " + name3 + " имя длиннее")
