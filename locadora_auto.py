"""
Buscando incrementar o turismo no Brasil, uma locadora de automóveis precisa de
um sistema que a ajude com os aluguéis dos carros, proporcionando, de maneira
mais fácil, o cálculo do valor do aluguel. A locadora possui três categorias de
veículos disponíveis: Econômico, Sedan e SUV.

Estabeleça os valores das diárias para cada uma das categorias e não esqueça de
adicionar o valor do seguro por diária. Além disso, o aluguel do carro possui
uma taxa administrativa obrigatória, que custa R$ 75,00.

A locadora possui algumas promoções. Por exemplo, caso o cliente opte por sete
diárias ou mais, ele terá um desconto de 15% no valor da diária. Há também
alguns itens opcionais disponíveis para o cliente:

1. GPS - R$ 12,00 por dia
2. Bebê Conforto - R$ 15,00 por dia
3. Cadeira de bebê -  R$ 15,00 por dia
4. Assento de Elevação - R$ 12,00 por dia

Crie um sistema que se baseie em funções e possibilite a realização de todos os
cálculos necessários para alugar um carro. Ao final, você deve salvar todos os
dados em um arquivo .txt, apresentando todos os gastos envolvidos na locação do
carro. Por exemplo:

Tipo do Carro: SUV
5 Diárias                Total
5 x R$ 84,90          R$ 424,50
------------------------------------------
Seguro do Carro
5 x R$ 20,00          R$ 100,00
------------------------------------------
GPS -  5 x R$ 12,00          R$ 60,00
Assento  - 5 x R$ 12,00          R$ 60,00
------------------------------------------
Taxa Administrativa	R$ 75,00

Total do Aluguel                R$ 759,50
"""

TX_ADM = 75


def cabecalho():
    """
    Apresenta um cabeçalho simples
    :return: Não há retorno, somente imprime na saída padrão
    """
    print('LOCADORA DE AUTOMÓVEIS')
    print('======================')


def formata_dinheiro(dindin):
    """
    Realiza a formatação o dinheiro para o formato brasileiro com R$ e vírgula separando
    os centavos
    :param dindin: recebe o valor em notação float
    :return: retorna uma string com R$ e trocando o . por ,
    """
    dindin = '%.2f' % dindin
    return 'R$ ' + str(dindin).replace('.', ',')


def calcula_opcionais(opcional, diarias):
    """
    Faz o cálculo de cada opcional que for solicitado pelo cliente
    :param opcional: Opcional escolhido pelo cliente
    :param diarias: Número de diárias contratadas
    :return: retorna com os opcionais contratados dentro de um dicionário
    """
    op_contratados[opcional] = opcionais[opcional]


def divisao():
    """
    Imprime uma linha divisória
    :return: não há retorno. Somente a impressão na saída padrão
    """
    return '-' * 60 + '\n'


def gravar_arquivo(categoria, diarias, total_a, total_s, total):
    with open('aluguel.txt', 'w') as gravacao:
        gravacao.write('Tipo de Carro: ')
        gravacao.write(categoria + '\n')
        gravacao.write(str(diarias) + ' Diárias' + '\t\t\t\t\t' + 'Total' + '\n')
        gravacao.write(str(diarias) + ' x ' + formata_dinheiro(categorias[categoria]) + '\t\t\t\t' + str(total_a) +
                       '\n')
        gravacao.write(str(divisao()))
        gravacao.write('Seguro do Carro' + '\n')
        gravacao.write(str(diarias) + ' x ' + formata_dinheiro(seguro_veiculo[categoria]) + '\t\t\t\t' + str(total_s) +
                       '\n')
        gravacao.write(str(divisao()))
        for op, valor in op_contratados.items():
            gravacao.write(str(op) + ' - ' + str(diarias) + ' x R$ ' + formata_dinheiro(valor) + '\t\t' +
                           formata_dinheiro(diarias*valor) + '\n')
        gravacao.write(str(divisao()))
        gravacao.write('Taxa Administrativa ' + formata_dinheiro(TX_ADM))
        gravacao.write('\n\n')
        gravacao.write('Total do Aluguel' + '\t\t\t' + total)
        gravacao.close()


categorias = {
    'Econômico': 27.8,
    'Sedan': 55.2,
    'SUV': 84.9
}

seguro_veiculo = {
    'Econômico': 10,
    'Sedan': 15,
    'SUV': 20
}

opcionais = {
    'GPS': 12,
    'Bebê Conforto': 15,
    'Cadeira de bebê': 15,
    'Assento de Elevação': 12
}

op_contratados = {}

cabecalho()

print('Informe a categoria deseja alugar um carro? ')

for chave in categorias.keys():
    print(f'- {chave}')

diaria = input('Escolha: ')
qtde_diarias = int(input('Quantas diárias? '))
total_aluguel = qtde_diarias * categorias[diaria]
seguro = qtde_diarias * seguro_veiculo[diaria]

op = input('Você deseja opcionais? [S/N]: ')

if op[0] in 'Ss':
    while True:
        for chave in opcionais.keys():
            print(f'- {chave}')
        extra = input()
        calcula_opcionais(extra, qtde_diarias)
        continua = input('Deseja adicionar outro opcional? [S/N] ')
        if continua in 'Nn':
            break

total_geral = total_aluguel + seguro + TX_ADM
for o in op_contratados.values():
    total_geral += o * qtde_diarias

gravar_arquivo(diaria, qtde_diarias, formata_dinheiro(total_aluguel), formata_dinheiro(seguro),
               formata_dinheiro(total_geral))
