import sqlite3
import os
import sys
import unidecode


inputBanco = input('digite o nome do banco de dados desejado : ')
inputNome = input('digite o nome do usuário: ')
inputSenha = input('digite a senha:')
inputEmail = input('digite o seu e-mail:')

inputBanco = unidecode.unidecode(inputBanco)
inputNome = unidecode.unidecode(inputNome)
inputEmail = unidecode.unidecode(inputEmail)

try:
    inputBanco = str(inputBanco)
    inputNome = str(inputNome)
    inputSenha = int(inputSenha)
    inputEmail = str(inputEmail)
    if '@' and '.com' not in inputEmail:
        print('email inválido, favor verifique...')
        sys.exit(2)
    else:
        pass

except:
    print('erro: a senha deve ser composta apenas por números"')
    sys.exit(2)


criacao_banco = sqlite3.connect(f'{inputBanco}.db'.format(inputBanco))
cursor = criacao_banco.cursor()

criar_tables =f'''
CREATE TABLE IF NOT EXISTS USU (
    nome varchar(50),
    senha varchar(50),
    email varchar(100)
)
'''
cursor.execute(criar_tables)
select = '''
INSERT INTO USU(nome, senha, email)
VALUES (?, ?, ?)
'''

cursor.execute(select, (inputNome, inputSenha, inputEmail))
busca ='''
SELECT * FROM USU
'''
cursor.execute(busca)
resultado = cursor.fetchall()
for linha in resultado:
    list(linha)
    nome = linha[0]
    senha = linha[1]
    email = linha[2]
    print('o nome do usuário é : "{}", com sua respectiva senha : "{}",e email : "{}" no banco de dados : "{}"'.format(nome, senha, email, inputBanco))
    # print("o nome de usuário é: '{}', a senha é: '{}', e o email é '{}' o banco criado é '{}' .".format(nome, senha, email, inputBanco))


if os.path.exists(f'{inputBanco}.db'.format(inputBanco)):
    os.remove(f'{inputBanco}.db'.format(inputBanco))
    print(f'{inputBanco}.db foi removido!'.format(inputBanco))
else:
    print('erro ao tentar excluir ;-;')
    exit()

cursor.close()
criacao_banco.commit()

criacao_banco.close()
