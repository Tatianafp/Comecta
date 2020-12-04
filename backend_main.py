import io
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd

from CRUD import create_local, read_local, update_local, delete_local, create_usuario, read_usuario, read_usuario_especifico, update_usuario, delete_usuario, create_avaliacao, read_avaliacao, read_avaliacao_especifico, update_avaliacao, delete_avaliacao, create_estabelecimento, read_estabelecimento, read_estabelecimento_especifico, update_estabelecimento, delete_estabelecimento,verifica_procedure, total_elementos2, read_view

html.H4('Algo deu errado. Tente novamente.', className='card-subtitle')
html.H4('Banco de Dados foi atualizado com sucesso', className='card-subtitle')

def create_layout(app):
    # Actual layout of the app
    return html.Div([
    html.Link(href="https://fonts.googleapis.com/css2?family=Raleway&display=swap", rel="stylesheet"),
    html.Div([
        html.Div(
            id = 'main_background',
            #className='card',
            children = [
                html.Div(id = 'base',
                    className='card',
                    children = [
                        html.Div(id = "titulo",
                            className = "titulo",
                            children = [
                                html.H1('COMECTA', className='card-title'), 
                                #html.Img(src='assets/img/github.png',className='github-img'),
                        ]),
                        html.Div(id = 'menu-principal',
                            className = 'menu',
                            children = [                              
                                html.Button(children=["create"], className="Button", id="create-button", n_clicks=0),
                                html.Button(children=["read"], className="Button", id="read-button", n_clicks=0),
                                html.Button(children=["update"], className="Button", id="update-button", n_clicks=0),
                                html.Button(children=["delete"], className="Button", id="delete-button", n_clicks=0),
                        ]),
                        html.Div(id = 'menu-entidades',
                            style = {"display": "none"},
                            className = 'menu',
                            children = [                              
                                html.Button(children=["usuário"], className="Button", id="usuario-button", n_clicks=0),
                                html.Button(children=["avaliação"], className="Button", id="avaliacao-button", n_clicks=0),
                                html.Button(children=["loja"], className="Button", id="loja-button", n_clicks=0),
                                #html.Button(children=["voltar"], className="Button", id="voltar0-button", n_clicks=0),
                        ]),
                        html.Div(id = 'menu-read',
                            style = {"display": "none"},
                            className = 'menu',
                            children = [                              
                                html.Button(children=["usuários"], className="Button", id="usuarios-button", n_clicks=0),
                                html.Button(children=["avaliações"], className="Button", id="avaliacoes-button", n_clicks=0),
                                html.Button(children=["lojas"], className="Button", id="lojas-button", n_clicks=0),
                                html.Button(children=["lojas por perto"], className="Button", id="view-button", n_clicks=0),        
                        ]),

                        # CREATE

                        html.Div(id = 'create-usuario-page',
                            style = {"display": "none"},
                            className = 'create',
                            children = [  
                                html.H4('Create Usuário', className='card-subtitle'),
                                html.H4('Email:', className='comando'),
                                dcc.Input(id='input-email-usuario', className="input", type='text'),
                                html.H4('Nome completo:', className='comando'),
                                dcc.Input(id='input-nome-usuario', className="input", type='text'),                            
                                html.H4('Senha:', className='comando'),
                                dcc.Input(id='input-senha-usuario', className="input", type='text'),
                                html.H4('Endereço:', className='comando'),
                                html.H4('-> Bairro:', className='comando'),
                                dcc.Input(id='input-bairro-usuario', className="input", type='text'),
                                html.H4('-> Complemento:', className='comando'),
                                dcc.Input(id='input-complemento-usuario', className="input", type='text'),

                                html.Button(children=["Enviar"], className="Button", id="enviar-create-usuario-button", n_clicks=0),
                                html.Div(id='result-create-usuario', style={"display":"none"}, className="card-output",),
                        ]),

                        html.Div(id = 'create-avaliacao-page',
                            style = {"display": "none"},
                            className = 'create',
                            children = [  
                                html.H4('Create Avaliação', className='card-subtitle'),
                                html.H4('Comentário:', className='comando'),
                                dcc.Input(id='input-comentario-avaliacao', className="input", type='text'),                            
                                html.H4('Nota:', className='comando'),
                                dcc.Slider(
                                    id='input-nota-avaliacao',
                                    min=1,
                                    max=5,
                                    marks={1:"1",2:"2",3:"3",4:"4",5:"5"},
                                    step=None,
                                    value=3,
                                ),
                                html.H4('Usuario:', className='comando'),
                                dcc.Dropdown(id='input-usuario-avaliacao', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "Jose Vinicius Garreto","value": "jose@gmail.com",},
                                        {"label": "Lucas Honda","value": "lucas@gmail.com",},
                                        {"label": "Marco Antonio Garcia","value": "marco@gmail.com",},
                                        {"label": "Plinio Mayer","value": "plinio@gmail.com",},
                                        {"label": "Tatiana Pereira","value": "tati@gmail.com",},
                                    ],
                                    placeholder="Selecione um usuario",
                                ),
                                html.H4('Loja:', className='comando'),
                                dcc.Dropdown(id='input-loja-avaliacao', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "1 - Farmacia Alegria","value": "1",},
                                        {"label": "2 - Volta ao Mundo","value": "2",},
                                        {"label": "3 - Banco Familia","value": "3",},
                                        {"label": "4 - Acai Mania","value": "4",},
                                        {"label": "5 - Academia Hercules","value": "5",},
                                    ],
                                    placeholder="Selecione uma loja",
                                ),

                                html.Button(children=["Enviar"], className="Button", id="enviar-create-avaliacao-button", n_clicks=0),
                                html.Div(id='result-create-avaliacao', style={"display":"none"}, className="card-output",),
                        ]),

                        html.Div(id = 'create-loja-page',
                            style = {"display": "none"},
                            className = 'create',
                            children = [  
                                html.H4('Create Loja', className='card-subtitle'),
                                html.H4('Nome:', className='comando'),
                                dcc.Input(id='input-nome-loja', className="input", type='text'),
                                html.H4('Descrição:', className='comando'),
                                dcc.Input(id='input-descricao-loja', className="input", type='text'),                            
                                html.H4('Tempo médio de atendimento:', className='comando'),
                                html.H5('(hh:mm:ss)', className='detalhe-comando'),
                                dcc.Input(id='input-tempo-loja', className="input", type='text'),
                                html.H4('Endereço:', className='comando'),
                                html.H4('-> Bairro:', className='comando'),
                                dcc.Input(id='input-bairro-loja', className="input", type='text'),
                                html.H4('-> Complemento:', className='comando'),
                                dcc.Input(id='input-complemento-loja', className="input", type='text'),

                                html.Button(children=["Enviar"], className="Button", id="enviar-create-loja-button", n_clicks=0),
                                html.Div(id='result-create-loja', style={"display":"none"}, className="card-output",),
                        ]),

                        # READ

                        html.Div(id = 'read-usuario-page',
                            style = {"display": "none"},
                            className = 'read',
                            children = [   
                                #html.H4('Digite o email do usuario:', className='comando'),
                                #dcc.Input(id='input-read-usuario', className="input", type='text'), 
                                html.H4('Read Usuários', className='card-subtitle'),
                                
                                html.Div(
                                    className='card-output',
                                    children = [html.Div(id = 'output-read-usuario'),]
                                )                           
                        ]),

                        html.Div(id = 'read-avaliacao-page',
                            style = {"display": "none"},
                            className = 'read',
                            children = [   
                                html.H4('Read Avaliações', className='card-subtitle'), 
                                
                                html.Div(
                                    className='card-output',
                                    children = [html.Div(id = 'output-read-avaliacao'),]
                                )                           
                        ]),

                        html.Div(id = 'read-loja-page',
                            style = {"display": "none"},
                            className = 'read',
                            children = [   
                                html.H4('Read Lojas', className='card-subtitle'),
                                html.Div(
                                    className='card-output',
                                    children = [html.Div(id = 'output-read-loja')]
                                )                           
                        ]),

                        html.Div(id = 'read-view-page',
                            style = {"display": "none"},
                            className = 'read',
                            children = [   
                                html.H4('Lojas por perto', className='card-subtitle'),
                                dcc.Dropdown(id='input-read-view', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "Jose Vinicius Garreto","value": "jose@gmail.com",},
                                        {"label": "Lucas Honda","value": "lucas@gmail.com",},
                                        {"label": "Marco Antonio Garcia","value": "marco@gmail.com",},
                                        {"label": "Plinio Mayer","value": "plinio@gmail.com",},
                                        {"label": "Tatiana Pereira","value": "tati@gmail.com",},
                                    ],
                                    placeholder="Selecione um usuario",
                                    value = "temp"
                                ), 
                                html.Div(
                                    className='card-output',
                                    children = [html.Div(id = 'output-read-view'),]
                                )                           
                        ]),

                        # UPDATE

                        html.Div(id = 'update-usuario-page',
                            style = {"display": "none"},
                            className = 'update',
                            children = [
                                html.H4('Update Usuário', className='card-subtitle'),
                                dcc.Dropdown(id='input-update-usuario', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "jose@gmail.com","value": "jose@gmail.com",},
                                        {"label": "lucas@gmail.com","value": "lucas@gmail.com",},
                                        {"label": "marco@gmail.com","value": "marco@gmail.com",},
                                        {"label": "plinio@gmail.com","value": "plinio@gmail.com",},
                                        {"label": "tati@gmail.com","value": "tati@gmail.com",},
                                    ],
                                    placeholder="Selecione o email do usuário",
                                ),
                                html.Button(children=["buscar"], className="Button", id="buscar-update-usuario", n_clicks=0),
                                html.Div(id = 'update-usuario-options',
                                    style = {"display": "none"},
                                    children = [
                                        html.H4('Nome completo:', className='comando'),
                                        dcc.Input(id='input-nome-usuario-update', className="input", type='text'),                            
                                        html.H4('Senha:', className='comando'),
                                        dcc.Input(id='input-senha-usuario-update', className="input", type='text'),
                                        html.Button(children=["enviar"], className="Button", id="enviar-update-usuario", n_clicks=0),
                                    ]
                                ),
                                html.Div(id='result-update-usuario', style={"display":"none"}, className="card-output",),
                        ]),
                        
                        html.Div(id = 'update-avaliacao-page',
                            style = {"display": "none"},
                            className = 'update',
                            children = [
                                html.H4('Update Avaliacao', className='card-subtitle'),
                                dcc.Dropdown(id='input-update-avaliacao1', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "jose@gmail.com","value": "jose@gmail.com",},
                                        {"label": "lucas@gmail.com","value": "lucas@gmail.com",},
                                        {"label": "marco@gmail.com","value": "marco@gmail.com",},
                                        {"label": "plinio@gmail.com","value": "plinio@gmail.com",},
                                        {"label": "tati@gmail.com","value": "tati@gmail.com",},
                                    ],
                                    placeholder="Selecione o email do usuário",
                                ),
                                dcc.Dropdown(id='input-update-avaliacao2', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "1 - Farmacia Alegria","value": "1",},
                                        {"label": "2 - Volta ao Mundo","value": "2",},
                                        {"label": "3 - Banco Familia","value": "3",},
                                        {"label": "4 - Acai Mania","value": "4",},
                                        {"label": "5 - Academia Hercules","value": "5",},
                                    ],
                                    placeholder="Selecione uma loja",
                                ),
                                html.Button(children=["buscar"], className="Button", id="buscar-update-avaliacao", n_clicks=0),
                                html.Div(id = 'update-avaliacao-options',
                                    style = {"display": "none"},
                                    children = [
                                        html.H4('Comentário:', className='comando'),
                                        dcc.Input(id='input-comentario-avaliacao-update', className="input", type='text'),                            
                                        html.H4('Nota:', className='comando'),
                                        dcc.Slider(
                                            id='input-nota-avaliacao-update',
                                            min=1,
                                            max=5,
                                            marks={1:"1",2:"2",3:"3",4:"4",5:"5"},
                                            step=None,
                                            value=3,
                                        ),
                                        html.Button(children=["enviar"], className="Button", id="enviar-update-avaliacao", n_clicks=0),
                                ]),
                                html.Div(id='result-update-avaliacao', style={"display":"none"}, className="card-output",),
                        ]),

                        html.Div(id = 'update-loja-page',
                            style = {"display": "none"},
                            className = 'update',
                            children = [
                                html.H4('Update Loja', className='card-subtitle'),
                                dcc.Dropdown(id='input-update-loja', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "1 - Farmacia Alegria","value": "1",},
                                        {"label": "2 - Volta ao Mundo","value": "2",},
                                        {"label": "3 - Banco Familia","value": "3",},
                                        {"label": "4 - Acai Mania","value": "4",},
                                        {"label": "5 - Academia Hercules","value": "5",},
                                    ],
                                    placeholder="Selecione uma loja",
                                ),
                                html.Button(children=["buscar"], className="Button", id="buscar-update-loja", n_clicks=0),
                                html.Div(id = 'update-loja-options',
                                    style = {"display": "none"},
                                    children = [
                                        html.H4('Nome:', className='comando'),
                                        dcc.Input(id='input-nome-loja-update', className="input", type='text'),
                                        html.H4('Descrição:', className='comando'),
                                        dcc.Input(id='input-descricao-loja-update', className="input", type='text'),                            
                                        html.H4('Tempo médio de atendimento:', className='comando'),
                                        html.H5('(escreva em minutos)', className='detalhe-comando'),
                                        dcc.Input(id='input-tempo-loja-update', className="input", type='text'),
                                        html.Button(children=["enviar"], className="Button", id="enviar-update-loja", n_clicks=0),
                                ]),
                                html.Div(id='result-update-loja', style={"display":"none"}, className="card-output",),
                        ]),

                        # DELETE

                        html.Div(id = 'delete-usuario-page',
                            style = {"display": "none"},
                            className = 'delete',
                            children = [
                                html.H4('Delete Usuário', className='card-subtitle'),
                                dcc.Dropdown(id='input-delete-usuario', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "jose@gmail.com","value": "jose@gmail.com",},
                                        {"label": "lucas@gmail.com","value": "lucas@gmail.com",},
                                        {"label": "marco@gmail.com","value": "marco@gmail.com",},
                                        {"label": "plinio@gmail.com","value": "plinio@gmail.com",},
                                        {"label": "tati@gmail.com","value": "tati@gmail.com",},
                                        {"label": "teste@gmail.com","value": "teste@gmail.com",},
                                    ],
                                    placeholder="Selecione o email do usuário",
                                    value = "none",
                                ),
                                html.Button(children=["delete"], className="Button", id="buscar-delete-usuario", n_clicks=0),
                                html.Div(id = 'delete-usuario-confirmacao',
                                    style = {"display": "none"},
                                    children = [
                                        html.H4('Tem certeza?', className='comando', style = {"margin-top":"10%"}),
                                        html.Button(children=["sim"], className="Button", id="confirmar-delete-usuario", n_clicks=0),
                                    ]
                                ), 
                                html.Div(id='result-delete-usuario', style={"display":"none"}, className="card-output",),           
                        ]),

                        html.Div(id = 'delete-avaliacao-page',
                            style = {"display": "none"},
                            className = 'delete',
                            children = [
                                html.H4('Delete Avaliacao', className='card-subtitle'),
                                dcc.Dropdown(id='input-delete-avaliacao1', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "jose@gmail.com","value": "jose@gmail.com",},
                                        {"label": "lucas@gmail.com","value": "lucas@gmail.com",},
                                        {"label": "marco@gmail.com","value": "marco@gmail.com",},
                                        {"label": "plinio@gmail.com","value": "plinio@gmail.com",},
                                        {"label": "tati@gmail.com","value": "tati@gmail.com",},
                                    ],
                                    placeholder="Selecione o email do usuário",
                                ),
                                dcc.Dropdown(id='input-delete-avaliacao2', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "1 - Farmacia Alegria","value": "1",},
                                        {"label": "2 - Volta ao Mundo","value": "2",},
                                        {"label": "3 - Banco Familia","value": "3",},
                                        {"label": "4 - Acai Mania","value": "4",},
                                        {"label": "5 - Academia Hercules","value": "5",},
                                    ],
                                    placeholder="Selecione a loja",
                                ),
                                html.Button(children=["delete"], className="Button", id="buscar-delete-avaliacao", n_clicks=0),
                                html.Div(id = 'delete-avaliacao-confirmacao',
                                    style = {"display": "none"},
                                    children = [
                                        html.H4('Tem certeza?', className='comando', style = {"margin-top":"10%"}),
                                        html.Button(children=["sim"], className="Button", id="confirmar-delete-avaliacao", n_clicks=0),
                                    ]
                                ),
                                html.Div(id='result-delete-avaliacao', style={"display":"none"}, className="card-output",),            
                        ]),

                        html.Div(id = 'delete-loja-page',
                            style = {"display": "none"},
                            className = 'delete',
                            children = [
                                html.H4('Delete Loja', className='card-subtitle'),
                                dcc.Dropdown(id='input-delete-loja', className ="input",
                                    searchable=True,
                                    clearable=False,
                                    options=[
                                        {"label": "1 - Farmacia Alegria","value": "1",},
                                        {"label": "2 - Volta ao Mundo","value": "2",},
                                        {"label": "3 - Banco Familia","value": "3",},
                                        {"label": "4 - Acai Mania","value": "4",},
                                        {"label": "5 - Academia Hercules","value": "5",},
                                        {"label": "6 - Flores do Cerrado","value": "6",},
                                    ],
                                    placeholder="Selecione a loja",
                                    value = "none",
                                ),
                                html.Button(children=["delete"], className="Button", id="buscar-delete-loja", n_clicks=0),
                                html.Div(id = 'delete-loja-confirmacao',
                                    style = {"display": "none"},
                                    children = [
                                        html.H4('Tem certeza?', className='comando', style = {"margin-top":"10%"}),
                                        html.Button(children=["sim"], className="Button", id="confirmar-delete-loja", n_clicks=0),
                                    ]
                                ), 
                                html.Div(id='result-delete-loja', style={"display":"none"}, className="card-output",),           
                        ]),

                        # BOTÃO DE VOLTAR

                        html.Div(id="botao-voltar",
                            className = "menu",
                            style = {"display": "none"},
                            children = [
                                html.Button(children=["voltar ao menu principal"], className="Button", id="voltar-button", n_clicks=0),
                        ]),
                        
                    ]
                ),
                html.Div(id = 'output',
                    className='card',
                    children = [html.Div(children = [],id='output-data'),]
                )
        ]),
    ], className='row'),
])

