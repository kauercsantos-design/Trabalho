from models import Produto

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade, preco):
        self.produtos.append(Produto(nome, quantidade, preco))

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, nome):
        for p in self.produtos:
            if p.nome.lower() == nome.lower():
                return p
        return None

    def atualizar_estoque(self, nome, quantidade):
        produto = self.buscar_produto(nome)
        if produto:
            produto.quantidade += quantidade
            return True
        return False

    def remover_produto(self, nome):
        produto = self.buscar_produto(nome)
        if produto:
            self.produtos.remove(produto)
            return True
        return False

    def estoque_baixo(self, limite=5):
        return [p for p in self.produtos if p.quantidade <= limite]