*******************
***** CODE *****
*******************
def cavalo(origem, destino):
  oL = origem // 8 + 1
  oC = origem % 8 +1
  dL = destino // 8 + 1
  dC = destino % 8 +1
  qtLinhas = abs(oL - dL)
  qtColunas = abs(oC - dC)
  mov1 = [(1,2),(2,1)]
  mov2 = [(0,2), (0,4), (1,3), (2,0), (2,4), (3,1), (3,3), (4,0), (4,2)]
  mov3 = [(0,1), (0,3), (0,5), (1,0), (1,4), (1,6), (2,3), (2,5), (3,0), (3, 2),
          (3,4), (3,6), (4,1), (4,3), (4,5), (5,0), (5,2), (5,4), (6,1), (6,3)]
  mov4 = [(0,6), (1,1), (1,5), (1,7), (2,2), (2,6), (3,5), (3,7), (4,4), (4,6),
          (5,1), (5,3), (5,5), (5,7), (6,0), (6,2), (6,4), (6,6), (7,1), (7,3), 
          (7,5)]
  mov5 = [(0,7), (2,7), (4,7), (5,6), (6,5), (6,7), (7,0), (7,2), (7,4), (7,6)]
  mov6 = [(7,7)]
  
  movimentos = 0
  mov = (qtLinhas, qtColunas)
  if (mov in mov1):
    movimentos = 1
  elif (mov in mov2):
    movimentos = 2
  elif (mov in mov3):
    movimentos = 3 
  elif (mov in mov4):
    movimentos = 4 
  elif (mov in mov5):
    movimentos = 5
  elif (mov in mov6):
    movimentos = 6 
  return movimentos

cavalo(0,1)
cavalo(19,36)
