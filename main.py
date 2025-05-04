r"""
Autor: Heverton dos Santos Borges
Data: 04/05/2025
Descrição: Script para realizar operações em imagens, transformando-as em matrizes e retornando no formato PBM P1.

Como executar:
    crie um ambiente virtual (opcional):
        $ python -m venv venv

        ative o ambiente virtual:
            linux:
                $ source venv/bin/activate
            windows (powershell):
                $ venv\Scripts\Activate.ps1

    instale as dependências:
        $ pip install numpy pillow

    execute o código:
        $ python main.py {caminho para a imagem}

* A imagem de entrada deve estar no formato PBM.
* A saída sera na pasta "./output".
* O "$" não deve ser incluso nos comandos, seu propósito é apenas para indicar que a linha é um comando.
"""

import os
import sys

import numpy as np
from PIL import Image


def pegarCaminhoImagem():
    argv = sys.argv

    if len(argv) > 1:
        return argv[1]

    print("O caminho da imagem deve ser informado como parâmetro!")
    sys.exit()


def criarMatriz(caminhoImagem):
    if not os.path.exists(caminhoImagem):
        print("Imagem não encontrada!")
        sys.exit()

    if not caminhoImagem.endswith(".pbm"):
        print("Formato inválido, a imagem deve estar no formato PBM!")
        sys.exit()

    img = Image.open(caminhoImagem)

    return 1 - np.asarray(img, dtype=np.uint8)


def transporMatriz(matriz):
    matrizT = np.empty((matriz.shape[1], matriz.shape[0]), np.uint8)

    for i, linha in enumerate(matriz):
        for j, e in enumerate(linha):
            matrizT[j][i] = e

    return matrizT


def inverterOrdemLinhas(matriz):
    matrizIL = np.empty(matriz.shape, dtype=np.uint8)

    for i, linha in enumerate(matriz):
        matrizIL[(matriz.shape[0] - 1) - i] = linha

    return matrizIL


def inverterOrdemColunas(matriz):
    matrizIC = np.empty(matriz.shape, dtype=np.uint8)

    for i, linha in enumerate(matriz):
        for j, e in enumerate(linha):
            matrizIC[i][(matriz.shape[1] - 1) - j] = e

    return matrizIC


def inverterOrdemLinhasEColunas(matriz):
    return inverterOrdemColunas(inverterOrdemLinhas(matriz))


def salvarImagem(matriz, caminhoImagem):
    if not os.path.exists("output"):
        os.mkdir("output")

    matriz = matriz.astype(str)
    arquivoImg = open(f"output/{caminhoImagem}", "w")

    arquivoImg.write(f"P1\n{matriz.shape[1]} {matriz.shape[0]}\n")
    for linha in matriz:
        arquivoImg.write("".join(linha) + "\n")


caminhoImg = pegarCaminhoImagem()
matrizImg = criarMatriz(caminhoImg)
print("Matriz criada!")

matrizImgT = transporMatriz(matrizImg)

salvarImagem(inverterOrdemLinhas(matrizImgT), "img_1.pbm")
salvarImagem(inverterOrdemColunas(matrizImgT), "img_2.pbm")
salvarImagem(inverterOrdemLinhas(matrizImg), "img_3.pbm")
salvarImagem(inverterOrdemLinhasEColunas(matrizImg), "img_4.pbm")
salvarImagem(inverterOrdemColunas(matrizImg), "img_5.pbm")
salvarImagem(matrizImgT, "img_6.pbm")
salvarImagem(matrizImg, "img_7.pbm")
salvarImagem(inverterOrdemLinhasEColunas(matrizImgT), "img_8.pbm")

print("Imagens salvas na pasta output!")
