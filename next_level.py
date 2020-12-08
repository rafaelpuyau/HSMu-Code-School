"""
A Next Level, uma moderna e conceituada universidade, necessita de um sistema
de gestão acadêmico.

Para o projeto piloto de implantação do sistema, você deve criar um programa
que permita calcular a média semestral dos alunos.

A média semestral é a média aritmética simples das médias bimestrais.
As médias bimestrais são compostas pelas seguintes atividades: prova (peso 3),
projeto (peso 3), lista de exercícios (2) e contribuição em projetos de
software livre/ conclusão de MOOCs recomendados pelo docente (3).

Os dados devem ser obtidos a partir de input pelo teclado e o programa deve
exibir se o aluno foi aprovado ou reprovado. Considere que o aluno deve ser
aprovado se obtiver nota igual ou maior que 8.

Caso o aluno tenha média menor que 8, determine também a nota mínima necessária
para a pontuação na prova final, de forma que o aluno garanta aprovação na
disciplina. Para tal, basta subtrair do valor 10,00 o valor da média.
"""


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    @staticmethod
    def situacao_aluno(media):
        if media >= 8:
            return f'APROVADO'
        else:
            return f'REPROVADO'

    @staticmethod
    def media_semestral(prova, projeto, lista_exercicios, contrib):
        semestre = ((prova * 3) + (projeto * 3) + (lista_exercicios * 2) + (contrib * 3)) / 11
        return f'{semestre:.2f}'


a1 = Aluno(input('Nome do aluno: '))
notas = [float(input('Nota da prova: ')), float(input('Nota do projeto: ')),
         float(input('Nota da lista de exercícios: ')), float(input('Nota da contribuição em projetos: '))]

n = float(a1.media_semestral(notas[0], notas[1], notas[2], notas[3]))

print(f'O aluno {a1.nome} foi {a1.situacao_aluno(n)} com média {n:.2f}')
