def conversão():
    while True:
        try:
        
            conversor = int(input("\nIndique abaixo quantos segundos quer converter: "))
            dias = conversor // 86400
            horas = conversor // 3600
            segundos = conversor % 3600
            minutos = segundos // 60
            mr = segundos // 60
            sr = minutos % 60
        
            print(f"\n{conversor} segundos, resultam em {dias} dias, {horas} horas, {mr} minutos e restam {sr} segundos")
    
        except ValueError:
            print ("\nletras ou palavras não podem ser executadas, insira novamente abaixo.")
        
conversão()