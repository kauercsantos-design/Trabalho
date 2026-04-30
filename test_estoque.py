import unittest
from estoque import Estoque

class TestEstoque(unittest.TestCase):

    def setUp(self):
        self.e = Estoque()

    def test_adicionar_produto(self):
        self.e.adicionar_produto("Mouse", 5, 50)
        self.assertEqual(len(self.e.produtos), 1)

    def test_listar_produtos(self):
        self.e.adicionar_produto("Mouse", 5, 50)
        self.e.adicionar_produto("Teclado", 10, 120)
        produtos = self.e.listar_produtos()
        self.assertEqual(len(produtos), 2)

    def test_buscar_produto(self):
        self.e.adicionar_produto("Mouse", 5, 50)
        produto = self.e.buscar_produto("Mouse")
        self.assertIsNotNone(produto)

    def test_buscar_produto_inexistente(self):
        produto = self.e.buscar_produto("Monitor")
        self.assertIsNone(produto)

    def test_atualizar_estoque(self):
        self.e.adicionar_produto("Mouse", 5, 50)
        resultado = self.e.atualizar_estoque("Mouse", 3)
        self.assertTrue(resultado)
        self.assertEqual(self.e.buscar_produto("Mouse").quantidade, 8)

    def test_atualizar_estoque_produto_inexistente(self):
        resultado = self.e.atualizar_estoque("Monitor", 3)
        self.assertFalse(resultado)

    def test_remover_produto(self):
        self.e.adicionar_produto("Mouse", 5, 50)
        resultado = self.e.remover_produto("Mouse")
        self.assertTrue(resultado)
        self.assertEqual(len(self.e.produtos), 0)

    def test_remover_produto_inexistente(self):
        resultado = self.e.remover_produto("Mouse")
        self.assertFalse(resultado)

    def test_estoque_baixo(self):
        self.e.adicionar_produto("Mouse", 3, 50)
        self.e.adicionar_produto("Teclado", 10, 120)

        baixos = self.e.estoque_baixo()
        self.assertEqual(len(baixos), 1)


if __name__ == "__main__":
    unittest.main()