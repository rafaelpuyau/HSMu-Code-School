"""
Um condomínio realiza uma eleição para síndico anualmente. Para otimizar o
processo de votação e apuração, há a necessidade de criar um sistema de votação
digital. Para isso, você deve fazer um programa em que seja possível registrar
os votos e, em seguida, apresentar o resultado final.

A eleição pode ter entre uma e três chapas, sendo elas Azul, Vermelho e Amarelo,
cada uma com apenas um candidato. O condomínio possui 35 apartamentos e apenas
um morador de cada residência pode votar. O resultado deve exibir quantos votos
teve cada candidato, a quantidade de votos nulos e brancos e a porcentagem deles
sobre o total de votos.
"""

APTO = 35
votos = 0
votacao = {
    'Chapa_Azul': 0,
    'Chapa_Vermelho': 0,
    'Chapa_Amarelo': 0,
    'Brancos': 0,
    'Nulos': 0
    }

while votos < APTO:
    computar_voto = input('Seu voto [Azul | Vermelho | Amarelo]: ').lower()
    if computar_voto == 'azul':
        votacao['Chapa_Azul'] += 1
    elif computar_voto == 'vermelho':
        votacao['Chapa_Vermelho'] += 1
    elif computar_voto == 'amarelo':
        votacao['Chapa_Amarelo'] += 1
    elif computar_voto == '':
        votacao['Brancos'] += 1
    else:
        votacao['Nulos'] += 1
    votos += 1

print('RESUMO DA VOTAÇÃO')
print('-' * 18)
for candidato, votos in votacao.items():
    print(f'{candidato} : {votos} - ({votos/APTO*100:.2f}%)')
