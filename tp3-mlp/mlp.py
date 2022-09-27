from math import exp


class Perceptron:

    def __init__(self, w, data):  # weights => w
        self.e0 = 1
        self.data = data
        self.factor = 0.1
        self.w = w
    
    def run(self, e):   # entradas => e
        e = e.copy()
        e.insert(0, self.e0)
        z = 0
        for i in range(len(self.w)):
            z += (e[i] * self.w[i])
        valor_real = 1/(1+exp(-z))
        return valor_real

    def train(self, e):
        sr = self.run(e)
        sd = self.data[2]
        e = e.copy()
        e.insert(0, self.e0)
        error = sd - sr
        delta = sr * (1-sr) * error
        for i, v in enumerate(self.w):
            self.w[i] += self.factor * e[i] * delta
        return delta

    def train_oculto(self, e, delta):
        sr = self.run(e)
        e = e.copy()
        e.insert(0, self.e0)
        delta_oc = sr * (1-sr) * delta
        for i, v in enumerate(self.w):
            self.w[i] += self.factor * e[i] * delta_oc
        print(self.w)


if __name__ == '__main__':

    entradas1 = [0, 0, 0]

    # Capa de entrada    
    p0 = Perceptron([0.9, 0.7, 0.5], entradas1)
    p1 = Perceptron([0.3, -0.9, -1], entradas1)
    p2 = Perceptron([0.8, 0.35, 0.1], entradas1)

    # Capa de salida    
    p3 = Perceptron([-0.23, -0.79, 0.56, 0.6], entradas1)

    e0 = p0.run(entradas1)
    e1 = p1.run(entradas1)
    e2 = p2.run(entradas1) 

    entradas2 = [e0, e1, e2]
    print(entradas2)

    sr = p3.run(entradas2)
    print(sr)

    d = p3.train(entradas2)

    p0.train_oculto(entradas1, d)
    p1.train_oculto(entradas1, d)
    p2.train_oculto(entradas1, d)

    # p4 = Perceptron([0.6, -0.6, 0.22])
    # p5 = Perceptron([-0.22, -0.55, 0.31, -0.32])
    #e4 = p4.run(entradas2)
    #entradas3 = [e2, e3, e4]
    #sr = p5.run(entradas3)

