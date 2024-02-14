class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Tarefa "{task}" adicionada à lista.')

    def show_tasks(self):
        if not self.tasks:
            print('Nenhuma tarefa na lista.')
        else:
            print('Lista de Tarefas:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

def main():
    todo_list = TodoList()

    while True:
        print('\nEscolha uma opção:')
        print('1. Adicionar tarefa')
        print('2. Mostrar tarefas')
        print('3. Sair')

        choice = input('Digite o número da opção desejada: ')

        if choice == '1':
            task = input('Digite a tarefa a ser adicionada: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
        elif choice == '3':
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida. Por favor, escolha novamente.')

if __name__ == "__main__":
    main()