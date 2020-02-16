class Les():
    def __init__(self):
        self.vetor = [None, None, None, None, None]
        self.quant = 0

    def getQuant(self):
        return self.quant

    def estaCheia(self):
        if self.quant == 5:
            return True
        else:
            return False

    def estaVazia(self):
        return self.quant == 0
    
    def inserirFim(self,valor):
        if self.quant < 5:
            self.vetor[self.quant] = valor
            self.quant += 1
        else:
            print("A lista já esta cheia!")

    def inserirInicio(self,valor):
        i = self.quant
        while i > 0:
            self.vetor[i] = self.vetor[i-1]
            i -= 1
        self.vetor[0] = valor
        self.quant += 1

    def removerInicio(self):
        i = 0
        while i < self.quant-1:
            self.vetor[i] = self.vetor[i+1]
            i += 1
        self.quant -= 1

    def removerFim(self):
        self.quant-=1

    def getPrim(self):
        return self.vetor[0]

    def getUlt(self):
        return self.vetor[self.quant-1]

    def show(self):
        i = 0
        while i < self.quant:
            print(self.vetor[i])
            i+=1


    def inserirAposDet(self,valor1,valor2):
        i = 0
        while i < self.quant and self.vetor[i] != valor2:
            i += 1
        if i != self.quant:
            j = self.quant
            while j > i+1:
                self.vetor[j] = self.vetor[j-1]
                j -= 1
        self.vetor[j] = valor1 
        self.quant += 1
        
    def inserirAntesDet(self,valor1,valor2):
        i = 0
        while i < self.quant and self.vetor[i] != valor2:
            i += 1
        if i != self.quant:
            j = self.quant
            while j > i+1:
                self.vetor[j] = self.vetor[j-1]
                j -= 1
        self.vetor[j-1] = valor1
        self.quant += 1




























    

    
    
