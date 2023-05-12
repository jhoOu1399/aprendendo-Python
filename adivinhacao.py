print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 10

chute_srt = input("Digite o seu número: ")

print("Você digitou: ", chute_srt) 

chute = int(chute_srt)

if(numero_secreto == chute):
  print("Parábens, você acertou!")
else:
  print("Você errou, que pena...")
 
print("Fim de jogo")
