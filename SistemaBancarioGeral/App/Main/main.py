from App.repositories.repositorio import Repositorio
from App.services.servicos import Servico
from App.Controller.controller import Controller
from App.View.view import ObtemDados


repositorio = Repositorio()

servico = Servico(repositorio)

view = ObtemDados()

controller = Controller(servico, view)

controller.criar_conta()