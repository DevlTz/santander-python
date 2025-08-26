# Descobrir se aquilo está ou não no valor
banco = "Python Santander"
pessoas = ["João", "Laura", "Gabriel", "Pedro"]
saques = [1000, 2400, 3000]

print("Python" in banco)
# Para provar e verificar existência ou presença no valor.

print("Carlos" in pessoas)
# Retorna falso, pois Carlos não pertence ao conj Pessoas(P)


if 2400 in saques:
    print("Possível saque disponível")
# Semantica e escrita influencia na parte da verificação

print("joão" in pessoas)
#Verifique o que ele vai responder -> False (João) != (joão) - Na escrita
# Você pode fazer uma lógica para botar e não diferenciar upper ou lower case.