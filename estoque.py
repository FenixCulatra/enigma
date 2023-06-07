def main():
	tipo,tamanho = input().split(" ")
	tipo = int(tipo)
	tamanho = int(tamanho)
	
	estoque = []
	for i in range(tipo):
		linha = list()
		valores = input().split(" ")
		for x in range(len(valores)):
			linha.append(int(valores[x]))
		estoque.append(linha)
	
	
	compras = int(input())
	vendas = 0
	for i in range(compras):
		valores = input().split(" ")
		for x in range(len(valores)):
			valores[x] = int(valores[x])
		
		if estoque[valores[0] - 1][valores[1] - 1] > 0:
			estoque[valores[0] - 1][valores[1] - 1] -= 1
			vendas += 1
	
			
	print(vendas)
			
	return 0

if __name__=="__main__":
	main()
