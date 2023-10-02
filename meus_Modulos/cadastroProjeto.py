import menuefuncao as fc
while True:
    print('''
        --------------------------------
        CONTATOS
        --------------------------------
        1. Incluir contato
        2. Alterar dados
        3. Exluir contato
        4. Consultar TODOS os contatos
           4.1 Consultar Um
           4.2 Consulta Desconto
        5. Encerrar aplicação
        B. Backup

        --------------------------------
          ''')
    ordem = float(input('Informe a operação: '))
    if ordem == 1:
        fc.func_nome()
    elif ordem == 2:
        fc.func_alterar()
    elif ordem == 3:
        fc.func_excluir()
    elif ordem == 4:
        fc.func_consulta_Todos()
    elif ordem == 4.1:
        fc.func_consulta_Um()
    elif ordem == 4.2:
        fc.func_consulta_desconto()
    elif ordem == 'B':
        fc.func_Backup()
    elif ordem == 5:
        print('Programa encerrado.')
        break
    else:
        print('OPÇÃO INVALIDA')
