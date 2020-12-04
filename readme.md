# Comecta | Projeto Final de Banco de Dados | 2020.1

## O que é

Comecta foi o nome que resolvemos dar a interface de interação com o usuário de nosso projeto. Como o objetivo da ferramenta para a qual desenvolvemos o banco de dados é informar tanto aos usuários quanto aos donos de estabelecimentos como está a situação dos lugares em relação a quantidade de pessoas e preocupações com aglomerações desnecessárias, o nome veio da pergunta "Como é que está?", que ao ser falada rapidamente pode soar como "Coméqtá", que foi transformado para "Comecta". 

## Como navegar pela interface

Na página inicial da interface encontram-se quatro botões, cada qual referente a umas das opreações CRUD que são possíveis de se realizar em nosso banco de dados. após selecionar qual operação se deseja realizar, o usuário então escolhe em qual das entidades ele deseja realizar tal operação. Nas operações de criar, atualizar e deletar dados são dadas três opções de tabelas que podem ser alteradas, todas elas possuem relações entre si. Já a operação de buscar e ler dados do banco de dados possui uma opção a mais: ao clicar no botão 
"lojas por perto", aparecerá na tela uma lista dos estabelecimentos próximos ao usuário selecionado a partir do dropdown, tal tabela foi gerada a partir da implementação de views. 

## Como executar o código

Para executar o código é necessário ter o Pyhton instalado em seu computador, junto com as bibliotecas Dash (pip install dash) e e MySQL.Connector (pip install mysql-connector-python).

Para criar o banco de dados, primeiro utilize os códigos presentes na pasta "mysql". Primeiro crie o banco de dados e suas tabales rodando o código "". Depois insira as instâncias rodando o código "". As partes referentes as implementações da View e da Procedure então presente no final do segundo código mencionado.

Para rodar a interface de interação com o usuário, basta rodar o comando "python app.py" no terminal, diretamente na pasta onde se encontram os arquivos presentes neste repositório. 

## View

## Procedure
