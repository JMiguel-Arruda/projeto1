class TarefaInvalida(Exception): pass
class NomeInvalido(TarefaInvalida): pass
class NomeRepetido(TarefaInvalida): pass
class ListaVazia(TarefaInvalida): pass

class Tarefas:
    def __init__(self):
        self.lista = []
    def adicionar_tarefa(self, nome: str, concluido = False):
        if not isinstance(nome, str) or len(nome) < 4:
            raise NomeInvalido("Nome de tarefa inválido!")
        if not any(l.isalpha() for l in nome):
            raise NomeInvalido("Nome de tarefa inválido!")
        for tarefa in self.lista:
            if nome.lower() == tarefa['nome'].lower():
                raise NomeRepetido("Tarefa já existente!")
        self.lista.append({"nome": nome, "concluido": concluido})
    def listar_tarefas(self):
        if not self.lista:
            raise ListaVazia("Nenhuma tarefa adicionada!")
        for i, tarefa in enumerate(self.lista, start=1):
            print(f"{i}. {tarefa['nome']} - Conclusão: {tarefa['concluido']}")
    def concluir_tarefa(self, nome: str):
        if not self.lista:
            raise ListaVazia("Nenhuma tarefa adicionada!")
        for tarefa in self.lista:
            if nome.lower() == tarefa['nome'].lower() and tarefa['concluido'] == False:
                tarefa['concluido'] = True
                print(f"{tarefa['nome']} concluído!")
                return 
        print("Tarefa não-existente!")
    def excluir_tarefa(self, nome: str):
        if not self.lista:
            raise ListaVazia("Nenhuma tarefa adicionada!")
        for tarefa in self.lista:
            if nome.lower() == tarefa['nome'].lower():
                print(f"{tarefa['nome']} foi removido!")
                self.lista.remove(tarefa)
                return
        print("Tarefa não-existente!")
            
print("----------TESTES-----------")
minhas_tarefas = Tarefas()
minhas_tarefas.adicionar_tarefa("Fazer as compras")
minhas_tarefas.adicionar_tarefa("Lavar a louça")
minhas_tarefas.listar_tarefas()
minhas_tarefas.concluir_tarefa("Fazer as compras")
minhas_tarefas.listar_tarefas()
minhas_tarefas.excluir_tarefa("Fazer as compras")
minhas_tarefas.listar_tarefas()  
print("---------------------------")