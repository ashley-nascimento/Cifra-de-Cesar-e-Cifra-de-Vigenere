print("Cifra de Vigenère")
while True:
  opcao = input("\nVocê deseja (C)Cifrar ou (D)Descrifar?  ").upper()
  chave = input("Qual a chave?  ").upper()
  texto = input("Escreva a palavra ou texto:  ").replace(' ', '').upper()

  alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

  #deixa a chave do tamanho do texto
  if len(chave) < len(texto):
    chave = chave * int((len(texto)))
    chave = chave[:len(texto)]
  else:
    chave = chave[:len(texto)]

  #cria as listas
  texto = list(texto)
  chave = list(chave)
  idx_crip = []
  resultado = ""

  #Se a opção é Cifrar
  if opcao == "C": 
    for x, y in zip(texto, chave):
      if(x not in alfabeto):
        resultado = resultado + x
      idx_crip.append((alfabeto.index(x) + alfabeto.index(y))%26)

  #Se a opção é Descifrar
  if opcao == "D":
    for x, y in zip(texto, chave):
      if(x not in alfabeto):
        resultado = resultado + x
      idx_crip.append((alfabeto.index(x) - alfabeto.index(y))%26)

  #Converte o index do alfabeto no resultado
  for c in idx_crip:
    resultado = resultado + alfabeto[(c)]
     
  print ("\nResultado: ", resultado)

  print("-"*50)
  if(input("Deseja realizar outra operação? (y/n)") =="n" ):
    print("Bye bye!")
    break
