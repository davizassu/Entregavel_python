"""Desafio 4 - Calculadora de desconto."""

preco = float(input("Preço do produto: R$ "))
percentual_desconto = float(input("Percentual de desconto (%): "))

valor_desconto = preco * percentual_desconto / 100
preco_final = preco - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")


#Versão Portugol:
programa {
  funcao inicio() {
    inteiro total_segundos, horas, minutos, segundos

    // Lê o tempo total em segundos
    escreva("Digite o tempo em segundos: ")
    leia(total_segundos)

    // Divisão inteira (/) e resto (%) separam horas, minutos e segundos
    horas = total_segundos / 3600
    minutos = (total_segundos % 3600) / 60
    segundos = total_segundos % 60

    escreva(total_segundos, " segundos = ", horas, "h ", minutos, "min ", segundos, "s\n")
  }
}
