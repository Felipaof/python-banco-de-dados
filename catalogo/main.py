Pessoa = {}

def adicionar_variavel():
  nome = input("Digite o nome da pessoa: ")
  idade = input("Digite o idade da pessoa: ")
  Pessoa[nome] = idade
  print(f"Variável {nome} adicionada com sucesso!")

def remover_variavel():
  nome = input("Digite o nome da pessoa a ser removida: ")
  if nome in Pessoa:
    del Pessoa[nome]
    print(f"pessoa {nome} removida com sucesso!")
  else:
    print("pessoa não encontrada.")

def mostrar_Pessoa():
  if not Pessoa:
    print("Não há pessoa cadastradas.")
  else:
    print("pessoa:")
    for nome, idade in Pessoa.items():
      print(f"{nome} - {idade}")

def menu():
  while True:
    print("\nMenu:")
    print("1. Adicionar pessoa")
    print("2. Remover pessoa")
    print("3. Mostrar pessoa")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
      adicionar_variavel()
    elif opcao == '2':
      remover_variavel()
    elif opcao == '3':
      mostrar_Pessoa()
    elif opcao == '4':
      break
    else:
      print("Opção inválida.")

if __name__ == "__main__":
  menu()
