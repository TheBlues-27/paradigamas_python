from verificador import validar_cpf

print("=== Validador de CPF ===\n")
    
while True:
    cpf = input("Digite um CPF (ou 'sair' para finalizar): ")
        
    if cpf.lower() == 'sair':
        break
        
    if validar_cpf(cpf):
        print(f"✓ CPF {cpf} é VÁLIDO\n")
    else:
        print(f"✗ CPF {cpf} é INVÁLIDO\n")