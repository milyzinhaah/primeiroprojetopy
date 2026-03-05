nome=input("digite seu nome")
nota1=float(input("digite sua nota1"))
nota2=float(input("digite sua nota2"))
trabalho=float(input("digite sua nota do trabalho"))
media=(nota1+nota2+trabalho)/3
if media>=7:
    situacao="aprovado"
elif media>=5:
    situacao="recuperação"
else:
    situacao="reprovado"
    print("\nAluno:", nome)
    print("Média final: {:.2f}" .format(media) )
    print("Situação:", situacao)