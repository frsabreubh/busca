import classe as M
import carga_matrix as Arq

 
linha = len(Arq.Matrix)
coluna = len(Arq.Matrix[0])

g = M.GraphoMatrix(linha, coluna, Arq.Matrix)

qtd_rios = g.conta_rios()

print('.'*10) 
print('\n Projeto 3:') 
if qtd_rios > 0:
    print(f"\t A matriz possui {qtd_rios} grande(s) grupo(s) de rio(s) composto(s) por {g.lista} rio(s) menor(es).\n\n")
else:
     print(f"\t A matriz não possui nenhum rio.\n\n")
print('.'*10) 
