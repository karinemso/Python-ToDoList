from funções import validacoes as vd


def titulo(msg):
    tam = len(msg)+2
    print('-'*tam)
    print(f' {msg}')
    print('-'*tam)

def linha(t=20):
    print('-'*t)


def ações(op, tarefas):
    if len(tarefas) == 0:
        if op == 1:
                tf = vd.leiaTarefa('Digite a tarefa que deseja adicionar: ')
                tarefas.append(tf)   
    else:
        if op == 1:
            tf = vd.leiaTarefa('Digite a tarefa que deseja adicionar: ')
            tarefas.append(tf)
        elif op == 2:
            qual = vd.leiaIndice('Qual o número da tarefa que deseja editar? ', tarefas)
            editada = vd.leiaTarefa('Reescreva sua tarefa: ')
            tarefas[qual] = editada
        elif op == 3:
            qual = vd.leiaInt('Qual o número da tarefa que deseja concluir? ')
            vd.tarefaStatus(tarefas, qual)
        elif op == 4:
            qual = vd.leiaInt('Qual o número da tarefa que deseja excluir? ')
            tarefas.remove(tarefas[qual])
  

def menu(tarefas):
    while True:
        titulo('Menu')
        if len(tarefas) == 0:
            print('''1-Adicione uma tarefa\n2-Sair do Sistema''')
            op =  vd.leiaOp('Digite sua opção: ')
            ações(op,tarefas)
            if op == 2:
                break
        else:
            titulo('Minha Lista')
            for c,t in enumerate(tarefas):
                print(f'{c} - {t}')
            linha()
            print('''1-Adicione uma tarefa\n2-Edite uma tarefa\n3-Conclua uma tarefa\n4-Exclua uma tarefa\n5-Sair do sistema''')
            linha()
            op = vd.leiaOp('Digite sua opção: ')
            ações(op,tarefas)
            if op == 5:
                break
           
            

                    
       
        