#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-
#import matplotlib
#matplotlib.use('Agg')

import numpy as np
import time
from pylab import *
import matplotlib.pyplot as plt
from random import randint
import sys

# bias w0 = 0
# pesos w[0] = 0 w[1] = 0

def plot_dados(dados, classes, nome, left, right, low, high):
#    print('low: ', low)
    j = 0
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title(nome, fontweight='bold', fontsize=12)
    ax.set_ylim(left, right)
    ax.set_xlim(low, high)
    arrow(left, 0, right - left, 0, length_includes_head=True, head_width=0.05)
    arrow(0, low, 0, high - low, length_includes_head=True, head_width=0.05)
    x_plot = np.array([])
    y_plot = np.array([])
    while j < dados.shape[0]:  # plota dados
        x_plot = np.append(x_plot, dados[j, 0])
        y_plot = np.append(y_plot, dados[j, 1])
        if classes[j] == 0:
            [plt.plot([x_plot[j]], [y_plot[j]], '*', markersize=15)]
        else:
            [plt.plot([x_plot[j], x_plot[j]], [y_plot[j], y_plot[j]], 'ro')]
        j += 1
    draw()

def calcula_xp1_yp2(w0, w):
# calcula p1 e p2
    print('w0: ', w0)
    print('w[0]', w[0])
    print('w[1]', w[1])

    if w[0] == 0: xp1 = w0*1.
    if w0 == 0 and w[0] > 0: xp1 = (1*1./w[0]*1.)
    if w0 == 0 and w[0] == 0: xp1 = 0
    if w0 == 0 and w[0] < 0: xp1 = (1*1./w[0]*1.)
    if w0 != 0 and w[0] != 0: xp1 = -(w0 *1./ w[0]*1.)

    if w[1] == 0: yp2 = w0*1.
    if w0 == 0 and w[1] > 0: yp2 = (1*1./w[1]*1.)
    if w0 == 0 and w[1] == 0: yp2 = 0
    if w0 == 0 and w[1] < 0: yp2 = (1*1./w[1]*1.)
    if w0 != 0 and w[1] != 0: yp2 = -(w0 *1./ w[1]*1.)

    print('xp1: ', xp1)
    print('yp2: ', yp2)
    return (xp1, yp2)


def plot_fronteira(xp1, yp2, left, right, low, high):
#    print('dados: ', dados)
    if xp1 != 0 and yp2 != 0:
        x_short = np.linspace(xp1, 0)
        y_short = np.linspace(0, yp2)
        x_ext = np.linspace(left, right, 100)
        p = np.polyfit(x_short, y_short , deg=1)
        y_ext = np.poly1d(p)(x_ext)
        try:
            plt.plot((x_ext),(y_ext), '-', linewidth=1, label=u'Fronteira de decisão')  # python2
        except:
            plt.plot((x_ext),(y_ext), '-', linewidth=1, label='Fronteira de decisão')  # python3
        plt.legend(loc='best', prop={'size': 6})
    elif xp1 == 0 and yp2 != 0:
        x_short = np.linspace(xp1, 0)
        y_short = np.linspace(0, yp2)
#        x_ext = np.linspace(left, right, 100)
#        p = np.polyfit(x_short, y_short, deg=1)
#        y_ext = np.poly1d(p)(x_ext)
        try:
            plt.plot((xp1,0), (low,high), '-', linewidth=1, label=u'Fronteira de decisão')  # python2
        except:
            plt.plot((xp1,0), (low,high), '-', linewidth=1, label='Fronteira de decisão')  # python3
        plt.legend(loc='best', prop={'size': 6})
    elif xp1 != 0 and yp2 == 0:
        x_short = np.linspace(xp1, 0)
        y_short = np.linspace(0, yp2)
        #        x_ext = np.linspace(left, right, 100)
#        p = np.polyfit(x_short, y_short, deg=1)
        #        y_ext = np.poly1d(p)(x_ext)
        try:
            plt.plot((left, right), (0, yp2), '-', linewidth=1, label=u'Fronteira de decisão')  # python2
        except:
            plt.plot((left, right), (0, yp2), '-', linewidth=1, label='Fronteira de decisão')  # python3
        plt.legend(loc='best', prop={'size': 6})
    elif xp1 == 0 and yp2 == 0:
        print('pontos 0')
        x_short = np.linspace(xp1, 0)
        y_short = np.linspace(0, yp2)
        #        x_ext = np.linspace(left, right, 100)
