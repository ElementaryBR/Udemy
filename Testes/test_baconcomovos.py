'''

TDD - Test Drive Development ( Desenvolvimetno dirigido a testes)


Red
    Parte 1 -> Criar o teste e ver falhar

Green
    Parte 2 -> Criar o codigo e ver o teste passar

Refactor
    Parte 3 -> Melhorar o codigo
'''
from Testes.baconcomovos import bacon_com_ovos
import unittest

class TestBaconComOvos(unittest.TestCase):

    def test_bacon_com_ovos_deve_levantar_assertionerror_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15,30,45,60)
        saidas = 'Bacon com Ovos'
        for entrada in entradas:
            with self.subTest(entrada= entrada, saida = saidas):
                self.assertEqual(bacon_com_ovos(entrada),saidas,msg=f'Entrada não retornou a saida {saidas}')

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1,2,4,7,8)
        saidas = 'Passar Fome'

        for entrada in entradas:
            with self.subTest(entrada= entrada, saida = saidas):
                self.assertEqual(bacon_com_ovos(entrada),saidas,msg=f'Entrada não retornou a saida {saidas}')

    def test_bacon_com_ovos_deve_retornar_bacon_se_for_multiplo_de_3(self):
        entradas = (3,6,9,12)
        saidas = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada= entrada, saida = saidas):
                self.assertEqual(bacon_com_ovos(entrada),saidas,msg=f'Entrada não retornou a saida {saidas}')

    def test_bacon_com_ovos_deve_retornar_bacon_se_for_multiplo_de_5(self):
        entradas = (5,10,20,25,35)
        saidas = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada= entrada, saida = saidas):
                self.assertEqual(bacon_com_ovos(entrada),saidas,msg=f'Entrada não retornou a saida {saidas}')


if __name__ == '__main__':
    unittest.main(verbosity=2)