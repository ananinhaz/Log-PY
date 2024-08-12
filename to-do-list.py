import logging


logging.basicConfig(
    filename='todo.log',  
    level=logging.INFO,   
    format='%(asctime)s - %(levelname)s - %(message)s'  )

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        logging.info(f'Tarefa adicionada: {task}')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            logging.info(f'Tarefa removida: {task}')
        else:
            logging.warning(f'Tentativa de remover tarefa não existente: {task}')

    def list_tasks(self):
        logging.info('Listando tarefas.')
        if not self.tasks:
            logging.info('Nenhuma tarefa na lista.')
        for i, task in enumerate(self.tasks, start=1):
            print(f'{i}. {task}')

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            task = input("Digite a tarefa: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task = input("Digite a tarefa a ser removida: ")
            todo_list.remove_task(task)
        elif choice == '4':
            logging.info('Encerrando o programa.')
            print("Saindo...")
            break
        else:
            logging.warning(f'Opção inválida selecionada: {choice}')
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
