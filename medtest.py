def calcular_pontuacao():
    print("Critérios Centor e McIsaac")
    print("Responda às perguntas abaixo:")

    febre = input("O paciente tem febre > 38°C? (s/n): ").strip().lower()
    tosse = input("O paciente tem ausência de tosse? (s/n): ").strip().lower()
    adenopatia = input("O paciente tem adenopatia cervical anterior? (s/n): ").strip().lower()
    exsudato = input("O paciente tem exsudato ou edema amigdaliano? (s/n): ").strip().lower()

    pontos = 0
    pontos += 1 if febre == "s" else 0
    pontos += 1 if tosse == "s" else 0
    pontos += 1 if adenopatia == "s" else 0
    pontos += 1 if exsudato == "s" else 0

    idade = int(input("Informe a idade do paciente: "))
    if 3 <= idade <= 14:
        pontos += 1
    elif idade >= 45:
        pontos -= 1

    print(f"\nPontuação total: {pontos}")

    if pontos <= 0:
        probabilidade = "1-2,5%"
    elif pontos == 1:
        probabilidade = "5-10%"
    elif pontos == 2:
        probabilidade = "11-17%"
    elif pontos == 3:
        probabilidade = "28-35%"
    else:
        probabilidade = "51-53%"

    print(f"Probabilidade de faringite por Streptococcus do grupo A: {probabilidade}")

while True:
    print("\nMenu:")
    print("1 - Registrar um novo paciente")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        calcular_pontuacao()
    elif opcao == "2":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
