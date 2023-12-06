from itertools import permutations

import time

class Matriz:
    def __init__(self,file):
        self.__file = file
        self.__matriz = {}
        self.__coluna = None
        self.__linha = None
        self.__lista_do_arquivo = None
  
    def get_line(self):
        c = str(self.__file)
        f = open(c,"r")
        conteudo = f.read(1)
        f.close()
        conteudo = int(conteudo)
        self.__linha = conteudo
        return self.__linha #incluir a linha
    
    def get_collum(self):
        c = str(self.__file)
        f = open(c,"r")
        for i in range(3):
            conteudo = f.read(1)
        f.close()
        conteudo = int(conteudo)
        self.__coluna = conteudo
        return self.__coluna # incluir a coluna
    
    def matriz(self,linha,coluna,lista):
        m = self.__matriz 
        self.__linha = linha
        self.__coluna = coluna
        self.__lista_do_arquivo = lista
        v = 0
        for i in range(self.__linha): # fazer um dicionário com i,j simulando uma matriz
            for j in range(self.__coluna):
                if '0' == self.__lista_do_arquivo[v]: # aqui pegamos a lista e percorremos ela para achar os valores diferentes de 0
                    v += 1
                else:
                    m[self.__lista_do_arquivo[v]] = (i,j) # se não for 0 entra no dicionário a letra como chave e a posição (i,j) como o valor
                    v += 1
        return m #retorna o dicionário
    
    def lista_arquivo(self,linha,coluna):
        abrir_arquivo = str(self.__file) 
        f = open(abrir_arquivo,"r")
        conteudo = f.read()
        conteudo = conteudo.replace("\n"," ")
        conteudo =  conteudo.split()
        conteudo.remove(f"{linha}")
        conteudo.remove(f"{coluna}")
        self.__lista_do_arquivo = conteudo #aqui tratamos o \n e removemos os números de linhas e colunas. É criado uma lista com todos os elementos
        f.close()
        return conteudo

class Drone:
    def __init__(self,pontos,chaves):
        self.__pontos = pontos
        self.__chaves = chaves

    def lista_de_pontos(self):
        a = []
        for c in self.__chaves:
            if c == 'R':
                pass
            else:
                a.append(c)
        self.__chaves = a
        return self.__chaves #Retorna as uma tupla das chaves sem o R

    def vizinho_mais_proximo(self):
        m = self.__pontos
        pontos = list(m.keys())
        pontos.remove('R')  # Remove o ponto inicial 'R'
        caminho = ['R']  # Começa com o ponto inicial 'R'
        ponto_atual = 'R'

        while pontos:
            menor_distancia = float('inf')
            proximo_ponto = None

            for ponto in pontos:
                i, j = m[ponto_atual]
                k, l = m[ponto]
                distancia = abs(i - k) + abs(j - l)  # Distância de Manhattan

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    proximo_ponto = ponto

            caminho.append(proximo_ponto)
            ponto_atual = proximo_ponto
            pontos.remove(proximo_ponto)

        caminho.append('R')  # Volta ao ponto inicial 'R'
        distancia_total = 0
        for i in range(len(caminho) - 1):
            ponto_atual = caminho[i]
            proximo_ponto = caminho[i + 1]
            i, j = m[ponto_atual]
            k, l = m[proximo_ponto]
            distancia_total += abs(i - k) + abs(j - l)

        return distancia_total, caminho

inicio = time.time()            
arq = Matriz("arquivo.txt")
l = arq.get_line()
c = arq.get_collum()
lt = arq.lista_arquivo(l,c)
mt = arq.matriz(l,c,lt)
pop = mt.keys()
flyfood = Drone(mt,pop)
flyfood.lista_de_pontos()
val , cam = flyfood.vizinho_mais_proximo()
print(f"dronometros {val}, pontos em sequência :{cam}")
fim = time.time()
final = fim - inicio
print(f"{final:.10f}")