import datetime

data = datetime.datetime.now()
print('A data completa é:')
print(data)

dia = data.day
mês = data.month
ano = data.year
hora = data.hour
min = data.minute
segundos = data.second

print ('Estamos no dia:', dia)
print ('Estamos no mês:', mês)
print ('Estamos no ano:', ano)
print ('O horário de agora é:', hora, min, segundos,'horário de Brasilia')