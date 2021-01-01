"""
Implemente um sistema para uma empresa de eventos. Cada evento deve ter um nome,
um responsável, as datas de início e fim, uma carga horária e lista de
palestras.

Os dados mínimos esperados para o responsável são nome completo, telefone para
contato e valor por hora, mas, se for necessário, é possível incluir outras
informações. Cada palestra deve ter um título, horário de início, palestrante,
uma descrição e carga horária. Por fim, um palestrante terá o seu nome, contato
e valor de uma hora de sua palestra.

O sistema deve fornecer:
1. o valor gasto com o responsável;
2. o valor total dos gastos com as palestras;
3. o valor total gasto por palestra;
4. os dados do palestrante com o maior e menor valor gasto em sua palestra.
"""
# Importação da biblioteca colorama para deixar algumas saídas coloridas como o que o sistema irá fornecer
from colorama import Fore


# Classe Evento que tratará das saídas do programa
class Evento:

    dados_palestrante = {}
    dados_maiormenor = {}
    valores = list()
    lista_dados_palestrantes = []
    lista_palestras = []  # recebo a lista de palestras
    total_palestras = 0

    def __init__(self, nome, data_inicio, data_fim, carga_horaria):
        self.__nome = nome
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__carga_horaria = carga_horaria

    def __str__(self):
        return self.__nome

    def responsavel(self, nome_completo, telefone, valor_hora):
        self.__nome_completo = nome_completo
        self.__telefone = telefone
        self.__valor_hora = valor_hora

    def formata_moeda(self, moeda):
        converte = str(moeda).replace('.', ',')
        return f'R${converte}'

    def valor_gasto_responsavel(self):
        return f'O valor gasto com {self.__nome_completo} foi de ' \
               f'{self.formata_moeda(self.__carga_horaria * self.__valor_hora)}'

    def palestra(self, titulo, horario_inicio, descricao, carga_horaria):
        dados_palestra = {'Título': titulo, 'Horário': horario_inicio, 'Descrição': descricao,
                          'Carga Horária': carga_horaria}
        self.__class__.lista_palestras.append(dados_palestra)

        return dados_palestra

    def gastos_palestras(self):
        return Fore.LIGHTGREEN_EX + self.formata_moeda(f'{self.total_palestras:.2f}') + Fore.RESET

    def gastos_por_palestras(self):
        for lp in Evento.lista_palestras:
            print(f"{lp['Título']} ({evento.dados_palestrante['Nome']}) : "
                  f"{evento.formata_moeda(lp['Carga Horária'] * evento.dados_palestrante['Valor_hora'])}")
            self.total_palestras += lp['Carga Horária'] * evento.dados_palestrante['Valor_hora']
        for dp in self.dados_palestrante['Palestras']:
            self.valores.append(self.dados_palestrante['Valor_hora'] * dp['Carga Horária'])
        self.dados_maiormenor = {
            'Nome': self.dados_palestrante['Nome'],
            'Contato': self.dados_palestrante['Contato'],
            'Valor Hora': self.formata_moeda(self.dados_palestrante['Valor_hora']),
            'Maior Valor': self.formata_moeda(max(self.valores)),
            'Menor Valor': self.formata_moeda(min(self.valores))
        }
        self.lista_dados_palestrantes.append(self.dados_maiormenor)
        self.valores.clear()
        self.lista_palestras.clear()

    def palestrante(self, nome_palestrante, contato, valor_hora_palestrante, *sobre_palestra):
        self.dados_palestrante = {
            'Nome': nome_palestrante,
            'Contato': contato,
            'Valor_hora': valor_hora_palestrante,
            'Palestras': sobre_palestra
        }

        return f"{self.dados_palestrante['Nome']} | {self.dados_palestrante['Contato']} | " \
               f"{self.formata_moeda(self.dados_palestrante['Valor_hora'])}" \
               f"\nValor da palestra do(a) {self.dados_palestrante['Nome']} : " \
               f"" \
               f"{self.formata_moeda(self.dados_palestrante['Valor_hora'] * self.dados_palestrante['Palestras'][0]['Carga Horária'])}"

    def dados_palestrante_maiormenor(self):
        for dp in range(len(self.lista_dados_palestrantes)):
            print(f"Nome: {self.lista_dados_palestrantes[dp]['Nome']} | Contato: "
                  f"{self.lista_dados_palestrantes[dp]['Contato']} | "
            f"Valor Hora: {self.lista_dados_palestrantes[dp]['Valor Hora']} => Maior "
                  f"valor: {self.lista_dados_palestrantes[dp]['Maior Valor']} e " 
            f"Menor Valor: {self.lista_dados_palestrantes[dp]['Menor Valor']}")


    @classmethod
    def lista(cls):
        return cls.lista_palestras
# FIM DA DECLARAÇÃO DA CLASSE


# INÍCIO DO CÓDIGO
evento = Evento('Live Gastronomia - YouTube', '14/12/2020', '15/12/2020', 8)
print(Fore.LIGHTGREEN_EX + f'EVENTO : {evento.__str__()}' + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + '=-' * 30 + Fore.RESET)
print(Fore.YELLOW + '=> O valor gasto com o responsável;' + Fore.RESET)
evento.responsavel('Padmé Amidala', '24 99999.9999', 99.27)
print(evento.valor_gasto_responsavel())
print(Fore.YELLOW + '=> O valor total gasto por palestra;' + Fore.RESET)
pr1 = evento.palestra('Python Básico', '14:00', 'Primeiros passos', 4)
pr2 = evento.palestra('Python Avançado', '16:00', 'Para os já iniciados', 8)
pr3 = evento.palestra('Python & Flask', '18:00', 'Desenvolvimento Web', 6)
evento.palestrante('Anakin Skywalker', '24 11111.1111', 100.37, pr1, pr2, pr3)
# print(evento.dados_palestrante['Palestras'][1]['Carga Horária'])
evento.gastos_por_palestras()
pg1 = evento.palestra('Alimentação Saudável', '14:00', 'Primeiros passos', 6)
pg2 = evento.palestra('LGPD', '20:00', 'Por dentro da lei', 4)
evento.palestrante('Leia Organa', '21 22222.2222', 58.27, pg1, pg2)
evento.gastos_por_palestras()
pc1 = evento.palestra('Quibe de forno', '18:00', 'Receita Fácil e Rápida', 6)
pc2 = evento.palestra('Lombo Suíno', '10:00', 'Alternativa para a carne vermelha', 4)
evento.palestrante('Padmé Amidala', '21 33333.3333', 83.97, pc1, pc2)
evento.gastos_por_palestras()
print(Fore.YELLOW + '=> O valor total dos gastos com as palestras;' + Fore.RESET)
print(evento.gastos_palestras())
print(Fore.YELLOW + '=> Os dados do palestrante com o maior e menor valor gasto em sua palestra.' + Fore.RESET)
evento.dados_palestrante_maiormenor()
