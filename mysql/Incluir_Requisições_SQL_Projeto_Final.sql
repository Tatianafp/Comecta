USE mydb;

INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('1', 'ASA NORTE', 'SQN 304; Bloco Z; Apt 333;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('2', 'VICENTE PIRES', 'RUA 3Z; CHACARA 666; CASA 3;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('3', 'TAGUATINGA NORTE', 'TQNQ 200; Bloco X; Apt 706;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('4', 'ASA NORTE', 'SQN 404; Bloco J; Apt 903;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('5', 'ASA NORTE', 'SQN 312; Bloco V; Apt 222;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('6', 'ASA SUL', 'CLS 102; Bloco B; Loja 7;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('7', 'ASA SUL', 'CLS 202; Bloco A; Loja 10;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('8', 'ASA SUL', 'SCS Bloco A; Loja 29;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('9', 'ASA NORTE', 'CLN 311; Bloco A; Loja 32;');
INSERT INTO `mydb`.`local` (`Código`, `Bairro`, `Complemento`) VALUES ('10', 'TAGUATINGA NORTE', 'CLTQN 902; Bloco A; Loja 33;');

INSERT INTO `mydb`.`transporte` (`Código`, `Categoria`, `Risco`) VALUES ('1', 'Carro', 'Nenhum');
INSERT INTO `mydb`.`transporte` (`Código`, `Categoria`, `Risco`) VALUES ('2', 'Onibus', 'Medio');
INSERT INTO `mydb`.`transporte` (`Código`, `Categoria`, `Risco`) VALUES ('3', 'Uber', 'Baixo');
INSERT INTO `mydb`.`transporte` (`Código`, `Categoria`, `Risco`) VALUES ('4', 'Metro', 'Alto');
INSERT INTO `mydb`.`transporte` (`Código`, `Categoria`, `Risco`) VALUES ('5', 'A pé', 'Baixo');

INSERT INTO `mydb`.`produtos` (`Código`, `Nome`, `Descrição`) VALUES ('1', 'Remedios', ' Remedios para dor de cabeça, dor de garganta e afins');
INSERT INTO `mydb`.`produtos` (`Código`, `Nome`, `Descrição`) VALUES ('2', 'Comida Mexicana', 'Tacos, guacamole, burrito, nachos...');
INSERT INTO `mydb`.`produtos` (`Código`, `Nome`, `Descrição`) VALUES ('3', 'Dinheiro', 'Cedulas de dois reais, cinco reais, 10 reais ...');
INSERT INTO `mydb`.`produtos` (`Código`, `Nome`, `Descrição`) VALUES ('4', 'Açai', 'Acai da fruta, batido com charope de guarana e banana...');
INSERT INTO `mydb`.`produtos` (`Código`, `Nome`, `Descrição`) VALUES ('5', 'Aparelhos para Malhar', 'Bicicletas fixas, steps, esteira, jumps...');

INSERT INTO `mydb`.`categoria` (`Nome`, `Descrição`) VALUES ('Farmacia', 'Venda de Remedios e produtos de higiene pessoal;');
INSERT INTO `mydb`.`categoria` (`Nome`, `Descrição`) VALUES ('Restaurante', 'Venda de comida na hora do almoço e/ou jantar;');
INSERT INTO `mydb`.`categoria` (`Nome`, `Descrição`) VALUES ('Banco', 'Local para saques, administrativo, agencia, pagamentos de contas...');
INSERT INTO `mydb`.`categoria` (`Nome`, `Descrição`) VALUES ('Lanchonete', 'Venda de comidas rapidas, para lanches ou cafe da manha;');
INSERT INTO `mydb`.`categoria` (`Nome`, `Descrição`) VALUES ('Academia', 'Local para realizar exercicios fisicos e cuidar do corpo;');


INSERT INTO `mydb`.`usuário` (`Email`, `Nome`, `Senha`, `Local_Código`) VALUES ('tati@gmail.com', 'Tatiana Pereira', 'tatiperfeita', '1');
INSERT INTO `mydb`.`usuário` (`Email`, `Nome`, `Senha`, `Local_Código`) VALUES ('marco@gmail.com', 'Marco Antonio Garcia', 'marcomaravilhoso', '2');
INSERT INTO `mydb`.`usuário` (`Email`, `Nome`, `Senha`, `Local_Código`) VALUES ('lucas@gmail.com', 'Lucas Honda', 'lucaslindo', '3');
INSERT INTO `mydb`.`usuário` (`Email`, `Nome`, `Senha`, `Local_Código`) VALUES ('jose@gmail.com', 'Jose Vinicius Garreto', 'josejusto', '4');
INSERT INTO `mydb`.`usuário` (`Email`, `Nome`, `Senha`, `Local_Código`) VALUES ('plinio@gmail.com', 'Plinio Mayer', 'pliniopoderoso', '5');

INSERT INTO `mydb`.`estabelecimento` (`Código`, `Nome`, `Descrição`, `Tempo_Medio_Atendimento`, `Local_Código`) VALUES ('1', 'Farmacia Alegria', 'Farmacia, venda de remedios;', '00:10:00', '6');
INSERT INTO `mydb`.`estabelecimento` (`Código`, `Nome`, `Descrição`, `Tempo_Medio_Atendimento`, `Local_Código`) VALUES ('2', 'Volta ao Mundo', 'Restaurante, venda de comida diversa;', '00:30:00', '7');
INSERT INTO `mydb`.`estabelecimento` (`Código`, `Nome`, `Descrição`, `Tempo_Medio_Atendimento`, `Local_Código`) VALUES ('3', 'Banco Familia', 'Banco, saques, administrativo, agencia, pagamento de contas;', '00:20:00', '8');
INSERT INTO `mydb`.`estabelecimento` (`Código`, `Nome`, `Descrição`, `Tempo_Medio_Atendimento`, `Local_Código`) VALUES ('4', 'Acai Mania', 'Restaurante e lanchonete, venda de comida e lanches;', '00:15:00', '9');
INSERT INTO `mydb`.`estabelecimento` (`Código`, `Nome`, `Descrição`, `Tempo_Medio_Atendimento`, `Local_Código`) VALUES ('5', 'Academia Hercules', 'Academia, lugar para fazer exercicios ', '01:00:00', '10');

INSERT INTO `mydb`.`lotação` (`ID`, `Tempo Estimado`, `Tamanho/nível`, `Estabelecimento_Código`) VALUES ('1', '00:05:00', 'Baixo', '1');
INSERT INTO `mydb`.`lotação` (`ID`, `Tempo Estimado`, `Tamanho/nível`, `Estabelecimento_Código`) VALUES ('2', '01:00:00', 'Medio', '2');
INSERT INTO `mydb`.`lotação` (`ID`, `Tempo Estimado`, `Tamanho/nível`, `Estabelecimento_Código`) VALUES ('3', '00:50:00', 'Medio', '3');
INSERT INTO `mydb`.`lotação` (`ID`, `Tempo Estimado`, `Tamanho/nível`, `Estabelecimento_Código`) VALUES ('4', '00:15:00', 'Baixo', '4');
INSERT INTO `mydb`.`lotação` (`ID`, `Tempo Estimado`, `Tamanho/nível`, `Estabelecimento_Código`) VALUES ('5', '00:00:00', 'Baixo', '5');

INSERT INTO `mydb`.`rotas` (`Código`, `Distância`, `Usuário_Email`, `Estabelecimento_Código`, `Transporte_Código`) VALUES ('1', '7', 'tati@gmail.com', '4', '1');
INSERT INTO `mydb`.`rotas` (`Código`, `Distância`, `Usuário_Email`, `Estabelecimento_Código`, `Transporte_Código`) VALUES ('2', '20', 'jose@gmail.com', '5', '1');
INSERT INTO `mydb`.`rotas` (`Código`, `Distância`, `Usuário_Email`, `Estabelecimento_Código`, `Transporte_Código`) VALUES ('3', '12', 'marco@gmail.com', '3', '2');
INSERT INTO `mydb`.`rotas` (`Código`, `Distância`, `Usuário_Email`, `Estabelecimento_Código`, `Transporte_Código`) VALUES ('4', '10', 'plinio@gmail.com', '2', '3');
INSERT INTO `mydb`.`rotas` (`Código`, `Distância`, `Usuário_Email`, `Estabelecimento_Código`, `Transporte_Código`) VALUES ('5', '18', 'lucas@gmail.com', '1', '1');

INSERT INTO `mydb`.`pico` (`Data`, `Dia da Semana`, `Lotação_ID`) VALUES ('2020-11-02 10:23:13', '2', '1');
INSERT INTO `mydb`.`pico` (`Data`, `Dia da Semana`, `Lotação_ID`) VALUES ('2020-11-02 21:37:03', '2', '2');
INSERT INTO `mydb`.`pico` (`Data`, `Dia da Semana`, `Lotação_ID`) VALUES ('2020-11-02 15:59:58', '2', '3');
INSERT INTO `mydb`.`pico` (`Data`, `Dia da Semana`, `Lotação_ID`) VALUES ('2020-11-03 16:34:56', '3', '4');
INSERT INTO `mydb`.`pico` (`Data`, `Dia da Semana`, `Lotação_ID`) VALUES ('2020-11-07 06:11:34', '7', '5');


INSERT INTO `mydb`.`avaliação` (`Horário`, `Comentário`, `Nota`, `Usuário_Email`, `Estabelecimento_Código`) VALUES ('14:15:56', 'super cuidadosos, funcionários de mascara.', '5','tati@gmail.com', '4');
INSERT INTO `mydb`.`avaliação` (`Horário`, `Comentário`, `Nota`, `Usuário_Email`, `Estabelecimento_Código`) VALUES ('16:00:00', 'Muito bem limpa, musica legal.', '5','jose@Gmail.com', '5');
INSERT INTO `mydb`.`avaliação` (`Horário`, `Comentário`, `Nota`, `Usuário_Email`, `Estabelecimento_Código`) VALUES ('12:30:37', 'Tinha funcionarios sem mascara.', '1','marco@gmail.com', '3');
INSERT INTO `mydb`.`avaliação` (`Horário`, `Comentário`, `Nota`, `Usuário_Email`, `Estabelecimento_Código`) VALUES ('20:20:20', 'Comida muito boa e lugar seguro ', '5', 'plinio@gmail.com', '2');
INSERT INTO `mydb`.`avaliação` (`Horário`, `Comentário`, `Nota`, `Usuário_Email`, `Estabelecimento_Código`) VALUES ('18:42:19', 'Tinha muitas pessoas', '3','lucas@gmail.com', '1');

INSERT INTO `mydb`.`pertence a` (`Estabelecimento_Código`,`Categoria_Nome`) VALUES ('1','Farmacia');
INSERT INTO `mydb`.`pertence a` (`Estabelecimento_Código`,`Categoria_Nome`) VALUES ('2','Restaurante');
INSERT INTO `mydb`.`pertence a` (`Estabelecimento_Código`,`Categoria_Nome`) VALUES ('3','Banco');
INSERT INTO `mydb`.`pertence a` (`Estabelecimento_Código`,`Categoria_Nome`) VALUES ('4','Lanchonete');
INSERT INTO `mydb`.`pertence a` (`Estabelecimento_Código`,`Categoria_Nome`) VALUES ('5','Academia');

INSERT INTO `mydb`.`frequenta` (`Usuário_Email`,`Estabelecimento_Código`) VALUES ('marco@gmail.com','3');
INSERT INTO `mydb`.`frequenta` (`Usuário_Email`,`Estabelecimento_Código`) VALUES ('tati@gmail.com','4');
INSERT INTO `mydb`.`frequenta` (`Usuário_Email`,`Estabelecimento_Código`) VALUES ('jose@gmail.com','5');
INSERT INTO `mydb`.`frequenta` (`Usuário_Email`,`Estabelecimento_Código`) VALUES ('lucas@gmail.com','1');
INSERT INTO `mydb`.`frequenta` (`Usuário_Email`,`Estabelecimento_Código`) VALUES ('plinio@gmail.com','2');

INSERT INTO `mydb`.`contém` (`Produtos_Código`,`Estabelecimento_Código`,`Quantidade`) VALUES ('3','3','200');
INSERT INTO `mydb`.`contém` (`Produtos_Código`,`Estabelecimento_Código`,`Quantidade`) VALUES ('4','4','60');
INSERT INTO `mydb`.`contém` (`Produtos_Código`,`Estabelecimento_Código`,`Quantidade`) VALUES ('5','5','100');
INSERT INTO `mydb`.`contém` (`Produtos_Código`,`Estabelecimento_Código`,`Quantidade`) VALUES ('1','1','200');
INSERT INTO `mydb`.`contém` (`Produtos_Código`,`Estabelecimento_Código`,`Quantidade`) VALUES ('2','2','33');

/* SELECTS PARA VER QUE AS TABELAS ESTÃO PREENCHIDAS

SELECT * FROM mydb.usuário;
SELECT * FROM mydb.estabelecimento;
SELECT * FROM mydb.`local`;
SELECT * FROM mydb.lotação;
SELECT * FROM mydb.rotas;
SELECT * FROM mydb.transporte;
SELECT * FROM mydb.produtos;
SELECT * FROM mydb.pico;
SELECT * FROM mydb.categoria;
SELECT * FROM mydb.avaliação;
SELECT * FROM mydb.`pertence a`;
SELECT * FROM mydb.frequenta;
SELECT * FROM mydb.contém;

*/




/* PROCEDURE TRABALHO FINAL */

DELIMITER $$
CREATE PROCEDURE existe_local(in comp VARCHAR(100), OUT existe int)
BEGIN 
	DECLARE  Sub Varchar(100);
	SELECT Complemento INTO SUB
	FROM `mydb`.`local` WHERE comp = Complemento ;
    IF (SELECT EXISTS(SELECT * from Local WHERE Complemento=SUB)) = 1 THEN
	SET	existe = (SELECT Código from Local WHERE Complemento=SUB);
    else
    set existe = 1 + (SELECT MAX(Código) FROM  `mydb`.`local`);
    
 END IF;
 END
 $$

/* EXEMPLO DE TESTE DA PROCEDURE

CALL existe_local('TESTE',@result);
SELECT @result;

*/

/* VIEWS TRABALHO FINAL */

CREATE VIEW Locais_user
	AS SELECT *
	FROM mydb.usuário u, mydb.`local` l
	WHERE u.`Local_Código` = l.`Código` ;

CREATE VIEW Locais_est
	AS SELECT Nome, Bairro , u.Código
	FROM mydb.estabelecimento u, mydb.`local` l
	WHERE u.`Local_Código` = l.`Código` ;

CREATE VIEW est_perto	
    AS SELECT e.Bairro, e.Nome, u.Nome as Usuario, e.Código, u.Email
	FROM mydb.locais_est e, mydb.locais_user u
	WHERE e.Bairro = u.Bairro;

CREATE VIEW est_perto_lotacao
	AS SELECT u.Nome as Estabelecimento, u.Usuario, l.`Tamanho/nível`, u.Email
	FROM mydb.est_perto u, mydb.lotação l
	WHERE u.Código = l.Estabelecimento_Código;


SELECT DISTINCT estabelecimento as Loja, `Tamanho/nível` as `Nível da Lotação` FROM est_perto_lotacao ORDER BY Usuario;




/* Mais um exemplo de VIEW */

CREATE VIEW Avaliacao_Estabelecimento
	AS SELECT tab.nome as `Usuário`, tab.Nota , estabelecimento.Nome as Loja
	FROM (SELECT * FROM usuário INNER JOIN avaliação on usuário.email = avaliação.`Usuário_Email` ) AS tab INNER
	JOIN estabelecimento on tab.estabelecimento_Código = estabelecimento.Código
	WHERE tab.nota > 3;
    
SELECT * FROM Avaliacao_Estabelecimento;

