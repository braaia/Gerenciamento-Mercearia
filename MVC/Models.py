from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):                
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        
class Estoque:
    def __init__(self, produto: Produtos, quantidade):        
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendidos: Produtos, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, tel, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.tel = tel
        self.categoria = categoria
        
class Pessoa:
    def __init__(self, nome, cpf, tel, email, idade):
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.email = email
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, clt, cargo, nome, cpf, tel, email, idade):
        self.clt = clt
        self.cargo = cargo
        super(Funcionario, self).__init__(nome, cpf, tel, email, idade)