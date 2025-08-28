curso = "  Python "
# Veja como será a saída de cada um dos prints

print(curso)

# Metódos de string que facilitam a vida 

print(curso.upper())
print(curso.lower())
print(curso.title())


# Metodos para cortar espaços em brancos e principalmente impedir o usuario a fazer algo assim.
print(curso.strip())
# Essa corta o espaço inteiro
print(curso.rstrip())
# Essa corta o espaço da direita e mantem o da esquerda
print(curso.lstrip())
# Essa corta o espaço da esquerda e mantém o da direita.

curso_novo = "PYthonzin"

# Como fazer junções e principalmente se concentrar em adicionar caracteres pra sua palavra.

print(curso_novo.center(20,"#"))

# X = 20 para sendo o número de caracteres que você quer que complete -> "#" Sendo o caracter que vc quer

print("-".join(curso_novo))

# Essa vai fazer para que você possa separar cada caracter com o que você passou. Join para a palavra.
