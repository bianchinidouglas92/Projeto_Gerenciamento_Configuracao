# Projeto: Gerenciamento de Configuração
# Nova funcionalidade: Controle de tarefas

def cadastrar_tarefa():
    tarefa = input("Digite o nome da tarefa: ")
    print("Tarefa cadastrada com sucesso!")
    print("Tarefa:", tarefa)


def main():
    print("Sistema de Gerenciamento de Tarefas")
    cadastrar_tarefa()


if __name__ == "__main__":
    main()