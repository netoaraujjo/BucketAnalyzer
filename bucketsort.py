#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
from copy import copy
import time
import matplotlib.pyplot as pyplot

class Bucketsort(object):
    """docstring for Quicksort"""
    def __init__(self, num_repeticoes, tamanhos):
        super(Bucketsort, self).__init__()
        self.num_repeticoes = num_repeticoes
        self.tamanhos = tamanhos

        self.INSERTION = 'insertion'
        self.MERGE  = 'merge'
        self.HEAP = 'heap'
        self.QUICK = 'quick'

        # Tempos de execucao de um tamanho especifico de arranjo
        self.tempos_de_execucao = {}
        self.tempos_de_execucao[self.INSERTION] = []
        self.tempos_de_execucao[self.MERGE]  = []
        self.tempos_de_execucao[self.HEAP]  = []
        self.tempos_de_execucao[self.QUICK]  = []

        # Tempo medio de execucao para cada tamanho de arranjo
        self.tempos_medios = {}
        self.tempos_medios[self.INSERTION] = []
        self.tempos_medios[self.MERGE]  = []
        self.tempos_medios[self.HEAP]  = []
        self.tempos_medios[self.QUICK]  = []


    def gera_arranjo(self, tamanho):
        """Inicializa os arranjos a serem ordenados."""

        # Configura o valor maximo do intervalo para o maior inteiro suportado
        # pela arquitetura do computador onde executa
        # maximo = sys.maxsize
        maximo = tamanho

        # Cria  arranjo de numeros aleatorios na quantidade especificada
        arranjo = random.sample(range(maximo), tamanho)

        return arranjo


    def executa(self):
        """"""
        for tamanho in self.tamanhos:
            print('\n#########################################################')
            print('Executando testes para arranjos de tamanho:', tamanho)
            print('#########################################################\n')
            for n in range(self.num_repeticoes):
                # Gera um novo arranjo
                arranjo_original = self.gera_arranjo(tamanho)

                # Faz uma copia do arranjo original
                arranjo = copy(arranjo_original)

                self.executa_ordenacao(copy(arranjo_original), self.INSERTION, tamanho)

                self.executa_ordenacao(copy(arranjo_original), self.MERGE, tamanho)

                self.executa_ordenacao(copy(arranjo_original), self.HEAP, tamanho)

                self.executa_ordenacao(copy(arranjo_original), self.QUICK, tamanho)

            self.calcula_tempo_medio()
            print('\n\n')

        self.plotar_grafico()


    def executa_ordenacao(self, arranjo, sub_algoritmo, tamanho):
        """"""
        print('Ordenacao por ', sub_algoritmo)
        # print(arranjo)

        tempo_inicial = 0.0
        tempo_final = 0.0

        if sub_algoritmo == self.INSERTION:
            # Obtem o tempo inicial
            tempo_inicial = time.time()

            buckets = [[] for x in range(10)]
            for i, x in enumerate(arranjo):
                buckets[int(x / (tamanho / len(buckets)))].append(x)
            out = []
            for buck in buckets:
                out += self.insertion_sort(buck)

            # Obtem o tempo final
            tempo_final = time.time()

        elif sub_algoritmo == self.MERGE:
            # Obtem o tempo inicial
            tempo_inicial = time.time()

            buckets = [[] for x in range(10)]
            for i, x in enumerate(arranjo):
                buckets[int(x / (tamanho / len(buckets)))].append(x)
            out = []
            for buck in buckets:
                out += self.merge_sort(buck)

            # Obtem o tempo final
            tempo_final = time.time()

        elif sub_algoritmo == self.HEAP:
            # Obtem o tempo inicial
            tempo_inicial = time.time()

            buckets = [[] for x in range(10)]
            for i, x in enumerate(arranjo):
                buckets[int(x / (tamanho / len(buckets)))].append(x)
            out = []
            for buck in buckets:
                out += self.heap_sort(buck)

            # Obtem o tempo final
            tempo_final = time.time()

        else:
            # Obtem o tempo inicial
            tempo_inicial = time.time()

            buckets = [[] for x in range(10)]
            for i, x in enumerate(arranjo):
                buckets[int(x / (tamanho / len(buckets)))].append(x)
            out = []
            for buck in buckets:
                out += self.quick_sort(buck)

            # Obtem o tempo final
            tempo_final = time.time()

        # Calcula o tempo de execucao, em milissegundos
        tempo_de_execucao = (tempo_final - tempo_inicial) * 1000

        self.tempos_de_execucao[sub_algoritmo].append(tempo_de_execucao)

        # print(arranjo)
        print('Tempo de execucao:', tempo_de_execucao, 'milissegundos')
        print()




    ######################
    # INSERTION
    ######################



    def insertion_sort(self, list):
        """
        A insertion sort algorithm implemetation.

        @param list: a list object.
        """

        for i in range(1, len(list)):
            key = list[i]
            j = i - 1
            while j >= 0 and list[j] > key:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = key

        return list


    ######################
    # QUICK
    ######################

    def partition(self, aList, first, last):
        """
        Creates two partitions in aList, with the elements at left end being lesses than the pivot, and the rigth end being bigger than the pivot.
        @param aList = list being partitioned
        @param first = an integer, first index of aList
        @param last = an integer, last index of aList
        returns the final value of first (elements lesser than pivot)
        """

        pivot = first + random.randrange(last - first + 1)
        self.swap(aList, pivot, last)

        for i in range(first, last):
            if aList[i] <= aList[last]:
                self.swap(aList, i, first)
                first += 1

        self.swap(aList, first, last)

        return first

    def swap(self, A, x, y):
        """
        Swaps two elements in A
        @param A = list object
        @param x,y = two indexes of A
        """

        A[x],A[y]=A[y],A[x]

    def quick_sort(self, aList):
        self._quicksort(aList, 0, len(aList) - 1)

        return aList

    def _quicksort(self, aList, first, last):
        """
        Perfoms the quicksort method
        @param aList = list being sorted
        @param first = an integer, first index of aList
        @param last = an integer, last index of aList
        """

        if first < last:
            pivot = self.partition(aList, first, last)
            self._quicksort(aList, first, pivot - 1)
            self._quicksort(aList, pivot + 1, last)


    ######################
    # MERGE
    ######################


    def merge(self, left, right):
        """
        Merge two lists into a ordered one.

        @param left: a list object.
        @param right: a list object.

        @return: a list object.
        """

        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


    def merge_sort(self, arranjo):
        """
        A merge sort algorithm implemetation.

        @param list: a list object.

        @return: a new ordered list.
        """

        if len(arranjo) < 2:
            return arranjo
        m = int(len(arranjo) / 2)

        return self.merge(self.merge_sort(arranjo[:m]), self.merge_sort(arranjo[m:]))



    ######################
    # HEAP
    ######################

    def siftdown(self, list, start, end):
        """
        Restore a heap.

        @param list: a list object.
        @param start: a integer, the start index of restoring.
        @param end: a integer, then end index of restoring.
        """

        root = start
        while True:
            child = root * 2 + 1

            if child > end:
                break

            if child + 1 <= end and list[child] < list[child + 1]:
                child += 1

            if list[root] < list[child]:
                list[root], list[child] = list[child], list[root]
                root = child
            else:
                break

    def heapify(self, list):
        """
        Transforms a list into a maximum heap.

        @param list: a list object.
        """

        for start in range(int((len(list) - 2) / 2), -1, -1):
            self.siftdown(list, start, len(list) - 1)

    def heap_sort(self, list):
        """
        A heap sort algorithm implemetation

        @param list: a list object.
        """

        self.heapify(list)

        for end in range(len(list) - 1, 0, -1):
            list[end], list[0] = list[0], list[end]
            self.siftdown(list, 0, end - 1)

        return list




    ######################
    ######################


    def calcula_tempo_medio(self):
        """"""
        media = sum(self.tempos_de_execucao[self.INSERTION]) / self.num_repeticoes
        self.tempos_medios[self.INSERTION].append(media)

        media = sum(self.tempos_de_execucao[self.MERGE]) / self.num_repeticoes
        self.tempos_medios[self.MERGE].append(media)

        media = sum(self.tempos_de_execucao[self.HEAP]) / self.num_repeticoes
        self.tempos_medios[self.HEAP].append(media)

        media = sum(self.tempos_de_execucao[self.QUICK]) / self.num_repeticoes
        self.tempos_medios[self.QUICK].append(media)

        print('Tempo medio insertion:', self.tempos_medios[self.INSERTION])
        print('Tempo medio merge:', self.tempos_medios[self.MERGE])
        print('Tempo medio heap:', self.tempos_medios[self.HEAP])
        print('Tempo medio quick:', self.tempos_medios[self.QUICK])

        self.tempos_de_execucao[self.INSERTION].clear()
        self.tempos_de_execucao[self.MERGE].clear()
        self.tempos_de_execucao[self.HEAP].clear()
        self.tempos_de_execucao[self.QUICK].clear()


    def plotar_grafico(self):
        """"""
        eixo_x = self.tamanhos
        eixo_insertion = self.tempos_medios[self.INSERTION]
        eixo_merge = self.tempos_medios[self.MERGE]
        eixo_heap = self.tempos_medios[self.HEAP]
        eixo_quick = self.tempos_medios[self.QUICK]

        pyplot.subplot(1, 1, 1)

        pyplot.xlabel('Tamanho do arranjo (Nº de elementos)')
        pyplot.ylabel('Tempo de execução (ms)')

        pyplot.xlim(min(self.tamanhos), max(self.tamanhos) + 100)

        pyplot.xticks(range(0, max(self.tamanhos) + 1, 25000))

        pyplot.title('Análise do sub-algoritmo de ordenação do Bucketsort')

        plot1 = pyplot.plot(eixo_x, eixo_merge, 'bs-', label = 'MergeSort', linewidth = 2.5)
        plot2 = pyplot.plot(eixo_x, eixo_heap, 'gd-', label = 'HeapSort', linewidth = 2.5)
        plot3 = pyplot.plot(eixo_x, eixo_quick, 'y*-', label = 'QuickSort', linewidth = 2.5)

        pyplot.legend(loc='upper left')

        pyplot.savefig('plot.png', bbox_inches = 'tight')

        plot4 = pyplot.plot(eixo_x, eixo_insertion, 'ro-', label = 'InsertionSort', linewidth = 2.5)

        pyplot.legend(loc='upper left')

        # pyplot_all.show()
        pyplot.savefig('plot_all.png', bbox_inches = 'tight')
