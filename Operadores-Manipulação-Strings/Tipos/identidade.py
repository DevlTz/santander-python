# Comparar se dois objetos ocupam mesmo espaço de memoria

curso = "curso de python"
nome_curso = curso
saldo, limite = 400, 570

curso is nome_curso

print(saldo is limite)
# Descobrir se ele ocupa mesma região de memoria

# Descobrir também se ele não ocupa
print (saldo is not limite)


