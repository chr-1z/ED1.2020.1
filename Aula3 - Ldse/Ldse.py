class No():
    def __init__(self,valor,proximo):
        self.info = valor
        self.prox = proximo

class Ldse():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def inserirInicio(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor,self.prim)
        self.quant += 1

    def inserirFim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            self.ult = aux
            self.ult.prox = None
        self.quant -= 1

    '''

    aux = ant = self.prim
    while aux != self.ult:
        ant = aux
        aux = aux.prox
    self.ult = ant
    self.ult.prox = None

    '''
               
    def show(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end = "")
            aux = aux.prox

    def estaVazia(self):
        return self.quant == 0

    def getPrim(self):
        return self.prim.info

    def getUlt(self):
        return self.ult.info

    

    

    
        
        
        
        
    
