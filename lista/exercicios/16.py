def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)
    return ranking


pontuacoes = [50, 100, 30, 80, 70]

ranking = criar_ranking(pontuacoes)

print(ranking)
criar_ranking(ranking)