# Python a indentação importa para onde começa o bloco e onde termina.

# Regra e importante para o estilo.

def sacar(valor):   
    saldo = 4000
    
    if saldo >= valor:
        print("Valor sacado!")
        saldo_pos_saque = saldo - valor
        print("Seu valor atual agora é:" saldo_pos_saque)
    
    
def depositar(valor):
    saldo = 400
    saldo+=valor
        
sacar(300)
depositar(200)