#        p = np.polyfit(x_short, y_short, deg=1)
        #        y_ext = np.poly1d(p)(x_ext)
        try:
            plt.plot((xp1,0), (low,high), '-', linewidth=1, label=u'Fronteira de decisão')  # python2
        except:
            plt.plot((xp1,0), (low,high), '-', linewidth=1, label='Fronteira de decisão')  # python3
        plt.legend(loc='best', prop={'size': 6})
    draw()


def processa_epoch(w0, w, dados, classes, epoch, nome, left, right, low, high):
    evento_erro = 1
    while evento_erro == 1 and epoch <= lim_epoch:
        i = 0
        print('-----------------------------------')
        print ('epoch: ', epoch)
        print('w0: ', w0)
        print('w: ', w)
        evento_erro = 0
        while i < dados.shape[0]:
            nome_l = nome + str(epoch) + ", interacao: " + str(i)
            print('-----------------------------------')
            print('epoch: ', epoch)
            print('interacao: ', i)
            print('dados[i]: ', dados[i])
#            print('classe: ', classes[i])
            print('w0:', w0)
            print('w: ', w)
#            print('w[0] * dados[i]: ', w * dados[i])
            valor = np.sum((w * dados[i])) + w0
            print('valor: ', valor)

# calcula hardlim
            if valor >= 0:
                y = 1
            else:
                y = 0
            print('classe escolhida: ',y)
            print ('classes[i] :',classes[i])

# calcula erro
            erro = classes[i] - y
            print('erro: ', erro)

# atualizar bias e pesos
            if erro != 0:
                evento_erro = 1
                w = w +(erro*dados[i]) #recalcula pesos
#                print('erro*dados[i]: ', erro*dados[i])
                w0 = w0 + erro # recalcula bias
                print('novo w0:', w0)
                print('novo w: ', w)

# plota dados com fronteria de decisão recalculados
                plot_dados(dados, classes, nome_l, left, right, low, high)
#                print('dados: ', dados)
                xp1, yp2 = calcula_xp1_yp2(w0, w)
                plot_fronteira(xp1, yp2, left, right, low, high)

            i += 1
            print('i: ', i)
        epoch += 1
    print (epoch)
    print (evento_erro)
    return (epoch, evento_erro, w0, w)



def main(lim_epoch, points, w0, w00, w11, left, right, low, high, dados):
    np.seterr(divide='ignore', invalid='ignore')
    plt.rcParams.update({'figure.max_open_warning': 0})
    w = np.array([0,0])
    w[0] = w00
    w[1] = w11
#    print(w)

# cria pontos aleatórios entre left e right
    i = 0
    while i < points:
        j = 0
        while j <= 1:
            dados[i, j] = int(randint(left, right))
            j += 1
        i += 1

# Dados para teste
#    dados = np.array([[1,-5],[3, 6],[-6,2],[-4,-3]])
#    dados = np.array([[4,-1],[-2,-6],[0,-3],[-2,3]])
#    dados = np.array([[-1,3],[2,-3],[0,-4],[2,1]])
#    dados = np.array([[0,4], [5,4], [3,3], [-1,0]])
#    dados = np.array([[1,0], [-4,-1], [0,-3], [-1,5]])
#    dados = np.array([[-1,3], [0,-3], [-3,1], [-1,-2]])
#    dados = np.array([[1,-1],[3,6],[4,3],[3,4]])
#    dados = np.array([[-5,2], [-4,-2], [-5,0], [3,4]])
#    dados = np.array([[5,5], [4,-1], [5,4], [4,-3]])
#    dados = np.array([[2,2], [-2,-2], [-2,2], [-1,1]])
#    dados = np.array([[5,4], [2,2], [-4,-4], [4,-1],[3,4],[-3,-1]])
#    dados = np.array([[2, 3], [-2, -3], [-2, 2], [-1, 1],[-1,2],[-2,1]])
#    dados = np.array([[5, 1], [-2, -3], [-6, -1], [-1, -6], [6, -2], [-4, -3]])
#    dados = np.array([[-1,2],[-5,1],[-2,6],[4,3],[0,5],[6,5]])
#    dados = np.array([[-6,-4],[-4,-5],[-1,-1],[5,-3],[-3,3],[5,4]])
#    print ('tamanho dados: ', dados.shape[0])
    print('dados: ', dados)

