def func_incluir(bd):
    id = input('Id do novo contato: ')
    nome = input('Nome do novo contato: ')
    email = input('E-Mail do novo contato: ')
    bd[id] = {'nome':nome,'email':email}
    print(f'{id} {nome} incluído com sucesso')

def func_excluir(bd):
    id = input('Id do contato a ser excluído: ')
    if id in bd.keys():
        del bd[id]
    else:
        print('Essa chave não existe')
    print(f'{id} excluído com sucesso')

def func_consultar_um(bd):
    id = input('Id do contato a ser consultado: ')
    if id in bd.keys():
        print(f'ID: {id}')
        print('NOME:',bd[id]['nome'])
        print('E-MAIL',bd[id]['email'])
    else:
        print('Essa chave não existe')
    print(f'Consulta executada com sucesso')

def func_consultar_todos(bd):
    for ident in bd:
        print(f'ID: {ident}')
        print('NOME:',bd[ident]['nome'])
        print('E-MAIL',bd[ident]['email'])
        print('----------------------------')
    print(f'Consulta executada com sucesso')

def func_alterar(bd):
    id = input('Id do contato a ser alterado: ')
    a = input(f'ID: {id} séra aleterado. Você deseja alterar nome, email ou ambos?(responda [nome, email ou ambos] ).  ')
    #COLOCAR A CHAVE QUE QUER ALTERAR APOS A ID
    if id in bd.keys():
        if a == 'nome':
           print(f'ID: {id} tera nome aleterado')
           nome = input('Novo nome: ')
           bd[id]['nome'] = nome
        elif a == 'email':
            print(f'ID: {id} tera o email alterado')
            email =  input('Novo email: ')
            bd[id]['email'] = email
        elif a == 'ambos':
            print(f'ID: {id} sera aletrado')
            nome = input('Novo nome: ')
            email = input('Novo email: ')
            bd[id]= {'nome':nome, 'email':email}
    else:
        print('Essa chave não existe')
    print('Alteração executada com sucesso')

def func_delete(bd):
    id = input('Id do contato a ser alterado: ')
    if id in bd.keys():
        print(f'ID: {id} séra deletado')
        dados.pop(id)
    else:
        print('Essa chave não existe')
    print('Operação executada com sucesso')

dados = {
    '1':{'nome':'fulano','email':'ful@qq.com'},
    '2':{'nome':'beltrano','email':'bb@qq.com'}
}

while True:
    print('''
        ==============================
        CONTATOS
        ==============================
        1. Incluir contato
        2. Excluir contato
        3. Consultar UM contato
        4. Consultar TODOS os contatos
        5. Encerrar aplicação
        6. Alterar contato
        ==============================
          ''')
    op = input('Informe a operação desejada: ')
    if op == '5':
        print('Aplicação encerrada')
        break
    elif op == '1':
        func_incluir(dados)
    elif op == '2':
        func_excluir(dados)
    elif op == '3':
        func_consultar_um(dados)
    elif op == '4':
        func_consultar_todos(dados)
    elif op == '6':
        func_alterar(dados)
    elif op == '7':
        func_delete(dados)
    else:
        print('Opção inválida')


print('fim')