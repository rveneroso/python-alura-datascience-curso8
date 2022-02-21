def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    # Convert a lista em set para eliminar as duplicidades e retorna o set convertido em list.
    return list(set(lista_normalizada))

def gerador_palavras(palavra):
    lista = palavra
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((lista[:i],lista[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras