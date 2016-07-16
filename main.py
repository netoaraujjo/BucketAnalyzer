#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MODO DE EXECUCAO
# python3 main.py numero de execucoes

from bucketsort import *
import sys

def main(num_repeticoes):

    tamanhos = [100, 500, 1000, 5000, 30000, 80000, 100000, 150000, 200000]
    # tamanhos = [10, 50, 100, 150, 200, 500]
    # tamanhos = [10, 20]

    bs = Bucketsort(num_repeticoes, tamanhos)

    bs.executa()


if __name__ == '__main__':
    num_repeticoes = int(sys.argv[1])
    main(num_repeticoes)
