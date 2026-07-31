idade = int(input("digite sua idade:"))
estudante = input("Você é estudante? (sim/não): ").strip().lower()

#Verificando se a pessoa tem direito à meia entrada
if idade < 18 or estudante == "sim":
    print("Meia entrada aplicada.")
else:
    print("Entrada inteira aplicada.")