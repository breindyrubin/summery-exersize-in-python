import numpy as numpyy


# 1
def sin_x(x):
    if x == 0:
        return 1
    else:
        return numpyy.sin(x) / x


# 2
def cos_x(x):
    if x == 0:
        return 1
    else:
        return numpyy.cos(x) / x


# 3
t = numpyy.arange(-100, 100, 0.01)

# 4
sinx = [sin_x(x) for x in t ]

#5
cosx = [cos_x(x) for x in t]

print(sin_x(99.98))
print(cos_x(0))
print(t)
print(sinx)
print(cosx)
