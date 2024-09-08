# Operador in checa se um elemento está contido em outro,
# por exemplo: "p" in "python" retorna True, pois "p" está contido em "python"
# "yt" in "python" retorna True, pois "yt" está contido em "python"
# "z" in "python" retorna False, pois "z" não está contido em "python"
"p" in "python"
"yt" in "python"


# Pecedência de operadores: https://docs.python.org/pt-br/3/reference/expressions.html#evaluation-order

# Exemplo de precedência de operadores:
# Média harmônica
x1 = 1
x2 = 2
x3 = 0.5
x4 = 0.25

n = 4

# simplificando a fórmula com o uso de parênteses e precedência
H = n / (1 / x1 + 1 / x2 + 1 / x3 + 1 / x4)

# Fórmula estendida, dividindo em etapas
x1_inv = 1 / x1
x2_inv = 1 / x2
x3_inv = 1 / x3
x4_inv = 1 / x4

denominador = x1_inv + x2_inv + x3_inv + x4_inv
H = n / denominador
H > 10

# com precedência, podemos simplificar a expressão, incluindo a comparação
n / (1 / x1 + 1 / x2 + 1 / x3 + 1 / x4) > 10

# redefinindo o valor de H para facilitar os exemplos
H = int(input("Digite um valor: "))
# Estruturas de controle de fluxo (ou condições/decisões)
if H > 10:  # se a média harmônica for maior que 10
    print("Média harmônica maior que 10")
    # imprime 2 sempre,
    # adicionado para exemplificar a execução de mais de uma instrução
    print(1 + 1)
# if H == 10:
elif H == 10:
    print("Média harmônica igual a 10")
elif H < 0:
    print("Média harmônica negativa")
# if not (H > 10) or H!=10 or H >=0:
else:
    print("Média harmônica entre 0 e 10")

# sempre será impresso, mesmo que a condição seja falsa
print("Fora do if/else")
