"""Desafio 4 - Calculadora de desconto."""

preco = float(input("Preço do produto: R$ "))
percentual_desconto = float(input("Percentual de desconto (%): "))

valor_desconto = preco * percentual_desconto / 100
preco_final = preco - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
