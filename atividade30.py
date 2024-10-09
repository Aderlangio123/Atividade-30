# crie uma funcao que calcule a nota, a media de 3 notas, em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    return media

def verificação(media):
    if media >= 7:
        return "aprovado"
    else:
        return "reprovado"


nota1 = float(input("digite a nota 1  "))
nota2 = float(input("digite a nota 2  "))
nota3 = float(input("digite a nota 3  "))

resultado = media(nota1, nota2, nota3)
verificacao_final = verificação(resultado)
print(verificacao_final)
print("sua nota é ", resultado)
