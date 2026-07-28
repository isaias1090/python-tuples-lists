frutas=("maçã","banana","laranja","uva")
p1=str(input("Qual fruta você quer verificar?"))
if p1 in frutas:
    escolha=str(input(f"{p1} está presente na tupla, deseja adicionar outra fruta?"))
    if escolha=="sim":
        fruta_lista=list(frutas)
        fruta_adicionada=str(input("Digíte o nome da fruta que deseja adicionar: "))
        fruta_lista.append(fruta_adicionada)
        frutas=tuple(fruta_lista)
        print(frutas)
else:
    escolha=str(input(f"A fruta {p1} não está na tupla. Deseja adiciona-la?"))
    if escolha=="sim":
        fruta_lista=list(frutas)
        fruta_lista.append(p1)
        frutas=tuple(fruta_lista)
        print(frutas)
