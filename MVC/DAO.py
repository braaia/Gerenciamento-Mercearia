from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('categorias.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('categorias.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat_list = []
        for i in cls.categoria:
            cat_list.append(Categoria(i))
        return cat_list

# DaoCategoria.salvar("Frutas")
# DaoCategoria.salvar("Verduras")
# DaoCategoria.salvar("Legumes")
# DaoCategoria.ler()

class DaoEstoque:
    @classmethod
    def salvar(cls, produtos: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(f"{produtos.nome}|{produtos.preco}|{produtos.categoria}|{str(quantidade)}")
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        estoq_list = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                estoq_list.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return estoq_list

# x = Produtos("Açai", 20, "Frios")
# DaoEstoque.salvar(x, 1)
# DaoEstoque.ler()

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(f"{venda.vendedor}|{venda.itensVendidos.nome}|{venda.itensVendidos.preco}|{venda.itensVendidos.categoria}|{venda.comprador}|{str(venda.quantidadeVendida)}|{venda.data}")
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vendas_list = []
        for i in cls.venda:
            vendas_list.append(Venda(Produtos(i[1], i[2], i[3]), i[0], i[4], i[5], i[6]))
        return vendas_list

# x = Produtos("morango", 20, "frutas")
# y = Venda(x, "Wesley", "Andrey", 15)
# DaoVenda.salvar(y)
# DaoVenda.ler()

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(f"{fornecedor.nome}|{str(fornecedor.cnpj)}|{str(fornecedor.tel)}|{fornecedor.categoria}")
            arq.writelines('\n')
        
    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn_list = []
        for i in cls.fornecedor:
            forn_list.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn_list

# x = Fornecedor("Coca-Cola", "40.432.544/0001-47", "(82) 9 8716-3703", "Bebidas")
# DaoFornecedor.salvar(x)
# DaoFornecedor.ler()

class DaoCliente:
    @classmethod
    def salvar(cls, cliente: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(f"{cliente.nome}|{str(cliente.cpf)}|{str(cliente.tel)}|{str(cliente.email)}|{str(cliente.idade)}")
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.cliente = arq.readlines()

        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))

        clientes_list = []
        for i in cls.cliente:
            clientes_list.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes_list
    
# x = Pessoa("Wesley", 18815583890580, 91842890000, "apwiamciw109@gmail.com", 19)
# DaoCliente.salvar(x)
# DaoCliente.ler()

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(f"{funcionario.nome}|{funcionario.cpf}|{funcionario.clt}|{funcionario.cargo}|{funcionario.email}|{funcionario.tel}|{funcionario.idade}")
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
        print(cls.funcionario)

        func_list = []
        if len(cls.funcionario) > 0:
            for i in cls.funcionario:
                func_list.append(Funcionario(i[2], i[3], i[0], i[1], i[5], i[4], i[6]))
            return func_list
        
# x = Funcionario(True, "Ceo", "Wesley", 192823918799, 8282032838, "okwdamo290130@gmail.com", 19)
# DaoFuncionario.salvar(x)
# DaoFuncionario.ler()