def leiaTarefa(msg):
    tf = input(msg)
    while True:
        if tf == '':
            tf = input(msg)
        else:
            break
    return str(tf)


def leiaInt(msg):
    num = input(msg)
    while True:
        if num.isnumeric() == True:
            break
        else:
            num = input(msg)
    return int(num)

def leiaOp(msg):
    num = input(msg)
    while True:
        if num in '12345' and num.isnumeric() == True:
            break
        else:
            num = input(msg)
    return int(num)

def leiaIndice(msg,tarefas):
    num = input(msg)
    while True:
        if num.isnumeric() == True and int(num) < len(tarefas):
            break
        else:
            num = input(msg)
    return int(num)

def tarefaStatus(tarefas,qual):
    if '\033[m' not in tarefas[qual]:
        editada = '\033[32m'+tarefas[qual]+'\033[m'
        tarefas[qual] = editada
    else:
        print('Essa tarefa já foi concluída!')   