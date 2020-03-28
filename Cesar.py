print("Cifra de Cesar!")

while True:
  opcao = input("\nVocê deseja (C)Cifrar ou (D)Descrifar?  ").upper()
  chave = int(input("Qual o tamanho da chave?  "))
  texto = input("Escreva a palavra ou texto:  ").upper()

  alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  
  resultado = ""
  if opcao == "C":
    for x in list(texto):
      if(x not in alfabeto):
        resultado = resultado + x
      else:
        resultado = resultado + alfabeto[((alfabeto.index(x) + chave)%26)]
  else:
      for x in list(texto):
          if(x not in alfabeto):
              resultado = resultado + x
          else:
              resultado = resultado + alfabeto[((alfabeto.index(x) - chave)%26)]

  print ("\nResultado: ",resultado)

  print("-"*50)
  if(input("Deseja realizar outra operação? (y/n)") =="n" ):
    print("Bye bye!")
    break
