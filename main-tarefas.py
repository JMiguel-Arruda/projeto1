class RespostaInvalida(Exception): pass
from gerenciador_de_tarefas import Tarefas, TarefaInvalida
def main():
    minha_lista = Tarefas()
    while True:
        try: 
            print("GERENCIADOR DE TAREFAS")
            print("1. ADICIONAR TAREFA")
            print("2. LISTAR TAREFAS")
            print("3. CONCLUIR TAREFA")
            print("4. EXCLUIR TAREFA")
            print("5. FECHAR PROGRAMA")
            resp = input("Digite aqui: ")
            if not isinstance(resp, str) or not any(n in"12345" for n in resp):
                raise RespostaInvalida("Digite uma resposta válida!")
            if resp == "1":
                minha_lista.adicionar_tarefa(nome = input("Nome da tarefa: "))
            elif resp == "2":
                minha_lista.listar_tarefas()
            elif resp == "3":
                minha_lista.concluir_tarefa(nome = input("Nome da tarefa: "))
            elif resp == "4":
                minha_lista.excluir_tarefa(nome = input("Nome da tarefa: "))
            elif resp == "5":
                print("Fechando...")
                break
            else:
                print("Entrada inválida!")
                break
        except TarefaInvalida as e:
            print(f"Erro: {e}")     
if __name__ == "__main__":
    main()
