def trocar_cidade(texto):
    texto_trocado = texto.replace('Java', 'Python')

    return texto_trocado
cidade = 'Eu estudo Java'
print(trocar_cidade(cidade))