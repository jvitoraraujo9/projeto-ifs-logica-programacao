from produto import *
from funcoes import *
import pickle


produto = []
cliente = []




try:
	arquivo = open('produtos.txt', 'rb')
	
except FileNotFoundError:
	arquivo = open("produtos.txt", "wb")
	arquivo.close()
	arquivo = open('clientes.txt', 'rb')

	
try:
	arquivo2 = open('clientes.txt', 'rb')
except FileNotFoundError:
	arquivo2 = open("clientes.txt", "wb")
	arquivo2.close()
	arquivo2 = open('clientes.txt', 'rb')

try:
	produto = pickle.load(arquivo)
	cliente = pickle.load(arquivo2)
except:
	print("\n")



op = menu()

while True:
		#Opcao 1: Realiza a compra
	while(op == 1):
		carrinho = []
		valorTotal = 0
		p= 0
		while True:
			print("-\n"*2)
			nome = menu1()
			for i in range(0, len(produto)):
				if((produto[i].nome == nome) or (produto[i].cod == nome)):
					if(produto[i].estoque > 0):
						produto[i].imprime()
						carrinho.append(produto[i].nome)
						valorTotal = produto[i].valor + valorTotal
						produto[i].estoque = produto[i].estoque-1
						p = 1
						break
					else:
						print("-\n"*2)
						print("SEM ESTOQUE DESSE PRODUTO NO MOMENTO")
						p = 2
						break

			if(p == 0):
				print("-\n"*2)
				print("PRODUTO NAO ENCONTRADO!\n")
				continue
			op2 = int(input("\n\n1. FINALIZAR COMPRA\n2. ADICIONAR PRODUTO\n"))
			if(op2 == 1):
				break
		
		op2 = menu1_cliente()
	
			#Cliente sem cadastro: 
		
		if(op2 == 1):
			print("-\n"*2)
			print("*CADASTRO CLIENTE*\n")
			nome = input("NOME: ").upper()
			cpf = verificaCPF()
			endereco = input("ENDERECO: ").upper()
			pagamento = input("DINHEIRO / DEBITO / CREDITO / CHEQUE: ").upper()
			cliente.append(Cliente(nome, cpf, endereco, carrinho, pagamento, valorTotal))
			
			print("\n\n*******COMPRA FINALIZADA COM SUCESSO********\n\n")
			for i in range(0, len(cliente)):
				if(cliente[i].nome == nome):
					cliente[i].imprimeCliente()
					break
		
				
			
			#Cliente ja cadastrado:
		
		if(op2 == 2):
			print("-\n"*2)
			nome = input("NOME DO CLIENTE: ").upper()
			cpf = input("CPF DO CLIENTE: ")
			for i in range(0, len(cliente)):
				if((cliente[i].nome == nome) and (cliente[i].cpf == cpf)):
					print("CLIENTE ENCONTRADO\n")
					cliente[i].prod = carrinho
					cliente[i].valorTotal = valorTotal
					print("\n\n*******COMPRA FINALIZADA COM SUCESSO********\n\n")
					cliente[i].imprimeCliente()
					break
	break
		
	#Opcao 3:
	
	while(op == 2):
		print("-\n"*2)
		op1 = menu2()

		
		if(op1 == 0):
			break
		
		if(op1 == 1):
			print("-\n"*2)
			print("\n*BUSCAR PRODUTO*\n")
			nome = input("DIGITE O PRODUTO: ").upper()
			P = 0
			for i in range(0, len(produto)):
				if(produto[i].nome == nome):
					produto[i].imprime()
					P = 1;
					print("-\n"*2)
					break
					
					
			if(P == 0):
				print("-\n"*2)
				print("PRODUTO NAO ENCONTRADO!\n")
					
		
		if(op1 == 2):
			print("-\n"*2)
			departamento = input("**BUSCA POR DEPARTAMENTO**\nDEPARTAMENTO: ").upper()
			P = 0;
			for i in range(0, len(produto)):
				if(produto[i].dep == departamento):
					produto[i].imprime()
					P = 1;
			if(P == 0):
				print("-\n"*2)
				print("\nNENHUM PRODUTO ENCONTRADO DESSE DEPARTAMENTO!\n")
				
			
		
		if(op1 == 3):
			for i in range(0, len(produto)):
				produto[i].imprime()
			print("-\n"*2)
			op1 = input("DIGITE 3 PARA RETORNAR\n")

		###

	while(op == 3):
		print("-\n"*2)
		op1 = menu3()
		
		
		if(op1 == 0):
			break
		
		
		
		while(op1 == 1):
			print("\n*CADASTRANDO PRODUTO*\n")
			nome = input("PRODUTO:").upper()
			valor= float(input("VALOR: "))
			cod  = input("CODIGO: ").upper()
			dep  = input("DEPARTAMENTO: ").upper()
			estoque  = int(input("QUANTIDADE DISPONIVEL: "))
			produto.append(Produto(nome, valor, cod, dep, estoque))
			print("-\n"*2)
			op1 = int(input("1. NOVO PRODUTO\n0. VOLTAR\n"));
			if(op1 == 0):
				break
		
		if(op1 == 2):
			print("-\n"*2)
			print("\n*DELETANDO PRODUTO*\n")
			nome = input("DIGITE O PRODUTO QUE DESEJA DELETAR\n").upper()
			estoque = int(input("DIGITE O VOLUME QUE DESEJA EXCLUIR\n"))
			i = 0;
			for i in range(0, len(produto)):
				
				if(produto[i].nome == nome):
					produto[i].estoque = produto[i].estoque - estoque
					i = 1;
					print("-\n"*2)
					print(estoque, "ITENS FORAM EXCLUIDOS COM SUCESSO!\n")
			if(i == 0):
				print("-\n"*2)
				print("PRODUTO NAO ENCONTRADO!\n")
	
				
			###
			
	if(op == 4):
		for i in range(0, len(cliente)):
			cliente[i].imprimeCliente()
			print("-\n"*2)
			
				
	if(op == 0):
		arquivo = open("produtos.txt", "wb")
		arquivo2 = open("clientes.txt", "wb")
		pickle.dump(produto, arquivo)
		pickle.dump(cliente, arquivo2)
		break;
	
	print("-\n"*2)
	op = menu()

	


	
	
	

	
