from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

ano_atual = datetime.now().year
ano_nascimento = int(data_nascimento.split("/")[2])

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")


