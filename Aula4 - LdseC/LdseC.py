class No():
    def __init__(self, valor = None, proximo = None):
        self.info = valor
        self.prox = proximo

class Ldsec():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.prox = self.prim
        else:
            self.prim = self.ult.prox = No(valor, self.prim)
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.prox = self.prim
        else:
            self.ult.prox = self.ult = No(valor, self.prim)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult.prox = self.prim = self.prim.prox
        self.quant -= 1

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None

        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            ult = aux
            ult.prox = self.prim
        self.quant -= 1

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(aux.info, end = "")
            aux = aux.prox

    def inserirAposDet(self, valor1, valor2):
        aux = self.prim
        while aux != None and aux.info != valor2:
            aux = aux.prox
        aux.prox = No(valor1, aux.prox)
        if aux == self.ult:
            self.ult = aux.prox
        self.quant += 1
        
            





























        

    
    
