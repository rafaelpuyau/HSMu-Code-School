"""
No Brasil, a multa por excesso de velocidade pode ser enquadrada em três
categorias: média, grave e gravíssima. Os valores são definidos de acordo
com o percentual em que o motorista excede o limite da via. Por exemplo, se
o motorista é flagrado a 48 km/h em uma via que a velocidade máxima permitida
é de 40 km/h, ele ultrapassou o limite em 20%.

Os valores e as categorias são:
1. até 20% acima do limite permitido na via, infração média. Valor: R$ 130,16;
2. de 21% até 50% acima do limite permitido na via, infração grave. Valor:
R$ 195,23;
3. a partir de 51% acima do limite permitido na via, infração gravíssima.
Valor: R$ 880,41.

Para ajudar os agentes de trânsito em sua fiscalização de rotina, crie um
programa para preparar a infração por excesso de velocidade. Considere que o
programa deve receber, pelo menos, o número da placa do veículo, a velocidade
analisada e o limite de velocidade da via. Em seguida, retorne uma mensagem ao
agente informando os dados do veículo (placa), a categoria da infração e o
valor da multa aplicada.
"""

placa = input('Placa do veículo: ').upper()
limite_via = int(input('Limite da via: '))
velocidade = float(input('Velocidade aferida: '))

if velocidade > limite_via:
    calculo = ((velocidade / limite_via) - 1) * 100
    if calculo <= 20:
        print('INFRAÇÃO MÉDIA')
        print(placa)
        print('Multa aplicada de R$130,16')
    elif 21 <= calculo <= 50:
        print('INFRAÇÃO GRAVE')
        print(placa)
        print('Multa aplicada de R$195,23')
    else:
        print('INFRAÇÃO GRAVÍSSIMA')
        print(placa)
        print('Multa aplicada de R$880,41')
