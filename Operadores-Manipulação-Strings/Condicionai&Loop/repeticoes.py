#For loops

texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end ="")  # Serve para separar as vogais do texto
else:
    print()
    print("Para executar no final do laço") # Essa parte é o for else.
              

print(" ")              
print("----------------------------------------------------------------------")
# For else? Executa no final do meu laço


# E tem range? Ora se não...

# >> Segue então como fazer.
for numero in range(0,10):
    print(numero, end=" ")
    
print(" ")

# Fazer tabuada tem como?

for numero in range(0, 51 , 5): # Respectivamente (Inicia, Até onde, Step (pulos)) 
    # Por que no 51 e não no 50? -> O 51 é o numero exclusivo não inclusivo!!! 51 - 1 : 50
    print(numero, end=" ")
    
    
print(" ")    
# While funciona como no python?

print("----------------------------------------------------------------------")

opcao = -1

while opcao != 0:
    opcao = int(input("O que você deseja fazer?\n [1] Sacar \n [2] Depositar \n [0] Sair \n >"))
    if opcao == 1:
        print("Você está realizando um saque...")
        # Continua o codigo aqui e pararapapa // Já fiz isso umas 27 vezes
    elif opcao == 2:
        print("Você está realizando um deposito...")

print("Você escolheu sair")
        
        
# Da pra usar o break tbm

while True:
    numero_sortido = int(input("Teste um numero da sorte: "))
    
    if numero_sortido == 10:
        break
    
    print("Não foi dessa vez, tenta novamente > ", numero_sortido)