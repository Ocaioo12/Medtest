import tkinter as tk

def calcular_pontuacao(febre, tosse, adenopatia, exsudato, idade):
    pontos = 0
    pontos += 1 if febre == "sim" else 0
    pontos += 1 if tosse == "sim" else 0
    pontos += 1 if adenopatia == "sim" else 0
    pontos += 1 if exsudato == "sim" else 0

    if 3 <= idade <= 14:
        pontos += 1
    elif idade >= 45:
        pontos -= 1

    return pontos

def determinar_probabilidade(pontos):
    if pontos <= 0:
        return "1-2,5%"
    elif pontos == 1:
        return "5-10%"
    elif pontos == 2:
        return "11-17%"
    elif pontos == 3:
        return "28-35%"
    else:
        return "51-53%"

def processar_dados():
    try:
        idade = int(entry_idade.get())
        if idade < 0:
            raise ValueError("Idade inválida.")
    except ValueError:
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Erro: Por favor, insira uma idade válida.")
        return

    pontos = calcular_pontuacao(febre.get(), tosse.get(), adenopatia.get(), exsudato.get(), idade)
    probabilidade = determinar_probabilidade(pontos)

    resultado_text.delete("1.0", tk.END)
    resultado_text.insert(tk.END, f"A probabilidade do paciente estar com faringite por Streptococcus é: {probabilidade}")


root = tk.Tk()
root.title("MedTest - By: Caio e Yure")
root.geometry("520x350")
root.iconbitmap("ic2.ico") #Caso o arquivivo do ícone esteja em outra pasta pode usar assim também: r"Caminho/do/local/da/Pasta/com/o/arquivo.ico"
root.resizable(False, False)

frame_inputs = tk.Frame(root, padx=20, pady=20)
frame_inputs.pack(fill="both", expand=True)

febre = tk.StringVar(value="não")
tosse = tk.StringVar(value="não")
adenopatia = tk.StringVar(value="não")
exsudato = tk.StringVar(value="não")


tk.Label(frame_inputs, text="O paciente apresenta febre > 38°C ?").grid(row=0, column=0, sticky="w", pady=5)
tk.Radiobutton(frame_inputs, text="Sim", variable=febre, value="sim").grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame_inputs, text="Não", variable=febre, value="não").grid(row=0, column=2, sticky="w")

tk.Label(frame_inputs, text="O paciente apresenta ausência de tosse ?").grid(row=1, column=0, sticky="w", pady=5)
tk.Radiobutton(frame_inputs, text="Sim", variable=tosse, value="sim").grid(row=1, column=1, sticky="w")
tk.Radiobutton(frame_inputs, text="Não", variable=tosse, value="não").grid(row=1, column=2, sticky="w")

tk.Label(frame_inputs, text="O paciente apresenta sintomas de linfonodomegalia cervical anterior ?").grid(row=2, column=0, sticky="w", pady=5)
tk.Radiobutton(frame_inputs, text="Sim", variable=adenopatia, value="sim").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_inputs, text="Não", variable=adenopatia, value="não").grid(row=2, column=2, sticky="w")

tk.Label(frame_inputs, text="O paciente apresenta sintomas de exsudato ou edema amigdaliano ?").grid(row=3, column=0, sticky="w", pady=5)
tk.Radiobutton(frame_inputs, text="Sim", variable=exsudato, value="sim").grid(row=3, column=1, sticky="w")
tk.Radiobutton(frame_inputs, text="Não", variable=exsudato, value="não").grid(row=3, column=2, sticky="w")

tk.Label(frame_inputs, text="Informe a idade do paciente:").grid(row=4, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(frame_inputs, width=6)
entry_idade.grid(row=4, column=1)

tk.Button(frame_inputs, text="Calcular", command=processar_dados).grid(row=5, column=0, columnspan=3, pady=10)
resultado_text = tk.Text(root, height=5, width=50, wrap="word")
resultado_text.pack(padx=20, pady=(10, 20))


root.mainloop()
