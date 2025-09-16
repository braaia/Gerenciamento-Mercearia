from DAO import *
from Models import *
from datetime import datetime

class ControllerCategoria:
    def cadastroCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria.lower() == novaCategoria.lower():
                existe = True
            
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso!")
        else:
            print("Essa categoria já existe!")

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat_list = list(filter(lambda x: x.categoria.lower() == categoriaRemover.lower(), x))

        if len(cat_list) <= 0:
            print("A categoria que deseja remover não existe!")
        else:
            for i in range(len(x)):
                if x[i].categoria.lower() == categoriaRemover.lower():
                    del x[i]
                    break
            print("Categoria removida com sucesso!")

            with open('categorias.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, novaCategoria):
        x = DaoCategoria.ler()

        cat_list = list(filter(lambda x: x.categoria.lower() == categoriaAlterar.lower(), x))

        if len(cat_list) > 0:
            cat1_list = list(filter(lambda x: x.categoria.lower() == novaCategoria.lower(), x))
            if len(cat1_list) == 0:
                x = list(map(lambda x: Categoria(novaCategoria) if(x.categoria.lower() == categoriaAlterar.lower()) else(x), x))
                print("Categoria alterada com sucesso!")
            else:
                print("A categoria que você deseja alterar já existe!")
        else:
            print("A Categoria que você deseja alterar não existe!")

        with open('categorias.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()

        if len(categorias) <= 0:
            print("Categoria vazia!")
        else:
            for i in categorias:
                print(f"Categoria: {i.categoria}")

class ControllerEstoque:
    def cadastroProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()

        cat_list = list(filter(lambda y: y.categoria.lower() == categoria.lower(), y))
        nome_list = list(filter(lambda x: x.produto.nome.lower() == nome.lower(), x))

        if len(cat_list) > 0:
            if len(nome_list) == 0:
                DaoEstoque.salvar(Produtos(nome, preco, categoria), quantidade)
                print("Produto cadastrado no estoque com sucesso!")
            else:
                print("Esse produto já existe!")
        else:
            print("Essa categoria não existe!")

    def removerProduto(self, produtoRemover):
        x = DaoEstoque.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == produtoRemover.lower(), x))

        if len(est_list) > 0:
            for i in range(len(x)):
                if x[i].produto.nome.lower() == produtoRemover.lower():
                    del x[i]
                    print("Produto removido com sucesso")  
                    break
        else:
            print("Esse produto que deseja remover não existe")
            
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')
    
    def alterarProduto(self, produtoAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == produtoAlterar.lower(), x))

        if len(est_list) > 0:
            est1_list = list(filter(lambda x: x.produto.nome.lower() == novoNome.lower(), x))
            if len(est1_list) == 0:
                cat_list = list(filter(lambda y: y.categoria.lower() == novaCategoria.lower(), y))
                if len(cat_list) > 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome.lower() == produtoAlterar.lower()) else(x), x))
                    print("Produto alterado completamente com sucesso!")
                else:
                    print("A categoria desejada não existe na lista de categorias!")
            else:
                print("Este produto já está registrado no estoque!")
        else:
            print("Esse produto não existe no estoque!")

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')

    def alterarNome(self, nomeAlterar, novoNome):
        x = DaoEstoque.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == nomeAlterar.lower(), x))

        if len(est_list) > 0:
            est1_list = list(filter(lambda x: x.produto.nome.lower() == novoNome, x))
            if len(est1_list) == 0:
                x = list(list(map(lambda x: Estoque(Produtos(novoNome, x.produto.preco, x.produto.categoria), x.quantidade) if(x.produto.nome.lower() == nomeAlterar.lower()) else(x), x)))
                print("Nome do produto alterado com sucesso!")
            else:
                print("Esse produto já existe no estoque!")
        else:
            print("Esse produto não existe no estoque!")

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')

    def alterarPreco(self, produtoAlterar, novoPreco):
        x = DaoEstoque.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == produtoAlterar.lower(), x))

        if len(est_list) > 0:
            est1_list = list(filter(lambda x: x.produto.preco == novoPreco, x))
            if len(est1_list) == 0:
                x = list(map(lambda x: Estoque(Produtos(x.produto.nome, novoPreco, x.produto.categoria), x.quantidade) if(x.produto.nome.lower() == produtoAlterar.lower()) else(x), x))
                print("Preço do produto alterado com sucesso!")
            else:
                print("Você colocou o preço igual ao anterior, por favor escolha outro caso deseja alterar!")
        else:
            print("O nome do produto que deseja alterar o preço não existe!")

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')

    def alterarCategoria(self, produtoAlterar, novaCategoria):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == produtoAlterar.lower(), x))

        if len(est_list) > 0:
            est1_list = list(filter(lambda y: y.categoria.lower() == novaCategoria.lower(), y))
            if len(est1_list) > 0:
                x = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, novaCategoria), x.quantidade) if(x.produto.nome.lower() == produtoAlterar.lower()) else(x), x))
                print("Categoria do produto alterada com sucesso!")
            else:
                print("Essa categoria não existe na lista de categorias!")
        else:
            print("Esse produto não existe no estoque!")

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')

    def adicionarQuantidade(self, produtoAlterar, novaQuantidade):
        x = DaoEstoque.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == produtoAlterar.lower(), x))

        if len(est_list) > 0:
            x = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, x.produto.categoria), int(x.quantidade) + int(novaQuantidade)) if(x.produto.nome.lower() == produtoAlterar.lower()) else(x), x))
            print("Produto adicionado ao estoque com sucesso!")
        else:
            print("Produto desejado não existe no estoque!")

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')

    def removerQuantidade(self, produtoAlterar, removerQuantidade):
        x = DaoEstoque.ler()
        est_list = list(filter(lambda x: x.produto.nome.lower() == produtoAlterar.lower(), x))

        if len(est_list) > 0:
            x = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, x.produto.categoria), int(x.quantidade) - int(removerQuantidade)) if(x.produto.nome.lower() == produtoAlterar.lower()) else(x), x))
            print("Produto adicionado ao estoque com sucesso!")
        else:
            print("Produto desejado não existe no estoque!")

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}")
                arq.writelines('\n')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()

        if len(estoque) <= 0:
            print("Estoque vazio!")
        else:
            for i in estoque:
                print(f"Estoque de: {i.produto.nome} | Preço: {i.produto.preco}R$ - Categoria: {i.produto.categoria} - Quantidade: {i.quantidade}\n")

a = ControllerEstoque()
a.mostrarEstoque()