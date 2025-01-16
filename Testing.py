import math

formula = "2*π*c*r/t"

a = 34.7420
vars = {
    'π':math.pi,
    'r': 6_370_000,
    't':86_400,
    'a':a,
    'c':math.cos(math.radians(a))
    
}

print(eval(formula,vars))