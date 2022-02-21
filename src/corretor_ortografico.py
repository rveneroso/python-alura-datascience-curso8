import nltk
import funcoes as fn
#nltk.download('punkt')

# Abre o arquivo no modo somente leitura e atribui o resultado à variável f
with open('../data/artigos.txt','r') as f:
    # Lê o arquivo f e atribui o conteúdo dele à variável artigos.
    artigos = f.read()
lista_palavras = nltk.tokenize.word_tokenize(artigos)
print(fn.corretor("lgica", lista_palavras))



