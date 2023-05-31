import unittest
import os
from unittest.mock import patch
from main import *

class TesteCadastro(unittest.TestCase):

    def setUp(self) -> None:
        os.remove('usuarios')

    # Cadastrar > Usuario > Senha > Sair
    @patch('getpass.getpass', lambda *args: 'senha')
    def test_menu(self):
        inputs = iter([
            '1',
            'username',
            '3',
        ])
        with patch('builtins.input', lambda *args: next(inputs)):
            menu()


class TesteEntrar(unittest.TestCase):

    def setUp(self) -> None:
        try:
            os.remove('usuarios')
        except:
            pass
        cadastrar_usuario('username','senha')

    # Entrar > Usuario > Senha > Sair
    @patch('getpass.getpass', lambda *args: 'senha')
    def test_menu(self):
        inputs = iter([
            '2',
            'username',
            '1',
            '3'
        ])
        with patch('builtins.input', lambda *args: next(inputs)):
            menu()


# class TesteCadastrarComUsuarioExistente(unittest.TestCase):

#     def setUp(self) -> None:
#         try:
#             os.remove('usuarios')
#         except:
#             pass
#         cadastrar_usuario('username','senha')

#     # Entrar > Usuario > Senha > Sair
#     @patch('getpass.getpass', lambda *args: 'senha')
#     def test_menu(self):
#         inputs = iter([
#             '1',
#             'username',
#             '3'
#         ])
#         with patch('builtins.input', lambda *args: next(inputs)):
#             menu()

        