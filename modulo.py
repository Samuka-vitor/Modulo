# mostrar o menu 
def exibir_menu():
    print("0 - Sair do programa.")
    print("1 - Verificar maioridade.")
    print("2 - Calcular IMC.")

# Verificar a maioridade 
def verificar_maioridade(nome, idade):
    if idade >=18:
        return f"{nome} é maior de idade."
    return f"{nome} é menor de idade."

# calcula o IMC 
calcular_imc = lambda peso, altura: peso/(altura**2)
