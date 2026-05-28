from Model.model import Banco
from View.view import ObtemDados
from Controller.controller import Controller

banco = Banco()

view = ObtemDados()

controller = Controller(banco, view)

controller.criar_conta()