class GraphoMtx:
    
    def __init__(self, linha, coluna, matriz):
        self.linha      = linha
        self.coluna     = coluna
        self.matriz     = matriz
        self.lista      = []
        self.cont_busca = 0        
        
    
    def BuscaPorProfundidade(self, i, j):
        
        if i < 0 or i >= len(self.matriz) or j >= len(self.matriz[0]) or j < 0 or self.matriz[i][j] != 1:
            return
 
        self.matriz[i][j] = -1

        self.cont_busca += 1
                 
        self.BuscaPorProfundidade(i - 1, j)        
        self.BuscaPorProfundidade(i, j - 1)
        self.BuscaPorProfundidade(i, j + 1)        
        self.BuscaPorProfundidade(i + 1, j)
        

    def conta_rios(self):
        
        ct_rios = 0        
        for i in range(self.linha):
            for j in range(self.coluna):                        
                if self.matriz[i][j] == 1:                             
                    self.cont_busca = 0         
                    self.BuscaPorProfundidade(i, j)
                    self.lista.append(self.cont_busca)                    
                    ct_rios += 1         
        return ct_rios
