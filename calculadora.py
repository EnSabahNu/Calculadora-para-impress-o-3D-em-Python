print("#" * 40)
print()
print("CALCULADORA DE IMPRESSÃO 3D")
print()
print("#" * 40)

peso_da_peca = float(input("Digite o peso da peça: "))
while(peso_da_peca <= 0):
    print("Número inválido, digite um número acima de zero.")
    peso_da_peca = float(input("Digite o peso da peça: "))

print() 

tempo_de_impressao = float(input("Digite o tempo de impressão(h): "))
while(tempo_de_impressao <= 0):
    print("Número inválido, digite um número acima de zero.")
    tempo_de_impressao = float(input("Digite o tempo de impressão(h): "))

print()

preco_do_filamento = float(input("Digite o preço do filamento: R$"))
while(preco_do_filamento <= 0):
    print("Número inválido, digite um número acima de zero.")
    preco_do_filamento = float(input("Digite o preço do filamento: R$"))

print()

custo_de_energia = float(input("Digite o kwh em R$ do seu Estado: R$"))
while(custo_de_energia <= 0):
    print("Número inválido, digite um número acima de zero.")
    custo_de_energia = float(input("Digite o kwh em R$ do seu Estado: R$"))

print()

print("Caso você não saiba. Digite 0,07.")
consumo_medio = float(input("Digite o consumo médio da sua impressora: "))
while(consumo_medio <= 0):
    print("Número inválido, digite um número acima de zero.")
    consumo_medio = float(input("Digite o consumo médio da sua impressora: "))

print()

desgaste = float(input("Digite o valor do desgaste em %: "))
while(desgaste <= 0):
    print("Número inválido, digite um número acima de zero.")
    desgaste = float(input("Digite o valor do desgaste em %: "))

print()

acabamento = float(input("Digite o valor do acabamento: R$"))
while(acabamento <= 0):
    print("Número inválido, digite um número acima de zero.")
    acabamento = float(input("Digite o valor do acabamento: R$"))

print()

preco_cobrado = float(input("Digite o valor cobrado da sua impressão: R$"))
while(preco_cobrado <= 0):
    print("Número inválido, digite um número acima de zero.")
    preco_cobrado = float(input("Digite o valor cobrado da sua impressão: R$"))

print()
print("#" * 40)
print("RESULTADO")
print("#" * 40)
print()

custo_do_filamento = (peso_da_peca * preco_do_filamento / 1000)
print(f"CUSTO DO FILAMENTO(R$): {custo_do_filamento:.2f}")

energia_gasta = consumo_medio * tempo_de_impressao * custo_de_energia
print(f"CUSTO DE ENERGIA: R${energia_gasta:.2f}" )

custo_base = custo_do_filamento + energia_gasta

valor_desgaste = custo_base * (desgaste / 100)

custo_total = custo_base + valor_desgaste + acabamento
print(f"CUSTO TOTAL: R${custo_total:.2f}")

preco_sugerido_2x = custo_total * 2
print(f"PREÇO SUGERIDO 2X: R${preco_sugerido_2x:.2f}")

preco_sugerido_3x = custo_total * 3
print(f"PREÇO SUGERIDO 3X: R${preco_sugerido_3x:.2f}")

lucro = preco_cobrado - custo_total
print(f"LUCRO(R$): R${lucro:.2f}")

margem_porcentagem = (lucro / preco_cobrado) * 100
print(f"MARGEM(%): {margem_porcentagem:.2f}")
