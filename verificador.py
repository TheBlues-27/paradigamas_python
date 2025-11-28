
def validar_cpf(cpf):    
    cpf = cpf.replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - (soma % 11)
    primeiro_digito = 0 if primeiro_digito >= 10 else primeiro_digito
    
    if int(cpf[9]) != primeiro_digito:
        return False
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - (soma % 11)
    segundo_digito = 0 if segundo_digito >= 10 else segundo_digito
    
    if int(cpf[10]) != segundo_digito:
        return False
    
    return True
