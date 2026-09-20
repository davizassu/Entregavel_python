"""Desafio 5 - Par ou ímpar (usando o operador de módulo %)."""

numero = int(input("Digite um número inteiro: "))

# numero % 2 vale 0 (par) ou 1 (ímpar) e serve de índice da tupla.
# Sem if/else, pois condicionais ainda serão vistos nas próximas aulas.
resultado = ("par", "ímpar")[numero % 2]

print(f"O número {numero} é {resultado}.")
