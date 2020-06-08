from Testes.calculadora import *
import unittest


class TestCalculadora(unittest.TestCase):
    def test_soma_entre_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_entre_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5,5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10,10,20),
            (10,5,15),
            (100,100,200),
            (-1.5,-1.5,-3.0),
            (1.5,1.5,3.0),
                      )

        for somas in x_y_saidas:
            with self.subTest(somas=somas):
                x, y ,saida = somas
                self.assertEqual(soma(x, y), saida)


    def test_sum_x_not_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('10',10)

    def test_sum_y_not_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(10,'10')

    def test_minus_between_5_and_5_return_0(self):
        self.assertEqual(subtrai(5,5), 0)

    def test_minus_between_6_negative_and_6_return_0(self):
        with self.subTest(error_on_subtraction= subtrai(-6,-6)):
            self.assertEqual(subtrai(-6,-6), 0)

    def test_x_not_int_or_float_return_assertionerror(self):
        x_y_outs = [
            (10,10,0),
            (10,20,-10),
            (100,10,90),
            (25,50,-25),
            (-10,10,-20),
            (-1.5,1.0,-2.5),
                    ]
        for calc in x_y_outs:
            x,y,out= calc
            with self.subTest(error_on_calcs=calc):
                self.assertEqual(subtrai(x,y),out)

if __name__ == '__main__':
    unittest.main(verbosity=2)
