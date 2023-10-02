menu = {
    1:{'nome':'Dias','email':'dias@bol.com','tipo':'Atacadista','desconto': 25},
    2:{'nome':'Olly','email':'Olly@bol.com','tipo':'Varejista','desconto': 15}

    
}





def func_nome():
    id       = input('Id  do  contato: ')
    nome     = input('Nome do contato: ')
    email  = input('E-Mail do contato: ')
    tipo      = input('Informe o tipo: ')
    desconto      = input('O desconto: ')
    menu[id] = {'nome':nome,'email':email,'tipo':tipo,'desconto':desconto}
    return(f'{id} {nome} incluído com sucesso')
    
def func_alterar():
    id = input('Id do contado para alterar: ')
    
    nome = input('Digite o novo nome: ')
    email    = input('Digite o email:')
    tipo     = input('Informe o tipo: ')
    desconto     = input('O desconto: ')
    menu[id] = {'nome':nome,'email':email,'tipo':tipo,'desconto':int(desconto)}

def func_excluir():
   id = input('Id do contato a ser excluído: ')
   resposta = cliente(id)
   print(resposta)

   
 
def func_consulta_Todos():
    pass
def func_consulta_Um():
    pass
def func_consulta_desconto():
    pass
def cliente(id):
    try:
      return f'''   nome: {menu[id]['nome']}
                    email: {menu[id]['email']}
                    tipo: {menu[id]['tipo']}
                    desconto: {menu[id]['desconto']}%
        '''
    except:
        return '[ERRO]'

def func_Backup():
    pass

def func_restaurar():
    pass
