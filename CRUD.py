# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:38:57 2020

@author: Marco Antonio Garcia e Tatiana Pereira
"""
import mysql.connector
import numpy as np
from datetime import date, datetime, timedelta
pas = '@Adm17015'
cnx = mysql.connector.connect(user='root',password= pas , host='127.0.0.1', port=3306 ,database='mydb')
curso = cnx.cursor()

SQL_create_usuario = "INSERT INTO `mydb`.`usuário` (`Email`, `Nome`, `Senha`, `Local_Código`) VALUES "
SQL_read_usuario = "SELECT * FROM `mydb`.`usuário`"
SQL_update_usuario = "UPDATE `mydb`.`usuário` SET "
SQL_delete_usuario = "DELETE FROM `mydb`.`usuário` WHERE `Email` = "


SQL_create_local = "INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES"
SQL_read_local = "SELECT * FROM `mydb`.`local`"
SQL_update_local = "UPDATE `mydb`.`local` SET "
SQL_delete_local = "DELETE FROM `mydb`.`local` WHERE `Código` = "

SQL_create_estabelecimento = "INSERT INTO `mydb`.`estabelecimento` (`Código`, `Nome`, `Descrição`, `Tempo_Medio_Atendimento`, `Local_Código`) VALUES "
SQL_read_estabelecimento = "SELECT * FROM `mydb`.`estabelecimento` "
SQL_update_estabelecimento = "UPDATE `mydb`.`estabelecimento` SET "
SQL_delete_estabelecimento = "DELETE FROM `mydb`.`estabelecimento` WHERE `Código` = "

SQL_create_avaliacao = "INSERT INTO `mydb`.`avaliação` (`Horário`, `Comentário`, `Nota`, `Usuário_Email`, `Estabelecimento_Código`) VALUES "
SQL_read_avaliacao = "SELECT * FROM `mydb`.`avaliação`"
SQL_update_avaliacao = "UPDATE `mydb`.`avaliação` SET "
SQL_delete_avaliacao = "DELETE FROM `mydb`.`avaliação` WHERE `Usuário_Email` = "

SQL_read_view = "SELECT * FROM est_perto_lotacao WHERE Usuario like "

# Funções auxiliares para as funções principais:

def transforma_certo(nome):
    nome_certo = '\'' + nome + '\''
    return nome_certo

# -----------------------------
# Funções para o CRUD de Local;
# -----------------------------

def create_local(codigo, bairro, complemento):
    codigo = transforma_certo(str(codigo))
    bairro = transforma_certo(bairro)
    complemento = transforma_certo(complemento)
    valores = '(' + codigo + ', ' + bairro + ', ' + complemento + ')'
    SQL_certo = SQL_create_local + valores
    try: 
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def read_local(codigo):
    codigo_certo = transforma_certo(str(codigo))
    onde = ' WHERE `Código` = ' + codigo_certo
    SQL_certo = SQL_read_local + onde

    try:
        curso.execute(SQL_certo)
        result = curso.fetchall()
        return result
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def update_local(bairro, complemento, codigo):
    bairro = transforma_certo(bairro)
    complemento = transforma_certo(complemento)
    codigo = str(codigo)
    valores = '`Bairro` = ' + bairro + ', ' + '`Complemento` = ' + complemento
    onde = ' WHERE `Código` = ' + codigo
    SQL_certo = SQL_update_local + valores + onde
    try: 
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def delete_local(codigo):
    codigo = transforma_certo(str(codigo))
    SQL_certo = SQL_delete_local + codigo
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)



# -------------------------------
# Funções para o CRUD do usuario;
# -------------------------------
    
def create_usuario(email, nome, senha, local_codigo):
    email_certo = transforma_certo(email)
    nome_certo = transforma_certo(nome)
    senha_certo = transforma_certo(senha)
    local_codigo = str(local_codigo)
    valores = '(' + email_certo + ', ' + nome_certo + ', ' + senha_certo + ', ' + local_codigo + ')'
    SQL_certo = SQL_create_usuario + valores
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)
     
def read_usuario():
    try:
        curso.execute(SQL_read_usuario)
        result = curso.fetchall()
        return result

    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def read_usuario_especifico(email):
    email_certo = transforma_certo(email)
    onde = ' WHERE `Email` = ' + email_certo
    SQL_certo = SQL_read_usuario + onde
    try:
        curso.execute(SQL_certo)
        result = curso.fetchall()
        return result

    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def update_usuario(nome, senha, email):
    nome = transforma_certo(nome)
    senha = transforma_certo(senha)
    email = transforma_certo(email)
    valores = '`Nome` = ' + nome + ', ' + '`Senha` = ' + senha 
    onde = ' WHERE `Email` = ' + email
    SQL_certo = SQL_update_usuario + valores + onde
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def delete_usuario(email):
    SQL_certo = SQL_delete_usuario + transforma_certo(email)
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)
    
# -----------------------------------
# Funcoes para o CRUD das avaliações;
# -----------------------------------
    
def create_avaliacao(comentario, nota, user_email, est_codigo):
    horario = datetime.now()
    horas_apenas = horario.strftime('%H:%M:%S')
    horario_certo = transforma_certo(horas_apenas)
    coment_certo = transforma_certo(comentario)
    nota_certa = transforma_certo(str(nota))
    user_email_certo = transforma_certo(user_email)
    est_codigo_certo = transforma_certo(str(est_codigo))
    valores = '(' + horario_certo + ', ' + coment_certo + ', ' + nota_certa + ', ' + user_email_certo + ', ' + est_codigo_certo + ')' 
    SQL_certo = SQL_create_avaliacao + valores
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def read_avaliacao():
    try: 
        curso.execute(SQL_read_avaliacao)
        result = curso.fetchall()
        return result
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def read_avaliacao_especifico(email, est_codigo):
    email = transforma_certo(email)
    est_codigo = str(est_codigo)
    onde = ' WHERE `Usuário_email` = ' + email + ' AND `Estabelecimento_Código` = ' + est_codigo
    SQL_certo = SQL_read_avaliacao + onde
    try: 
        curso.execute(SQL_certo)
        result = curso.fetchall()
        return result
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)
       
def update_avaliacao(comentario, nota, email, est_codigo):
    comentario = transforma_certo(comentario)
    nota = transforma_certo(str(nota))
    email = transforma_certo(email)
    est_codigo = str(est_codigo)
    valores = '`Comentário` = ' + comentario + ', ' + '`Nota` = ' + nota
    onde = ' WHERE `Usuário_email` = ' + email + ' AND `Estabelecimento_Código` = ' + est_codigo
    SQL_certo = SQL_update_avaliacao + valores + onde
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def delete_avaliacao(email, codigo):
    email = transforma_certo(email)
    codigo = transforma_certo(str(codigo))
    valores = email +' AND ' +' `Estabelecimento_Código` = ' + codigo
    SQL_certo = SQL_delete_avaliacao + valores
    try: 
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)


# ---------------------------------------
# Funcoes para o CRUD do estabelecimento;
# ---------------------------------------

    
def create_estabelecimento(codigo, nome, descricao, tempo, local_codigo):
    codigo_certo = str(codigo)
    nome_certo = transforma_certo(nome)
    descricao_certo = transforma_certo(descricao)
    tempo_certo = transforma_certo('0' + str(timedelta(minutes=tempo)))
    local_codigo_certo = transforma_certo(str(local_codigo))
    valores = '(' + codigo_certo + ', ' + nome_certo + ', ' + descricao_certo + ', ' + tempo_certo + ', ' + local_codigo_certo + ')'
    SQL_certo = SQL_create_estabelecimento + valores
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)
        
def read_estabelecimento():
    try:
        curso.execute(SQL_read_estabelecimento)
        result = curso.fetchall()
        return result
    
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def read_estabelecimento_especifico(codigo):
    codigo = str(codigo)
    onde = ' WHERE `Código` = ' + codigo
    SQL_certo = SQL_read_estabelecimento + onde
    try:
        curso.execute(SQL_certo)
        result = curso.fetchall()
        return result
    
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def update_estabelecimento(nome, descricao , tempo, codigo):
    nome = transforma_certo(nome)
    descricao = transforma_certo(descricao)
    tempo = transforma_certo('0' + str(timedelta(minutes=int(tempo))))
    codigo = str(codigo)
    valores = '`Nome` = ' + nome + ', ' + '`Descrição` = ' + descricao + ', ' + '`Tempo_Medio_Atendimento` = ' + tempo
    onde = ' WHERE `Código` = ' + codigo
    SQL_certo = SQL_update_estabelecimento + valores + onde
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "Banco de Dados foi atualizado com sucesso"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def delete_estabelecimento(codigo):
    codigo = str(codigo)
    SQL_certo = SQL_delete_estabelecimento + codigo 
    try:
        curso.execute(SQL_certo)
        cnx.commit()
        return "teste"
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)



# ---------------------------------------
# Funções para a VIEW e a PROCEDURE;
# ---------------------------------------

def read_view(email):
    SQL_read_view = "SELECT DISTINCT estabelecimento as Loja, `Tamanho/nível` as `Nível da Lotação` FROM est_perto_lotacao"
    onde = " WHERE `Email` = " + transforma_certo(email)
    SQL_certo = SQL_read_view + onde
    try:
        curso.execute(SQL_certo)
        result = curso.fetchall()
        return result
    except mysql.connector.Error as err:
        return "Something went wrong: {}".format(err)

def use_procedure(complemento): 
    args = [complemento, 0]
    result_args = curso.callproc('existe_local',args)
    return result_args[1]

def total_elementos(): 
    SQL_consulta = "SELECT MAX(Código) FROM  `mydb`.`local`"
    curso.execute(SQL_consulta)
    result = curso.fetchall()
    return result[0][0]

def total_elementos2(): 
    SQL_consulta = "SELECT MAX(Código) FROM  `mydb`.`estabelecimento`"
    curso.execute(SQL_consulta)
    result = curso.fetchall()
    return result[0][0]

def verifica_procedure(bairro,complemento):
    indice = use_procedure(complemento)
    total = total_elementos()
    if indice > total:
        create_local(indice, bairro, complemento)
        return indice
    else:
        return indice
    

'''
dicio = {"Email":"", "Nome":"", "Senha":"", "Código_Local":""}
user_dict = []   
user = read_usuario()
j = 0
while j<len(user):
    user_dict.append(dicio)
    j +=1
i = 0
while i < len(user):
    temp = dicio
    temp["Email"] = user[i][0]
    temp["Nome"] = user[i][1]
    temp["Senha"] = user[i][2]
    temp["Código_Local"] = user[i][3]
    user_dict[i] = temp
    print(dicio)       
    print(i)
    print(user_dict)
    i = i + 1'''
'''
dicio = {"Email":"", "Nome":"", "Senha":"", "Código_Local":""}
user_dict = []
user = read_usuario()
j = 0
for i in user:
    dicio["Email"] = user[j][0]
    dicio["Nome"] = user[j][1]
    dicio["Senha"] = user[j][2]
    dicio["Código_Local"] = user[j][3]
                
    user_dict.append(dicio.copy())
    j = j + 1
print(user_dict)

loja = read_estabelecimento_especifico("1")
nome = loja[0][1]
descricao = loja[0][2]
tempo = str(loja[0][3]) 

print(nome)
print(descricao)
print(type(tempo))
'''
print(read_view("tati@gmail.com"))