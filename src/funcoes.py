import nltk
lista_normalizada = []

def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

def gera_lista_normalizada(lista_palavras):
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

def normalizacao(lista_palavras):
    # Converte a lista em set para eliminar as duplicidades e retorna o set convertido em list.
    return list(set(gera_lista_normalizada(lista_palavras)))

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def corretor(palavra, lista_palavras):
    palavras_geradas = gerador_palavras(palavra)
    gera_lista_normalizada(lista_palavras)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta

def probabilidade(palavra_gerada):
    frequencia = nltk.FreqDist(lista_normalizada)
    return frequencia[palavra_gerada]/len(lista_normalizada)