valor_compra = float(input("Valor da compra: R$ "))
#Lê o valor digitado pelo usuário e converte em ponto flutuante
valor_pago = float(input("Valor pago: R$ "))

troco = valor_pago - valor_compra
#subtrai os valores dados e guarda na variável "troco"
print(f"Troco: R$ {troco:.2f}")
#imprime o resultado com a formatação de 2 casas decimais ".2f". 
#Isso ocorre para que não apareça números muito longos na tela




