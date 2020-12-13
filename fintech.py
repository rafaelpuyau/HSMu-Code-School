"""
Em um processo seletivo para trainee em uma fintech, foi solicitada a criação
de um programa que permita calcular as médias dos valores de ações na bolsa ao
longo de um mês.

Nesse caso, considere que os meses têm 28 dias e quatro semanas.

O programa deve apresentar as médias semanais (a menor e maior) e mensal.
"""

media_valores = [[[], [], [], []]]
media_mensal = []
media_s = media_m = 0

for mes in range(1):
    for semana in range(4):
        for dia in range(7):
            media_valores[mes][semana].append(float(input(f'Valor da ação do mês[{mes+1}], semana[{semana+1}] e '
                                                        f'dia[{dia+1}]=> ')))

for mes in range(1):
    for semana in range(4):
        print(media_valores[mes][semana])
        print(f'A média da semana[{semana+1}] = {sum(media_valores[mes][semana])/len(media_valores[mes][semana]):.2f}')
        print(f'Maior valor da semana: {max(media_valores[mes][semana])} | '
              f'Menor valor da semana: {min(media_valores[mes][semana])}')
        media_m += sum(media_valores[mes][semana])
    print(f'A média do mês[{mes+1}] = {media_m/28:.2f}')
