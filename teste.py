from recomendacao import avaliacoes
from math import sqrt

def euclidiana(usuario1, usuario2):
    si ={}
    for item in avaliacoes[usuario1]:
        if item in avaliacoes[usuario2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    soma = sum(pow(avaliacoes[usuario1][item] - avaliacoes[usuario2][item], 2)
               for item in avaliacoes[usuario1] if item in avaliacoes[usuario2])

    return 1 / (1 + sqrt(soma))




def getSimilares(target):
    similares = []
    for usuario in avaliacoes:
        if usuario != target:
            similares.append({euclidiana(target, usuario), usuario})

    similares.sort()
    similares.reverse()
    return similares

def getSimilaresIf(target, limit):
    similares = [(euclidiana(target, outro), outro) for outro in avaliacoes if outro != target and euclidiana(target, outro) > limit]

    similares.sort()
    similares.reverse()
    return similares
        
