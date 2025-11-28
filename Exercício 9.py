
class Produto:
    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
    
    def listar(self):
        print(f'Nome: {self.nome}\nCódigo: {self.codigo}\nPreço: R${self.preco:.2f}')


CARDAPIO = {
    100: Produto("Cachorro Quente", 100, 11.20),
    101: Produto("Bauru Simples", 101, 11.00),
    102: Produto("Bauru com ovo", 102, 14.00),
    103: Produto("Hambúrguer", 103, 12.90),
    104: Produto("Cheeseburguer", 104, 13.90),
    105: Produto("Refrigerante", 105, 10.00),
}


def obter_pedidos():
    pedidos = {}
    
    print("Digite o código do produto e a quantidade (0 para finalizar):")
    while True:
        try:
            codigo = int(input("\nCódigo do produto (ou 0 para sair): "))
            if codigo == 0:
                break
            
            if codigo not in CARDAPIO:
                print("Código inválido! Tente novamente.")
                continue
            
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Quantidade deve ser positiva!")
                continue
            
            if codigo in pedidos:
                pedidos[codigo] += quantidade
            else:
                pedidos[codigo] = quantidade
                
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")
    
    return pedidos


def exibir_conta(pedidos):
    if not pedidos:
        print("Nenhum pedido realizado.")
        return
    
    print("\n" + "+" + "-" * 67 + "+")
    print("|" + " " * 20 + "RESUMO DA CONTA" + " " * 33 + "|")
    print("+" + "-" * 15 + "+" + "-" * 8 + "+" + "-" * 18 + "+" + "-" * 12 + "+" + "-" * 14 + "+")
    print(f"| {'Especificação':<13} | {'Código':<6} | {'Preço Unit.(R$)':<16} | {'Qtd':<10} | {'Total (R$)':<12} |")
    print("+" + "-" * 15 + "+" + "-" * 8 + "+" + "-" * 18 + "+" + "-" * 12 + "+" + "-" * 14 + "+")
    
    total_geral = 0
    for codigo, quantidade in pedidos.items():
        produto = CARDAPIO[codigo]
        subtotal = produto.preco * quantidade
        total_geral += subtotal
        
        print(f"| {produto.nome:<13} | {codigo:<6} | R${produto.preco:>13.2f} | {quantidade:>10} | R${subtotal:>10.2f} |")
    
    print("+" + "-" * 15 + "+" + "-" * 8 + "+" + "-" * 18 + "+" + "-" * 12 + "+" + "-" * 14 + "+")
    print(f"| Total Geral:" + " " * 60 + f"R${total_geral:>10.2f} |")
    print("+" + "-" * 67 + "+")


print("=== Lanchonete do Manuel ===\n")
pedidos = obter_pedidos()
exibir_conta(pedidos)
