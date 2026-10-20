import json
import os

class TarefaInvalida(Exception): pass
class NomeInvalido(TarefaInvalida): pass
class NomeRepetido(TarefaInvalida): pass
class ListaVazia(TarefaInvalida): pass

class Tarefas:
    def __init__(self):
        self.lista = self.carregar_tarefas()
    def adicionar_tarefa(self, nome: str, concluido = False):
        if not isinstance(nome, str) or len(nome) < 4:
            raise NomeInvalido("Nome de tarefa inválido!")
        if not any(l.isalpha() for l in nome):
            raise NomeInvalido("Nome de tarefa inválido!")
        for tarefa in self.lista:
            if nome.lower() == tarefa['nome'].lower():
                raise NomeRepetido("Tarefa já existente!")
        self.lista.append({"nome": nome, "concluido": concluido})
        self.salvar_tarefas()
    def listar_tarefas(self):
        self.lista = self.carregar_tarefas()
        if not self.lista:
            raise ListaVazia("Nenhuma tarefa adicionada!")
        for i, tarefa in enumerate(self.lista, start=1):
            print(f"{i}. {tarefa['nome']} - Conclusão: {tarefa['concluido']}")
    def concluir_tarefa(self, nome: str):
        self.lista = self.carregar_tarefas()
        if not self.lista:
            raise ListaVazia("Nenhuma tarefa adicionada!")
        for tarefa in self.lista:
            if nome.lower() == tarefa['nome'].lower() and tarefa['concluido'] == False:
                tarefa['concluido'] = True
                print(f"{tarefa['nome']} concluído!")
                self.salvar_tarefas()
                return 
        print("Tarefa não-existente!")
    def excluir_tarefa(self, nome: str):
        self.lista = self.carregar_tarefas()
        if not self.lista:
            raise ListaVazia("Nenhuma tarefa adicionada!")
        for tarefa in self.lista:
            if nome.lower() == tarefa['nome'].lower():
                print(f"{tarefa['nome']} foi removido!")
                self.lista.remove(tarefa)
                self.salvar_tarefas()
                return
        print("Tarefa não-existente!")
    def salvar_tarefas(self):
        with open('tarefas.json', 'w', encoding='utf-8') as a:
            json.dump(self.lista, a, indent=4, ensure_ascii=False)
    def carregar_tarefas(self):
        if not os.path.exists('tarefas.json'):
            return []
        try:
            with open('tarefas.json', 'r', encoding='utf-8') as a:
                return json.load(a)
        except json.JSONDecodeError as e:
            print(f"Erro: {e}")
            return []