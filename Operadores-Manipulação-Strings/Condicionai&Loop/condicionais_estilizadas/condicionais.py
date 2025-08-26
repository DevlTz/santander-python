# Estrutura condicional permite o desvio quando determinadas expressões são atendidas

# If para fazer testes e verificar se tal coisa é possivel.

#saldo = 3000
#saque = float(input("Informe o valor que deseja sacar: "))

#if saque > saldo: 
#    print("Não é possível realizar porque você está tentando sacar um valor muito alto")
    
#if saldo >= saque:
#    print("Você conseguiu completar o saque: ")

# Essa estrutura não é tão funcional
# Fazemos da seguinte forma então

# ----------------------------------------------------------------------
print("----------------------------------------------------------------------")

#saldo_atual = 3000
#saque_novo = float(input("Informe o valor a ser retirado (sacado): "))

#if saldo_atual >= saque_novo:
  #  saldo_atualizado = saldo_atual - saque_novo
   # print("Seu saque foi realizado! Valor atual presente: ", saldo_atualizado)
#else:
   # print("Valor indisponível!")
   # print("Valor atual disponível", saldo_atual)
    
#print("----------------------------------------------------------------------")    
    
#---------------------------------------------------------------------

saldo = 27000
limite_diario = 2000
tipo_conta = "Especial"
opcao = int(input("Selecione uma opção: \n [1] Sacar \n [2] Depositar \n [3] Extrato \n > "))

if opcao == 1:
    saque = int(input("Informe o valor para sacar: "))
    if saldo >= saque:
        saldo_atual = saldo - saque
        print("Valor sacado! \n Segue seu valor atual: ", saldo_atual)
        
elif opcao == 2:
    print(input("Selecione quanto você quer depositar: "))
elif opcao == 3:
    print(f"Seu extrato impresso > > > \n {saldo} \n {limite_diario} \n {tipo_conta}")

else:
    sys.exit("Opção inválida.")