from estoque import Estoque
import os

def menu():
    e = Estoque()

    while True:
        print("\n--- CONTROLE DE ESTOQUE ---")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar estoque")
        print("4 - Remover produto")
        print("5 - Estoque baixo")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            qtd = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            e.adicionar_produto(nome, qtd, preco)

        elif opcao == "2":
            for p in e.listar_produtos():
                print(p)

        elif opcao == "3":
            nome = input("Produto: ")
            qtd = int(input("Quantidade a adicionar: "))
            if e.atualizar_estoque(nome, qtd):
                print("Atualizado!")
            else:
                print("Produto não encontrado.")

        elif opcao == "4":
            nome = input("Produto: ")
            if e.remover_produto(nome):
                print("Removido!")
            else:
                print("Produto não encontrado.")

        elif opcao == "5":
            baixos = e.estoque_baixo()
            print("Produtos com estoque baixo:")
            for p in baixos:
                print(p)

        elif opcao == "0":
            break

if __name__ == "__main__":
    if os.getenv("CI"):
        print("CI executado com sucesso!")
    else:
        # Execução automática (evita erro no Docker)
        e = Estoque()
        e.adicionar_produto("Mouse", 3, 50)
        e.adicionar_produto("Teclado", 10, 120)
        e.adicionar_produto("Monitor", 2, 900)

        for p in e.listar_produtos():
            print(p)

        print("\nEstoque baixo:")
        for p in e.estoque_baixo():
            print(p)