def call_display(app):

    @app.callback(
        [
            Output("menu-principal", "style"),
            Output("botao-voltar", "style"),
        ],
        [
            Input("create-button", "n_clicks"),
            Input("read-button", "n_clicks"),
            Input("update-button", "n_clicks"),
            Input("delete-button", "n_clicks"),

            Input("usuario-button", "n_clicks"),
            Input("avaliacao-button", "n_clicks"),
            Input("loja-button", "n_clicks"),

            Input("usuarios-button", "n_clicks"),
            Input("avaliacoes-button", "n_clicks"),
            Input("lojas-button", "n_clicks"),
            Input("view-button", "n_clicks"),
            
        ],
    )
    def show_menu_principal(create,read,update,delete,usuario,avaliacao,loja,usuarios,avaliacoes,lojas,view):
        entradas = [create,read,update,delete,usuario, avaliacao, loja, usuarios,avaliacoes,lojas, view]

        for i in entradas:
            if i == 1:
                return [{"display":"none"},{}]
        #if(create == 1 ) or (read == 1) or (update == 1) or (delete == 1) or (usuarios == 1) or (avaliacoes == 1) or (lojas == 1) or (view == 1) or (usuario == 0 or avaliacao == 0 or loja == 0):
            
        return [{},{"display":"none"}]

    @app.callback(
        [
            Output("menu-entidades", "style"),
        ],
        [
            Input("create-button", "n_clicks"),
            Input("update-button", "n_clicks"),
            Input("delete-button", "n_clicks"), 

            Input("usuario-button", "n_clicks"),
            Input("avaliacao-button", "n_clicks"),
            Input("loja-button", "n_clicks"),
            Input("voltar-button", "n_clicks"),
        ],
    )
    def show_menu_entidades(create,update,delete,usuario,avaliacao,loja,voltar):
        if((create == 1 ) or (update == 1) or (delete == 1)) :
            return [{}]
        return [{"display":"none"}]

    @app.callback(
        [
            Output("menu-read", "style"),
        ],
        [
            Input("read-button", "n_clicks"),
            Input("usuarios-button", "n_clicks"),
            Input("avaliacoes-button", "n_clicks"),
            Input("lojas-button", "n_clicks"),
            Input("view-button", "n_clicks"),
            Input("voltar-button", "n_clicks"),
        ]
    )
    def show_menu_read(read,a,b,c,d,e):
        if(read == 1):
            return [{}]
        return [{"display":"none"}]

    # controla display das páginas do create
   
