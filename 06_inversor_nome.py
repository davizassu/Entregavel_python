"""Desafio 6 - Inversor de nome (usando slicing [::-1])."""

nome = input("Digite um nome: ")

nome_invertido = nome[::-1]

print(f"Nome invertido: {nome_invertido}")

#Versão Portugol:
programa {
  inclua biblioteca Texto --> txt

  funcao inicio() {
    cadeia nome, nome_invertido = ""
    inteiro tamanho

    // Lê o nome e descobre quantos caracteres ele tem
    escreva("Digite um nome: ")
    leia(nome)
    tamanho = txt.numero_caracteres(nome)

    // Percorre o nome de trás para frente, letra por letra
    para (inteiro i = tamanho - 1; i >= 0; i--) {
      nome_invertido = nome_invertido + txt.extrair_subtexto(nome, i, i + 1)
    }

    escreva("Nome invertido: ", nome_invertido, "\n")
  }
}
