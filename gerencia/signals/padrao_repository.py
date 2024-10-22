from ..models import Aluno

class PadraoRepository:
    @staticmethod
    def get_by_id(id):
        return Aluno.objects.get(pk=id)
    
    @staticmethod
    def get_all():
        return Aluno.objects.all()
    
    @staticmethod
    def find_by_name(name):
        return Aluno.objects.filter(nome=name) 

    @staticmethod
    def update_alunos_treino(dias_treino):
        return Aluno.objects.update(dias_treino=dias_treino)
