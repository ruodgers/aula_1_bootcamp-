print("Olá. Preencha as Informações abaixo.")
CONTANTE_BONUS = 1000
nome = input("Digite o seu nome: ")
salario = (float(input("Digite o seu salário: ")))
bonus = (float(input("Digite o bonus recebido: ")))
valor_do_bonus = CONTANTE_BONUS + salario * bonus
print(f"O Usuário {nome} possui o bônus de {valor_do_bonus}")

