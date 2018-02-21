def fl(lst):
     s = 0
     for i in lst:
         s += i
     return s / len(lst)

print(fl([1, 2, 3, 4]))     