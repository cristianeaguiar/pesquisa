# lista
cidades = ["Plano Piloto", "Ceilândia", "Aguas Claras", "Taguatinga", "Sobradinho" "Núcleo Brandeirante", "Park Way", "Vicente Pires" "Itapoã", "Paranoá"]
           
# usuário informa o nome que deseja procurar
cidade = input("Informe o nome da cidade ue deseja procurar: ")

# informa a quantidade de vezes que o termo foi achado
quantidade = cidades.count(cidade)

#exibe o resultado na tela
if cidade in cidades:
    print(f"{cidade} foi encontrada na lista {quantidade} vezes.")
else:
    print(f"{cidade} não foi encontrado.")
