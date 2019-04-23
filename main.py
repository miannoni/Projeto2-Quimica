import os

materiais = {
	# str : {"Eletrons": int(), "Potencial": int(), "Solucao": str()}
	"Cobre" : {"Eletrons": 2, "Potencial": 0.34, "Solucao": "CuSO4"},
	"Zinco" : {"Eletrons": 2, "Potencial": -0.76, "Solucao": "ZnSO4"}
	}

def preenche_dicionario(dicionario, nome):
	print(nome)
	dicionario_saida = {}
	for i in dicionario.keys():
		if str(type(dicionario[i])) == "<class 'dict'>":
			dicionario_saida[i] = preenche_dicionario(dicionario[i], i)
		else:
			dicionario_saida[i] = input(i + " :\n")
	return dicionario_saida

def montar_pilha():
	print("Por favor nos diga como essa pilha tem que ser:")

	print("Materiais disponiveis:")
	for i in materiais.keys():
		print(i)

	inputs = {
		"Catodo"		: {"Material de eletrodo": str(), "Concentracao da solucao": float(), "Massa de eletrodo": float()},
		"Anodo"			: {"Material de eletrodo": str(), "Concentracao da solucao" : float(), "Massa de eletrodo": float()},
		"Temperatura"	: float()
		}

	inputs = preenche_dicionario(inputs, "Preencha as informações:")

	outputs = {
		"DDP": str(),
		"Capacidade de carga" : str(),
		"Densidade de carga" : str(),
		"Densidade de energia" : str(),
		"Custo" : str()
	}

	print(inputs)
	exit()

def selecionar_pilha():
	print("Por favor nos diga como essa pilha tem que ser:")

	print("Materiais disponiveis:")
	for i in materiais.keys():
		print(i)

	inputs = {
		"DDP"					: float(),
		"Potencia"				: float(),
		"Tempo em segundos"		: float()
		}

	inputs = preenche_dicionario(inputs, "Preencha as informações:")

	print(inputs)
	exit()


os.system("cls")

while True:

	o_que_fazer = input("Você deseja montar uma pilha (1), selecionar uma pilha pronta (2) ou sair do programa (sair)?\n")

	if (o_que_fazer == "1"):
		print()
		montar_pilha()
		os.system("cls")

	elif (o_que_fazer == "2"):
		selecionar_pilha()
		os.system("cls")

	elif (o_que_fazer.lower() == "sair"):
		os.system("cls")
		exit()

	else:
		os.system("cls")
		print("Por favor escolha uma das opções disponiveis\n")
