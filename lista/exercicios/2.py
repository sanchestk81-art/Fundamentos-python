def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    return alunos


lista = ["Ana", "Carlos", "João"]

print(inserir_aluno(lista, "Maria", 1))

inserir_aluno(lista, "Maria", 2)