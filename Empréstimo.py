from datetime import datetime

data_devolucao = input("Digite a data de devolução do livro (dd/mm/aaaa): ")

data_atual = datetime.now().date()
data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y").date()

diferenca = (data_devolucao - data_atual).days

if diferenca > 0:
    print(f"Você tem {diferenca} dias para devolver.")
elif diferenca < 0:
    print(f"O livro está atrasado em {-diferenca} dias!")
else:
    print("O livro vence hoje!")