# plota dados
    try:
        nome = unicode("Dados: ")  # python2
    except:
        nome = "Dados: "  # python3
    left -= 1
    right += 1
    low -= 1
    high += 1
    plot_dados(dados, classes, nome, left, right, low, high)

######## processa epoch ################
    epoch = 1
    nome = "Fronteira Perceptron epoch: "
    epoch, evento_erro, w0, w = processa_epoch(w0, w, dados, classes, epoch, nome, left, right, low, high)

#####   Indica que a fronteira nao foi encontrada   #######
    if epoch == lim_epoch + 1: # and evento_erro != 0:
        ep = str(epoch - 1)
        try:
            ep.decode('utf-8')
        except:
            ep = ep
        try:
            nome = u"Fronteira Perceptron não encontrada em: " + ep + u" epoch " #python2
        except:
            nome = "Fronteira Perceptron não encontrada em: " + ep + " epoch "  # python3

        # plota dados com fronteria de decisão recalculados
        plot_dados(dados, classes, nome, left, right, low, high)
        p1, p2 = calcula_xp1_yp2(w0, w)
        plot_fronteira(p1, p2, left, right, low, high)

#    if epoch == lim_epoch + 1: # and evento_erro == 0:
#        ep = str(epoch - 1)
#        try:
#            ep.decode('utf-8')
#        except:
#            ep = ep
#        try:
#            nome = u"Fronteira Perceptron não encontrada em: " + ep + u" epoch " #python2
#        except:
#            nome = "Fronteira Perceptron não encontrada em: " + ep + " epoch "  # python3

#        epoch, evento_erro, w0, w = processa_epoch(w0, w, dados, classes, epoch, nome, left, right, low, high)
#        plot_dados(dados, classes, nome, left, right, low, high)
#        p1, p2 = calcula_xp1_yp2(w0, w)
#        plot_fronteira(p1, p2, left, right, low, high)

    show()


if __name__ == '__main__':
    left = (-6)  # limite esquerdo do grafico e inferior para pontos aleatorios
    right = (6)  # limite direito do grafico e superior para pontos aleatorios
    low = (-6)  # limite acima do grafico
    high = (6)  # limite abaixo do grafico

    if len(sys.argv) == 6:
        lim_epoch = int(sys.argv[1])
        points = int(sys.argv[2])
        dados = np.empty([points, 2])
        sys.setrecursionlimit(10 * lim_epoch * points + 1)

        # Cria vetor de classes
        classes = [] * points
        i = 1
        while i <= points:
            if (i % 2 == 0):
                classes.append(0)  # par
            else:
                classes.append(1)
            i += 1
        print(classes)
        main(lim_epoch, points, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), left, right, low, high, dados)

    else:
        print("Para plotar os dados favor comentar as linhas 3 e 4 de perceptron.py")
        print( "Use: python perceptron.py <limite_de_epocas, numero_de_pontos, bias, peso_1, peso_2>")
        print("Executando default: <limite_de_epocas = 30, numero_de_pontos = 4, bias = 0, peso_1 = 0, peso_2 = 0>")

        try:
            input = raw_input("digite N para interromper: ") # python2
        except:
            input = input("digite N para interromper: ") # python3
        if input == 'n' or input == 'N':
            sys.exit()
        else:

            lim_epoch = int(30)
            points = int(4)
            dados = np.empty([points, 2])
            sys.setrecursionlimit(10 * lim_epoch * points + 1)
            # Cria vetor de classes
            classes = [] * points
            i = 1
            while i <= points:
                if (i % 2 == 0):
                    classes.append(0)  # par
                else:
                    classes.append(1)
                i += 1
            print(classes)

            main(lim_epoch, points, 0, 0, 0, left, right, low, high, dados)