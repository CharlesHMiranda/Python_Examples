from datetime import date, time, datetime, timedelta

def trabalhando_com_data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=10, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

def criando_uma_data():
    data_criada = datetime(2010, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=10)
    print(nova_data)

if __name__ == '__main__':
    trabalhando_com_data()
    trabalhando_com_time()
    trabalhando_com_datetime()
    criando_uma_data()
