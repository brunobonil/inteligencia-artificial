from math import exp
import random


class Perceptron:

    def __init__(self): 
        self.factor = 0.1
        self.e0 = 1
        self.w0 = random.uniform(-1, 1)
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)

    def train(self, datos):
        while True:
            errores = []
            for e in datos:
                z = (self.e0 * self.w0) + (e[0] * self.w1) + (e[1] * self.w2)
                valor_real = 1/(1+exp(-z))
                error = (e[2] - valor_real)
                errores.append(abs(error))
                self.w0 += (self.factor * error * self.e0)
                self.w1 += (self.factor * error * e[0])
                self.w2 += (self.factor * error * e[1])
            if max(errores) < 0.01:
                return
        
    
    def run(self, datos):
        for e in datos:
            z = (self.e0 * self.w0) + (e[0] * self.w1) + (e[1] * self.w2)
            valor_real = 1/(1+exp(-z))
            print(f"{e[0]} {e[1]} ==> {valor_real}")



if __name__ == '__main__':

    datos_OR = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    
    datos_AND = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]

    p = Perceptron()
    p.train(datos_OR)
    p.run(datos_OR)

    print('='*80)

    q = Perceptron()
    q.train(datos_AND)
    q.run(datos_AND)

