nome = input("Digite um funcionario: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionarios: "))
mensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(mensalidade))

print("===================Verifique os tipos de dados abaixo======================")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dados da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variável [mensalidade] é: ", type(mensalidade))