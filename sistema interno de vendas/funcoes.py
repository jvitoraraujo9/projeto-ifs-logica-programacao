def menu():

	opcao = int(input("\n****SISTEMA INTERNO DE VENDAS****\n\n1. COMPRAR\n"+
				  "2. CONSULTAR ESTOQUE\n"+
				  "3. PRODUTOS\n"+
				  "4. RECEITAS\n"+
				  "0. SAIR\n"))
	return opcao;
	
	
def menu1():
	opcao = input("***CARRINHO***\n\nDIGITE O NOME OU CODIGO DO PRODUTO:\n").upper()
	return opcao;
	
def verificaCPF():
	cpf = input("CPF: ")
	while((len(cpf) < 11) or (len(cpf) > 11)):
		print("CPF INVALIDO")
	return cpf;
	

def menu1_cliente():
	opcao = int(input("1. CADASTRAR CLIENTE\n2. CLIENTE JA CADASTRADO\n"))
	return opcao;
	


	
def menu2():
	opcao = int(input("1. CONSULTAR PRODUTO\n"+
				  "2. CONSULTA PRODUTO POR DEPARTAMENTO\n"+
				  "3. TODOS OS PRODUTOS\n"+
				  "0. VOLTAR\n"))
				  
	return opcao;



	
def menu3():
	opcao = int(input("1. CADASTRAR EQUIPAMENTO\n"+
				  "2. REMOVER VOLUME DE PRODUTO\n"+
				  "3. REMOVER PRODUTO\n"+
				  "0. VOLTAR\n"))
	return opcao;

										
