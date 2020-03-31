class No():
    def __init__(self, anterior, valor, proximo):
        self.info = valor
        self.ant = anterior
        self.prox = proximo

class Ldde():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def getPrim(self):
        return self.prim.info

    def getUlt(self):
        return self.ult.info

    def getQuant(self):
        return self.quant

    def estaVazia(self):
        return self.quant == 0

    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end = "")
            aux = aux.prox
        
    def showRev(self):
        aux = self.ult
        while aux != None:
            print(aux.info, end = "")
            aux = aux.ant
    
    def remover(self, valor):
        aux = self.prim
        while aux != None:
            if aux.info == valor:
                if aux.ant == None:
                    aux = aux.prox
                    aux.prox.ant = None
                    self.prim = aux
                else:
                    aux.ant.prox = aux.prox
                    aux = aux.ant
            aux = aux.prox

            
    def inserirAposDet(self, valor1, valor2):
        aux = self.prim
        while aux != None and aux.info != valor2:
            aux = aux.prox
        if aux != None:
            aux.prox = No(aux, valor1, aux.prox)
            if aux == self.ult:
                self.ult = aux.prox
            self.quant += 1

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1


    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None

        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant -= 1


        
