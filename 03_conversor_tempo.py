"""Desafio 3 - Conversor de tempo (segundos -> horas, minutos e segundos)."""

total_segundos = int(input("Digite o tempo em segundos: "))

horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print(f"{total_segundos} segundos = {horas}h {minutos}min {segundos}s")

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
