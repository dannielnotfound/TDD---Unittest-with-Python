from dataclasses import dataclass, asdict
import getpass, hashlib, json


@dataclass
class Usuario:
  user: str
  senha: str

def menu_usuario():
  while True:
    print('1 - Sair')
    print('2 - Voltar')
    menu_usuario = int(input())
    if menu_usuario == 1:
      break
    if menu_usuario == 2:
      __init()

def app(usuario):
  print('')
  print(f"Você está logado e autenticado como {usuario}, tendo permissões e acesso a serviços deste software.")
  print('')
  menu_usuario()


def criptografar_senha_sha256(senha):
  hash_sha256 = hashlib.sha256()
  hash_sha256.update(senha.encode('utf8'))
  return hash_sha256.hexdigest()

def grava_usuarios(lista_usuarios):
  list_dict = list(map(asdict,lista_usuarios))
  json_usuario = json.dumps(list_dict, indent=4)
  with open('usuarios', 'w+') as arquivo:
    arquivo.write(json_usuario)
  return True

def soma():
    pass

def cria_usuario(d):
  return Usuario(**d)

def cria_objeto_usuario(dicionario):
  usuarios_obj = list(map(lambda d : Usuario(**d), dicionario))
  return usuarios_obj

def ler_usuarios():
  try:
    with open('usuarios', 'r') as arquivo:
      json_usuarios = arquivo.read()
      list_dict = json.loads(json_usuarios)
      lista_usuarios = list(map(cria_usuario, list_dict))
      return lista_usuarios
  except:
      lista_usuarios = []
      with open('usuarios', 'w+') as arquivo:
        arquivo.write('\n')
        return lista_usuarios      
  
def retorna_dicionario_do_arquivo():
  try:
    with open('usuarios', 'r') as arquivo:
      json_usuarios = arquivo.read()
      dict_usuarios = json.loads(json_usuarios)
      return dict_usuarios
  except:
    with open('usuarios', 'w+') as arquivo:
        arquivo.write('\n')
        dict_usuarios = ''
        return dict_usuarios   


def cadastrar_usuario(username, senha):
    usuario = Usuario(username,criptografar_senha_sha256(senha))
    return grava_usuarios(ler_usuarios() + [ usuario])
    

def cadastrar():
  print('')
  print('UniLogin Cadastro')
  print('')
  usuario = input('Usuário: ')

  user_status = verifica_usuario(usuario)
  while(user_status):
    print(f'O usuário {usuario} já está em uso. Escolha outro nome de usuário.')
    usuario = input('Usuário: ')
    user_status = verifica_usuario(usuario)

  senha = getpass.getpass('Senha: ')

  
  if(cadastrar_usuario(usuario, senha)):
    print('\n')
    print(f"Usuário cadastrado com sucesso! ")
  else:
    print(f"Houve uma falha ao cadastrar novo usuário. ")

  print('\n')

def retorna_usuarios():
  users_dicionario = retorna_dicionario_do_arquivo()
  usuarios = cria_objeto_usuario(users_dicionario)
  return usuarios

def verifica_usuario(login_usuario):
  usuarios = retorna_usuarios()
  for usuario in usuarios:
    if(usuario.user == login_usuario):
      return True
      break
  return False

def verifica_senha(login_usuario, login_senha):
  usuarios = retorna_usuarios()
  for usuario in usuarios:
    if(usuario.senha == login_senha and usuario.user == login_usuario):
      return True
      break
  return False

def verifica_login(usuario, senha):
  user = verifica_usuario(usuario)
  senha = verifica_senha(usuario, senha)
  if(user == True and senha == True):
    return True
  else: 
    return False

def entrar():
  print('')
  print('UniLogin Entrar')
  print('')

  usuario = input('Usuario: ')
  senha = getpass.getpass('Senha: ')
  senha = criptografar_senha_sha256(senha)
  login = verifica_login(usuario, senha)

  if(login):
    app(usuario)
    
  else:
    print(f'Usuário ou senha inválidos.')
    print('\n')
    menu()


def menu():
  while True:
    print('Informe o número correspondente a sua escolha: ')
    print('1 - Cadastrar')
    print('2 - Entrar')
    print('3 - Sair')
    print('')

    while True:
      try:
        menu = int(input())
      except:
        print('')
        print('ERRO - Informe apenas números inteiros. ')
        print('Informe o número correspondente a sua escolha: ')
        print('1 - Cadastrar')
        print('2 - Entrar')
        print('3 - Sair')
        print('')
      else:
        break


    if(menu == 1):
      cadastrar()
    elif(menu == 2):
      entrar()
    elif(menu == 3):
      break
    else:
      print('')
      print('ERRO - Informe apenas números inteiros. ')
      print('')



def __init():
    print('')
    print('Bem vindo ao NUAPA')
    print('')

    menu()

if __name__ == '__main__':
    __init()
