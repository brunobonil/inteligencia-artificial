import cv2
import numpy as np
import random
from math import exp
from tqdm import tqdm
import matplotlib.pyplot as plot


class Perceptron:

    def __init__(self, w):  # weights => w
        self.factor = 0.5
        self.w = w
        self.errores = []
        #self.hist_w = [[] for i in range(len(w))]

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

    def __init__(self, n, datos, w=None): # 7680
        self.w = [[random.uniform(-1, 1) for i in range(7681)] for x in range(n)]
        perceptrones = [Perceptron(self.w[i]) for i in range(n)]
        self.capa_salida = Perceptron([random.uniform(-1, 1) for i in range(n+1)])
        self.capa_oculta = perceptrones
        self.datos = [np.append(i, [1]) for i in datos]
        

    def train(self, iteraciones):
        for i in tqdm(range(iteraciones)):   
            for x, entrada in enumerate(self.datos):
                if x % 2 == 0:
                    entrada = np.append(entrada, [0])
                else:
                    entrada = np.append(entrada, [1])
                salida_oc = [1]

                # Inicia el MLP para obtener la salida real de la red
                for p in self.capa_oculta:
                    salida_oc.append(p.run(entrada))
                sr = self.capa_salida.run(salida_oc)

            # Comienza back propagation
                # Entrenamiento de la capa de salida
                delta = self.capa_salida.train_salida(salida_oc, sr, entrada[-1])

                #Entrenamiento de la capa oculta
                count = 1 # Contador para iterar sobre la lista de Salidas Reales ocultas
                for p in self.capa_oculta:
                    p.train_oculto(entrada, delta, salida_oc[count])
                    count += 1

            #print(f"Iteracion {i}")
        
        # Grafico de errores
        for x in range(len(self.datos)):
            err = []
            for i in range(x, len(self.capa_salida.errores), len(self.datos)):
                err.append(self.capa_salida.errores[i])
            plot.plot(range(iteraciones), err, label=f"e{x}")
        plot.legend()
        plot.show()

    def run(self):
        for entrada in self.datos:
            salida_oc = [1]

            for p in self.capa_oculta:
                salida_oc.append(p.run(entrada))
            sr = self.capa_salida.run(salida_oc)


if __name__ == '__main__':

    n_neuronas = int(input("Ingrese el numero de neuronas: "))

    n_iteraciones = int(input("Ingrese numero de iteraciones: "))

    letras = ['A', 'B']
    img_list = []
    for i in range(1, 6):
        for x in letras:
            img = cv2.imread(f'./bonil/{i}{x}59159.jpg', 0).flatten()/255 # sd = 0
            img_list.append(img)


    mlp = MLP(n_neuronas, img_list)


    mlp.train(n_iteraciones)
