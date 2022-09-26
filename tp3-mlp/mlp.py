from math import exp
from pickle import EXT4


class Perceptron:

    def __init__(self, w):  # weights => w
        self.e0 = 1
        self.w = w
    
    def run(self, e):   # entradas => e
        e.copy()
        e.insert(0, self.e0)
        z = 0
        for i in range(len(self.w)):
            z += (e[i] * self.w[i])
        valor_real = 1/(1+exp(-z))
        return valor_real
        

if __name__ == '__main__':

    entradas1 = [0, 0]
    
    p0 = Perceptron([0.9, 0.7, 0.5])
    p1 = Perceptron([0.3, -0.9, -1])

    e0 = p0.run(entradas1.copy())
    e1 = p1.run(entradas1.copy())

    entradas2 = [e0, e1]

    p2 = Perceptron([0.8, 0.35, 0.1])
    p3 = Perceptron([-0.23, -0.79, 0.56])
    p4 = Perceptron([0.6, -0.6, 0.22])

    e2 = p2.run(entradas2.copy()) 
    e3 = p3.run(entradas2.copy())
    e4 = p4.run(entradas2.copy())

    p5 = Perceptron([-0.22, -0.55, 0.31, -0.32])

