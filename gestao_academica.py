"""
Você foi convidado para criar um sistema de gestão acadêmica que deve calcular
as médias semestrais dos alunos.
Inicialmente, você deve estruturar um programa para ser experimentado em apenas
uma disciplina, como projeto piloto.

As notas de cada bimestre são compostas por três atividades avaliativas, com
pesos diferentes: prova (peso 5), projeto (3) e lista de exercícios (2).
Os alunos são considerados aprovados, caso obtenham média semestral superior ou
igual a 8.
Caso obtenham notas entre 7.9 e 5, devem realizar a Avaliação Final (AF) e os
alunos com médias abaixo de 5, são considerados reprovados.

Desenvolva um código que ao fim da execução do programa, devem ser exibidas a
média geral da turma, a menor e a maior nota. Assim como a quantidade de alunos
que foram aprovados, reprovados e que necessitarão realizar AF.

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe
o link desse projeto no campo ao lado para que outros desenvolvedores possam
analisá-lo.

Observação: Existem diversas formas de determinar a maior e a menor média. Uma
delas é utilizando um conceito que será estudado mais à frente neste curso,
chamado vetores. Mas você pode utilizá-lo para a solução desta atividade.
"""

from colorama import Fore


class Turma:
    def __init__(self, turma, medias):
        self.turma = turma
        self.medias = medias

    @staticmethod
    def historico(medias, aluno, grau):
        medias[aluno] = grau
        return f'{medias}'

    @staticmethod
    def status(turma, aluno, status):
        turma[aluno] = status
        return f'{turma}'

    def media_geral(self, medias):
        media = 0
        for g in medias.values():
            media += g
        return f'{media/len(medias):.2f}'

    @staticmethod
    def maior_menor(medias):
        lista_grau = []
        for grau in medias.values():
            lista_grau.append(grau)
        maior = max(lista_grau)
        menor = min(lista_grau)
        return f'Maior média: {maior} | Menor média: {menor}'

    @staticmethod
    def status_alunos(turma):
        ap = rp = af = 0
        for status in turma.values():
            if status == 'APROVADO(A)':
                ap += 1
            elif status == 'REPROVADO(A)':
                rp += 1
            else:
                af += 1
        return f'Alunos aprovados : {ap} | Alunos em avaliação final : {af} | Alunos reprovados : {rp}'


class Aluno:
    def __init__(self, nome, prova, projeto, lista):
        self.__nome = nome
        self.prova = prova
        self.projeto = projeto
        self.lista = lista

    def nome(self):
        return self.__nome

    def media_aluno(self, prova, projeto, lista):
        media = ((prova * 5) + (projeto * 3) + (lista * 2)) / 10
        return f'{media:.2f}'

    def status_aluno(self, media):
        if media >= 8:
            return f'APROVADO(A)'
        elif 5.9 <= media <= 7.9:
            return f'EM AVALIAÇÃO FINAL'
        else:
            return f'REPROVADO(A)'


t1 = Turma({}, {})

while True:

    resp = input('Cadastrar aluno? [S/N] ')
    if resp[0] in 'Ss':
        a1 = Aluno(input('Qual o nome do aluno(a): ').title(), float(input('Nota da prova: ')),
                   float(input('Nota do projeto: ')), float(input('Nota da lista de exercícios: ')))
        a1.nome()
        mediaaluno = a1.media_aluno(a1.prova, a1.projeto, a1.lista)

        print(
            Fore.YELLOW + f'A média do aluno(a) {a1.nome()} foi {mediaaluno} e está {a1.status_aluno(float(mediaaluno))}' + Fore.RESET)

        t1.historico(t1.medias, a1.nome(), float(mediaaluno))
        t1.status(t1.turma, a1.nome(), a1.status_aluno(float(mediaaluno)))
    else:
        break

print(f'Média geral da turma : {t1.media_geral(t1.medias)}')
print(f'{t1.status_alunos(t1.turma)}')
print(f'{t1.maior_menor(t1.medias)}')
