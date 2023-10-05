from base import memoria
from gerador import palavra

palavra.gerar_palavra(int(input('qnts palavras deseja gerar?\n')))
if input('visualizar palavras geradas? s/n\n') == 's':
    memoria.ler_palavras()
print('----------\n'
      + 'bye')
