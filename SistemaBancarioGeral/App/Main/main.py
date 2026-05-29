from app.repositories.repositorio import Repositorio
from app.services.servicos import Servico
from app.Controller.controller import Controller
from app.View.view import ObtemDados


repositorio = Repositorio()

servico = Servico(repositorio)

view = ObtemDados()

controller = Controller(servico, view)

controller.criar_conta()