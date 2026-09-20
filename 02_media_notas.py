nota_1 = float(input("Digite a 1ª nota: "))
nota_2 = float(input("Digite a 2ª nota: "))
nota_3 = float(input("Digite a 3ª nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"Média: {media:.2f}")

#Versão Portugol:
programa {
  inclua biblioteca Matematica --> mat

  funcao inicio() {
    real nota_1, nota_2, nota_3, media

    // Lê as 3 notas
    escreva("Digite a 1ª nota: ")
    leia(nota_1)
    escreva("Digite a 2ª nota: ")
    leia(nota_2)
    escreva("Digite a 3ª nota: ")
    leia(nota_3)

    // Soma as notas e divide por 3
    media = (nota_1 + nota_2 + nota_3) / 3

    // Arredonda a média para 2 casas decimais
    escreva("Média: ", mat.arredondar(media, 2), "\n")
  }
}

#Versão Portugal:
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
