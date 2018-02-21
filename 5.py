def solver(a,b,c):
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        Disc = "Discriminant: %s \n X1: %s \n X2: %s \n" % (D, x1, x2)      
    else:
        Disc = "Discriminant: %s \n  No reshenie" % D  
    return Disc

print(solver(5,5,9))    