def call_usuario(app):
    @app.callback(
        [
            Output("create-usuario-page", "style"),
        ],
        [
            Input("usuario-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def ir_criar_usuario(usuario,create,update,delete):
        if(usuario == 1) and (create == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("result-create-usuario","style"),
            Output("result-create-usuario","children"),
        ],
        [
            Input("enviar-create-usuario-button", "n_clicks"),
            
        ],
        [
            State("input-email-usuario","value"),
            State("input-nome-usuario","value"),
            State("input-senha-usuario","value"),
            State("input-bairro-usuario","value"),
            State("input-complemento-usuario","value")
        ]
    )
    def criar_usuario2(enviar,email,nome,senha,bairro,complemento):
        if(enviar == 1):
            codigo = verifica_procedure(bairro,complemento)
            return [{},create_usuario(email,nome,senha,codigo)]
        return [{"display":"none"},None]

    @app.callback(
        [
            Output("update-usuario-page", "style"),
        ],
        [
            Input("usuario-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def atualizar_usuario1(usuario,create,update,delete):
        if(usuario == 1) and (update == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("update-usuario-options", "style"),
            Output("input-nome-usuario-update","value"),
            Output("input-senha-usuario-update","value")
        ],
        [
            Input("buscar-update-usuario", "n_clicks"),   
        ],
        [
            State("input-update-usuario", "value")
        ]
    )
    def atualizar_usuario2(buscar,email):
        if(buscar == 1):
            user = read_usuario_especifico(email)
            nome = user[0][1]
            senha = user[0][2]
            return [{}, nome, senha]
        return [{"display":"none"}, None, None]

    @app.callback(
        [
            Output("result-update-usuario", "children"),
            Output("result-update-usuario", "style"),
        ],
        [
            Input("enviar-update-usuario", "n_clicks"),   
        ],
        [
            State("input-update-usuario", "value"),
            State("input-nome-usuario-update","value"),
            State("input-senha-usuario-update","value"),
        ]
    )
    def atualizar_usuario3(enviar,email,nome,senha):
        if(enviar == 1):
            return [update_usuario(nome, senha, email), {}]
        return [None, {"display":"none"}]

    @app.callback(
        [
            Output("delete-usuario-page", "style"),
        ],
        [
            Input("usuario-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def deletar_usuario1(usuario,create,update,delete):
        if(usuario == 1) and (delete == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("delete-usuario-confirmacao", "style"),
        ],
        [
            Input("buscar-delete-usuario", "n_clicks"),   
        ]
    )
    def deletar_usuario2(confirmar):
        if(confirmar == 1):
            return [{}]
        return [{"display":"none"}]
    

    @app.callback(
        [
            Output("result-delete-usuario", "children"),
            Output("result-delete-usuario", "style"),
        ],
        [
            Input("confirmar-delete-usuario", "n_clicks"),   
        ],
        [
            State("input-delete-usuario","value")
        ]
    )
    def deletar_usuario_final(confirmar,email):
        if(confirmar == 1): 
            return [delete_usuario(email),{}]
        return [None, {"display":"none"}]

  
def call_avaliacao(app):
    @app.callback(
        [
            Output("create-avaliacao-page", "style"),
        ],
        [
            Input("avaliacao-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def criar_avaliacao(avaliacao,create,update,delete):
        if(avaliacao == 1) and (create == 1):
            return [{}]
        return [{"display":"none"}]

    @app.callback(
        [
            Output("result-create-avaliacao", "style"),
            Output("result-create-avaliacao", "children"),
        ],
        [
            Input("enviar-create-avaliacao-button", "n_clicks"),
            
        ],
        [
            State("input-comentario-avaliacao", "value"),
            State("input-nota-avaliacao", "value"),
            State("input-usuario-avaliacao", "value"),
            State("input-loja-avaliacao", "value"),
        ]
    )
    def criar_avaliacao2(enviar,comentario,nota,email,loja):
        if(enviar == 1):
            return [{},create_avaliacao(comentario,nota,email,loja)]
        return [{"display":"none"},None]
    


    @app.callback(
        [
            Output("update-avaliacao-page", "style"),
        ],
        [
            Input("avaliacao-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def atualizar_avaliacao1(avaliacao,create,update,delete):
        if(avaliacao == 1) and (update == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("update-avaliacao-options", "style"),
            Output("input-comentario-avaliacao-update","value"),
            Output("input-nota-avaliacao-update","value")
        ],
        [
            Input("buscar-update-avaliacao", "n_clicks"),   
        ],
        [
            State("input-update-avaliacao1", "value"),
            State("input-update-avaliacao2", "value")
        ]
    )
    def atualizar_usuario2(buscar,email,codigo):
        if(buscar == 1):
            avaliacao = read_avaliacao_especifico(email,codigo)
            comentario = avaliacao[0][1]
            nota = avaliacao[0][2]
            return [{}, comentario, nota]
        return [{"display":"none"}, None, None]

    @app.callback(
        [
            Output("result-update-avaliacao", "children"),
            Output("result-update-avaliacao", "style"),
        ],
        [
            Input("enviar-update-avaliacao", "n_clicks"),   
        ],
        [
            State("input-update-avaliacao1", "value"),
            State("input-update-avaliacao2", "value"),
            State("input-comentario-avaliacao-update","value"),
            State("input-nota-avaliacao-update","value"),
        ]
    )
    def atualizar_usuario3(enviar,email,codigo,comentario,nota):
        if(enviar == 1):
            return [update_avaliacao(comentario, nota, email,codigo), {}]
        return [None, {"display":"none"}]

    @app.callback(
        [
            Output("delete-avaliacao-page", "style"),
        ],
        [
            Input("avaliacao-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def deletar_avaliacao1(avaliacao,create,update,delete):
        if(avaliacao == 1) and (delete == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("delete-avaliacao-confirmacao", "style"),
        ],
        [
            Input("buscar-delete-avaliacao", "n_clicks"),   
        ]
    )
    def deletar_avaliacao2(confirmar):
        if(confirmar == 1):
            return [{}]
        return [{"display":"none"}]
    
    @app.callback(
        [
            Output("result-delete-avaliacao", "children"),
            Output("result-delete-avaliacao", "style"),
        ],
        [
            Input("confirmar-delete-avaliacao", "n_clicks"),   
        ],
        [
            State("input-delete-avaliacao1","value"),
            State("input-delete-avaliacao2","value")
        ]
    )
    def deletar_avaliacao_final(confirmar,email,codigo):
        if(confirmar == 1): 
            return [delete_avaliacao(email,codigo),{}]
        return [None, {"display":"none"}]

def call_loja(app):
    @app.callback(
        [
            Output("create-loja-page", "style"),
        ],
        [
            Input("loja-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def criar_loja(loja,create,update,delete):
        if(loja == 1) and (create == 1):
            return [{}]
        return [{"display":"none"}]

    @app.callback(
        [
            Output("result-create-loja","style"),
            Output("result-create-loja","children"),
        ],
        [
            Input("enviar-create-loja-button", "n_clicks"),
            
        ],
        [
            State("input-nome-loja","value"),
            State("input-descricao-loja","value"),
            State("input-tempo-loja","value"),
            State("input-bairro-loja","value"),
            State("input-complemento-loja","value")
        ]
    )
    def criar_usuario2(enviar,nome,descricao,tempo,bairro,complemento):
        if(enviar == 1):
            codigo = total_elementos2() + 1
            local_codigo = verifica_procedure(bairro,complemento)
            return [{},create_estabelecimento(codigo,nome,descricao,int(tempo),local_codigo)]
        return [{"display":"none"},None]

    @app.callback(
        [
            Output("update-loja-page", "style"),
        ],
        [
            Input("loja-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def atualizar_loja1(loja,create,update,delete):
        if(loja == 1) and (update == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("update-loja-options", "style"),
            Output("input-nome-loja-update","value"),
            Output("input-descricao-loja-update","value"),
            Output("input-tempo-loja-update","value"),
        ],
        [
            Input("buscar-update-loja", "n_clicks"),   
        ],
        [
            State("input-update-loja", "value"),
        ]
    )
    def atualizar_loja2(buscar,codigo):
        if(buscar == 1):
            loja = read_estabelecimento_especifico(codigo)
            nome = loja[0][1]
            descricao = loja[0][2]
            tempo = str(loja[0][3]) 
            return [{},nome,descricao,tempo]
        return [{"display":"none"},None,None,None]

    @app.callback(
        [
            Output("result-update-loja", "children"),
            Output("result-update-loja", "style"),
        ],
        [
            Input("enviar-update-loja", "n_clicks"),   
        ],
        [
            State("input-update-loja", "value"),
            State("input-nome-loja-update","value"),
            State("input-descricao-loja-update","value"),
            State("input-tempo-loja-update","value"),
        ]
    )
    def atualizar_loja3(enviar,codigo,nome,descricao,tempo):
        if(enviar == 1):
            return [update_estabelecimento(nome, descricao, tempo, codigo), {}]
        return [None, {"display":"none"}]

    @app.callback(
        [
            Output("delete-loja-page", "style"),
        ],
        [
            Input("loja-button", "n_clicks"),
            
        ],
        [
            State("create-button", "n_clicks"),
            State("update-button", "n_clicks"),
            State("delete-button", "n_clicks"),
        ]
    )
    def deletar_loja1(loja,create,update,delete):
        if(loja == 1) and (delete == 1):
            return [{}]
        return [{"display":"none"}]
        #return [result]

    @app.callback(
        [
            Output("delete-loja-confirmacao", "style"),
        ],
        [
            Input("buscar-delete-loja", "n_clicks"),   
        ]
    )
    def deletar_loja2(confirmar):
        if(confirmar == 1):
            return [{}]
        return [{"display":"none"}]

    @app.callback(
        [
            Output("result-delete-loja", "children"),
            Output("result-delete-loja", "style"),
        ],
        [
            Input("confirmar-delete-loja", "n_clicks"),   
        ],
        [
            State("input-delete-loja","value")
        ]
    )
    def deletar_loja_final(confirmar,codigo):
        if(confirmar == 1): 
            return [delete_estabelecimento(codigo),{}]
        return [None, {"display":"none"}]

def call_read(app):
    @app.callback(
        [
            Output("read-usuario-page", "style"),
            Output("output-read-usuario","children"),
            
        ],
        [
            Input("usuarios-button", "n_clicks"),      
        ]
    )
    def ler_usuario(usuarios):
        content = []
        if(usuarios == 1):
            result = {}
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
            
            colunas = ["Email","Nome","Senha","Código_Local"]
            content.append(dash_table.DataTable(
                data=user_dict,
                columns=[{'id': c, 'name': c} for c in colunas],
                style_cell={
                                'textOverflow': 'ellipsis',
                                'maxWidth': 'auto',
                                'height': 'auto',
                                'textAlign': 'center'
                            },
                style_table={
                                'maxHeight': '700px',
                                'overflowY': 'auto',
                                'overflowX': 'auto'
                            }
            ))
        else:
            result = {"display":"none"}
        return [result,content]

    @app.callback(
        [
            Output("read-avaliacao-page", "style"),
            Output("output-read-avaliacao","children"),
        ],
        [
            Input("avaliacoes-button", "n_clicks"),
            
        ]
    )
    def ler_avaliacao(avaliacoes):
        content = []
        if(avaliacoes == 1):
            result = {}
            dicio = {"Horário":"", "Comentário":"", "Nota":"","Email_Usuário":"", "Código_Loja":""}
            avaliacao_dict = []
            avaliacao = read_avaliacao()
            j = 0
            for i in avaliacao:
                dicio["Horário"] = str(avaliacao[j][0])
                dicio["Comentário"] = avaliacao[j][1]
                dicio["Nota"] = avaliacao[j][2]
                dicio["Email_Usuário"] = avaliacao[j][3]
                dicio["Código_Loja"] = avaliacao[j][4]
                
                avaliacao_dict.append(dicio.copy())
                j = j + 1
            
            colunas = ["Horário","Comentário","Nota","Email_Usuário","Código_Loja"]
            content.append(dash_table.DataTable(
                data=avaliacao_dict,
                columns=[{'id': c, 'name': c} for c in colunas],
                style_cell={
                                'textOverflow': 'ellipsis',
                                'maxWidth': 'auto',
                                'height': 'auto',
                                'textAlign': 'center'
                            },
                style_table={
                                'maxHeight': '700px',
                                'overflowY': 'auto',
                                'overflowX': 'auto'
                            }
            ))
        else:
            result = {"display":"none"}
        return [result,content]

    @app.callback(
        [
            Output("read-loja-page", "style"),
            Output("output-read-loja","children"),
        ],
        [
            Input("lojas-button", "n_clicks"),
            
        ]
    )
    def ler_loja(lojas):
        content = []
        if(lojas == 1):
            result = {}
            dicio = {"Código":"", "Nome":"", "Descrição":"","Tempo Atendimento":"", "Código_Local":""}
            loja_dict = []
            loja = read_estabelecimento()
            j = 0
            for i in loja:
                dicio["Código"] = loja[j][0]
                dicio["Nome"] = loja[j][1]
                dicio["Descrição"] = loja[j][2]
                dicio["Tempo Atendimento"] = str(loja[j][3])
                dicio["Código_Local"] = loja[j][4]
                
                loja_dict.append(dicio.copy())
                j = j + 1
            
            colunas = ["Código","Nome","Descrição","Tempo Atendimento","Código_Local"]
            content.append(dash_table.DataTable(
                data=loja_dict,
                columns=[{'id': c, 'name': c} for c in colunas],
                style_cell={
                                'textOverflow': 'ellipsis',
                                'maxWidth': 'auto',
                                'height': 'auto',
                                'textAlign': 'center'
                            },
                style_table={
                                'maxHeight': '700px',
                                'overflowY': 'auto',
                                'overflowX': 'auto'
                            }
            ))
        else:
            result = {"display":"none"}
        return [result,content]

    @app.callback(
        [
            Output("read-view-page", "style"),
        ],
        [
            Input("view-button", "n_clicks"),
        ]
    )
    def ler_view(view): 
        if(view == 1):
            return [{}]
        return [{"display":"none"}]

    @app.callback(
        [
            Output("output-read-view","children"),
        ],
        [
            
            Input("input-read-view", "value"),
        ]
    )
    def ler_view(email): 
        content = []
        if(email):
            dicio = {"Loja":"", "Nível de Aglomeração":""}
            loja_dict = []
            loja = read_view(email)
            j = 0
            for i in loja:
                dicio["Loja"] = loja[j][0]
                dicio["Nível de Aglomeração"] = loja[j][1]
                
                loja_dict.append(dicio.copy())
                j = j + 1
            
            colunas = ["Loja","Nível de Aglomeração"]
            content.append(dash_table.DataTable(
                data=loja_dict,
                columns=[{'id': c, 'name': c} for c in colunas],
                style_cell={
                                'textOverflow': 'ellipsis',
                                'maxWidth': 'auto',
                                'height': 'auto',
                                'textAlign': 'center'
                            },
                style_table={
                                'maxHeight': '700px',
                                'overflowY': 'auto',
                                'overflowX': 'auto'
                            }
            ))
        return [content]
        

def call_button(app):

    # reseta os outros botoes ao clicar no botao "voltar"
    @app.callback(
        [
            Output("usuario-button", "n_clicks"),
            Output("avaliacao-button", "n_clicks"),
            Output("loja-button", "n_clicks"),
            Output("usuarios-button", "n_clicks"),
            Output("avaliacoes-button", "n_clicks"),
            Output("lojas-button", "n_clicks"),
            Output("view-button", "n_clicks"),

            Output("enviar-create-usuario-button", "n_clicks"),
            Output("enviar-create-avaliacao-button", "n_clicks"),
            Output("enviar-create-loja-button", "n_clicks"),

            Output("buscar-update-usuario", "n_clicks"),
            Output("buscar-update-avaliacao", "n_clicks"),
            Output("buscar-update-loja", "n_clicks"),

            Output("buscar-delete-usuario", "n_clicks"),
            Output("buscar-delete-avaliacao", "n_clicks"),
            Output("buscar-delete-loja", "n_clicks"),

            Output("enviar-update-usuario", "n_clicks"),
            Output("enviar-update-avaliacao", "n_clicks"),
            Output("enviar-update-loja", "n_clicks"),
            
            Output("confirmar-delete-usuario", "n_clicks"),
            Output("confirmar-delete-avaliacao", "n_clicks"),
            Output("confirmar-delete-loja", "n_clicks"), 
            
        ],
        [
            Input("voltar-button", "n_clicks")
        ],
    )
    def voltar_menu_principal(voltar):
        return [0,0,0,0,0,0,0    ,0,0,0  ,0,0,0   ,0,0,0  ,0,0,0   ,0,0,0]

    @app.callback(
        [
            Output("read-button", "n_clicks"),
        ],
        [
            Input("voltar-button", "n_clicks"),
            Input("usuarios-button", "n_clicks"),
            Input("avaliacoes-button", "n_clicks"),
            Input("lojas-button", "n_clicks"),
            Input("view-button", "n_clicks"),
        ],
    )
    def reset_read_button(voltar,a,b,c,d):
        return [0]

    @app.callback(
        [
            Output("create-button", "n_clicks"),
            Output("update-button", "n_clicks"),
            Output("delete-button", "n_clicks"),
        ],
        [
            Input("voltar-button", "n_clicks"),
            Input("usuario-button", "n_clicks"),
            Input("avaliacao-button", "n_clicks"),
            Input("loja-button", "n_clicks")
        ],
    )
    def reset_menu_principal_buttons(voltar,a,b,c):
        return [0,0,0]

    @app.callback(
        [
            #usuario
            Output("input-usuario-avaliacao", "options"),
            Output("input-read-view", "options"),
            Output("input-update-usuario", "options"),
            Output("input-update-avaliacao1", "options"),
            Output("input-delete-usuario", "options"),
            Output("input-delete-avaliacao1", "options"),
            
            #loja
            Output("input-loja-avaliacao", "options"),
            Output("input-update-avaliacao2", "options"),
            Output("input-update-loja", "options"),
            Output("input-delete-avaliacao2", "options"),
            Output("input-delete-loja", "options"),
            
        ],
        [
            Input("voltar-button", "n_clicks"),
        ],
    )
    def update_dropdowns(voltar):
        dict_options = {"label":"", "value":""}
        usuarios = []
        user = read_usuario()
        j = 0
        for i in user:
            dict_options["label"] = user[j][0]
            dict_options["value"] = user[j][0]
            usuarios.append(dict_options.copy())
            j = j + 1

        lojas = []
        loja = read_estabelecimento()
        j = 0
        for y in loja:
            codigo = str(loja[j][0])
            nome = loja[j][1]
            label = codigo + " - " + nome
            dict_options["label"] = label
            dict_options["value"] = codigo
            lojas.append(dict_options.copy())
            j = j + 1

        return [usuarios,usuarios,usuarios,usuarios,usuarios,usuarios,lojas, lojas, lojas, lojas, lojas]


  
def main_callbacks(app):
    call_display(app)
    call_button(app)
    call_usuario(app)
    call_avaliacao(app)
    call_read(app)
    call_loja(app)
    