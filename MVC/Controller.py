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
            else:
                print("A categoria que você deseja alterar já existe!")
        else:
            print("A Categoria que você deseja alterar não existe!")

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()

        if len(categorias) <= 0:
            print("Categoria vazia!")
        else:
            for i in categorias:
                print(f"Categoria: {i.categoria}")
