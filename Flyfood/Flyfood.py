from itertools import permutations

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

    def caminhos(self):
        keys = self.__chaves
        dicionario = self.__pontos
        dronometros = {} # dicionário que vai ter como chave o valor em dronometro e valor como o caminho/permutação
        for c in permutations(keys):
            c = ('R',) + c + ('R',)
            v = 0
            for h in range(len(c) - 1):
                i, j = dicionario[c[h]]
                k, l = dicionario[c[h + 1]]
                g = abs(abs(i - k) + abs(j - l)) # distancia de manhattan
                v += g
            dronometros[v] = c
        s = list(dronometros.keys())
        f = min(s)
        menor_caminho = dronometros[f]

        return f, menor_caminho
            
arq = Matriz("arquivo.txt")
l = arq.get_line()
c = arq.get_collum()
lt = arq.lista_arquivo(l,c)
mt = arq.matriz(l,c,lt)
pop = mt.keys()
flyfood = Drone(mt,pop)
flyfood.lista_de_pontos()
val , cam = flyfood.caminhos()
print(f"O custo total do menor caminho foi de {val} dronometros e os pontos percorridos em sequência foram {cam}")




    


        