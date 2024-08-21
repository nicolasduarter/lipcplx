import math
def suma(x,y):
    real = x[0] + y[0]
    imag = x[1] + y[1]
    return (real,imag)

def producto(x,y):
    real = ((x[0] * y[0]) - (x[1] * y[1]))
    imag = ((x[0] * y[1]) + (x[1] * y[0]))
    return (real,imag)

def resta(x,y):
    real = x[0] - y[0]
    imag = x[1] - y[1]
    return (real,imag)

def division(x,y):
    real = (((x[0] * y[0]) + (x[1] * y[1])) / (y[0] ** 2 + y[1] ** 2)) 
    imag = (((y[0] * x[1]) - (x[0] * y[1])) / (y[0] ** 2 + y[1] ** 2)) 
    return (real,imag)

def modulo(x):
    num = (((x[0]**2) + (x[1]** 2))** (1/2))
    return (num)

def conjugado(x):
    real = x[0]
    imag = -x[1]
    return (real,imag)

def polar_a_cartesiano(x):
    real = x[0] * math.cos(x[1])
    imag = x[0] * math.sin(x[1])
    return (real,imag)

def cartesiano_a_polar(x):
    mag = modulo(x)
    angu = fase(x)
    return (mag,angu)

def fase(x):
    num = math.atan(x[1]/x[0])
    return (num)
