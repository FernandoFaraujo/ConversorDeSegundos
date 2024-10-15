# Este programa apresenta a conersão de segundos em dias, horas, minutos e restante dos segundos.

conversor = int(input("\nIndique abaixo quantos segundos quer converter: "))

dias = conversor // 86400

horas = conversor // 3600

segundos = conversor % 3600

minutos = segundos // 60

mr = segundos // 60

sr = minutos % 60

print(f"\n{conversor} segundos, resultam em {dias} dias, {horas} horas, {mr} minutos e restam {sr} segundos.\n")
