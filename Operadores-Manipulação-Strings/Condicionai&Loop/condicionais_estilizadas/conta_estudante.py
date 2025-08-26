# Demonstração de IF aninhados, cada um dentro do outro e se apoiando

saldo = 2000
saque_max = 500
cheque_especial = 450

opcao = int(input("Digite o tipo de conta: \n [1] Conta Normal \n [2] Conta Universitária\n > "))

if opcao == 1:
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= saldo:
        if valor_saque <= saque_max:
            print("Saque realizado com sucesso!")
            saldo -= valor_saque
        else:
            print("Valor do saque excede o limite máximo por operação.")
    elif valor_saque <= (saldo + cheque_especial):
        print("Saque realizado utilizando cheque especial!")
        saldo -= valor_saque
    else:
        print("Saldo insuficiente, mesmo com cheque especial.")
elif opcao == 2:
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= saldo:
        print("Saque realizado com sucesso!")
        saldo -= valor_saque
    else:
        print("Saldo insuficiente.")
else:
    print("Opção inválida.")

print(f"Saldo atual: R$ {saldo:.2f}")