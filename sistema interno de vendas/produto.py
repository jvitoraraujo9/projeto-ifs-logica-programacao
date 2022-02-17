class Produto():

	def __init__(self, nome, valor: float, cod, dep, estoque: int):
		self.nome = nome
		self.valor = valor
		self.cod = cod
		self.dep = dep 
		self.estoque = estoque
	
	
	def imprime(self):
		print("\n\n*******************\nNOME:...................", self.nome, "\nVALOR:.................. R$",
		self.valor, "\nCODIGO:.................", self.cod,
		"\nDEPARTAMENTO:...........", self.dep, "\nQUANTIDADE DISPONIVEL:..", self.estoque,"\n*******************\n\n")
		
	
	
		
class Cliente():
	
	def __init__(self, nome, cpf, endereco, prod, pag, valorTotal):
		self.nome = nome
		self.cpf = cpf
		self.endereco = endereco
		self.prod = prod
		self.pag = pag
		self.valorTotal = valorTotal
		
		
	def imprimeCliente(self):
		print("*******************************************\nNOME:.............", self.nome, "\nCPF:............",
		self.cpf, "\nENDERECO:.........", self.endereco,
		"\nPRODUTO:.....", self.prod, "\nVALOR TOTAL DA COMPRA........", self.valorTotal, "\nPAGAMENTO:.........",
		self.pag, "\n*******************************************\n" )
		
		
		
		
		
		
		
		
		
