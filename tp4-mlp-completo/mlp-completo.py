from math import exp
import matplotlib.pyplot as plot


class Perceptron:

    def __init__(self, w):  # weights => w
        self.factor = 0.5
        self.w = w
        self.errores = []
        self.hist_w = []

    def run(self, entradas):   # entradas => e
        z = 0
        for i in range(len(self.w)):
            z += (entradas[i] * self.w[i])
        valor_real = 1/(1+exp(-z))
        return valor_real

    def train_salida(self, entradas, sr, sd):
        error = sd - sr
        self.errores.append(error)
        delta = sr * (1-sr) * error
        for i, v in enumerate(self.w):
            self.w[i] += self.factor * entradas[i] * delta
        return delta

    def train_oculto(self, entradas, delta, sr):
        delta_oc = sr * (1-sr) * delta
        for i, v in enumerate(self.w):
            self.w[i] += self.factor * entradas[i] * delta_oc

class MLP:

    def __init__(self, n, w, datos):
        perceptrones = [Perceptron(w[i]) for i in range(n)]
        self.capa_salida = perceptrones.pop()
        self.capa_oculta = perceptrones
        self.datos = [[1] + i for i in datos]

    def train(self, iteraciones):

        for i in range(iteraciones):   
            for entrada in self.datos:
                salida_oc = [1]

                # Inicia el MLP para obtener la salida real de la red
                for p in self.capa_oculta:
                    salida_oc.append(p.run(entrada))
                sr = self.capa_salida.run(salida_oc)

            # Comienza back propagation
                # Entrenamiento de la capa de salida
                delta = self.capa_salida.train_salida(salida_oc, sr, entrada[len(entrada)-1])

                #Entrenamiento de la capa oculta
                count = 1 # Contador para iterar sobre la lista de Salidas Reales ocultas
                for p in self.capa_oculta:
                    p.train_oculto(entrada, delta, salida_oc[count])
                    count += 1
        
        # Grafico de errores
        for x in range(len(self.datos)):
            err = []
            for i in range(x, len(self.capa_salida.errores), len(self.datos)):
                err.append(self.capa_salida.errores[i])
            plot.plot(range(iteraciones), err, label=f"e{x}")
        plot.legend()
        plot.show()
                
        # Grafico de pesos
        for x in range(len(self.datos)):
            err = []
            for i in range(x, len(self.capa_salida.errores),4):
                err.append(self.capa_salida.errores[i])
            plot.plot(range(iteraciones), err, label=f"e{i}")
        plot.show()

    def run(self):
        for entrada in self.datos:
            salida_oc = [1]

            for p in self.capa_oculta:
                salida_oc.append(p.run(entrada))
            sr = self.capa_salida.run(salida_oc)
            print(f"{entrada[1]} {entrada[2]} => {sr}")

if __name__ == '__main__':

    #n_neuronas = int(input("Ingrese el numero de neuronas: ")) + 1

    pesos = [[0.9, 0.7, 0.5], [0.3, -0.9, -1], [0.8, 0.35, 0.1], [-0.23, -0.79, 0.56, 0.6]]

    entradas = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 0]]

    mlp = MLP(4, pesos, entradas)

    mlp.train(10000)

    mlp.run()









    # # Capa de entrada    
    # p0 = Perceptron([0.9, 0.7, 0.5], entradas1)
    # p1 = Perceptron([0.3, -0.9, -1], entradas1)
    # p2 = Perceptron([0.8, 0.35, 0.1], entradas1)

    # [[0.9, 0.7, 0.5], [0.3, -0.9, -1], [0.8, 0.35, 0.1], [-0.23, -0.79, 0.56, 0.6]]
    # # Capa de salida    

    # e0 = p0.run()
    # e1 = p1.run()
    # e2 = p2.run() 

    # entradas2 = [e0, e1, e2]
    
    # p3 = Perceptron([-0.23, -0.79, 0.56, 0.6], entradas2)
    
    # print(entradas2)

    # sr = p3.run()

    # print(f"Salida de la red: {sr}")

    # d = p3.train()
    # print(d)
    # p0.train_oculto(entradas1, d)
    # p1.train_oculto(entradas1, d)
    # p2.train_oculto(entradas1, d)


