/* Estudando comandos DML */

-- --------------------------------------------------------
-- comando INSERT: inserindo registros nas tabelas

INSERT INTO clientes (cpf,nome,endereco) VALUES
('021','João da Silva','Rua XYZ, sem número'),
('022','Maria José','Rua das Flores, 330'),
('023','Antônio Maria','Rua Tupinambá, 1544');

-- --------------------------------------------------------

INSERT INTO fornecedores (cnpj,nome,endereco) VALUES
('1011','Ciranda Locações','Rua Azuras, 453'),
('1012','Bola&Balão&Bambolê','Avenida Foguete, 3830'),
('1013','Estrelinha Diversões','Travessa Atravessada, 63');

-- --------------------------------------------------------

INSERT INTO equipamentos (codigo,nome,descricao,valor) VALUES
(11010,'Pula-pula','estrutura inflável com tela de proteção na lateral',615.50),
(11011,'Fliperama 413','estrutura de máquina de arcade, adaptada com 5 jogos',813.05),
(11012,'Futebol de sabão','estrutura inflável com tela de proteção, 12mx6m',1500.10),
(11013,'Piscina de bolinha','estrutura em aço e lona, 1,5m x 1,5m, 500 bolinhas',980.90);

-- --------------------------------------------------------
-- comando SELECT: buscando todos os registros na sua tabela

SELECT * FROM clientes;

-- --------------------------------------------------------
-- erro #1062 chave primária já existente
-- erro #1064 erro de sintaxe
-- erro #1054 coluna não existente na tabela
-- erro #1364 faltou um valor numa coluna NOT NULL

-- --------------------------------------------------------
-- comando UPDATE: atualizar registros nas tabelas

UPDATE clientes
    SET endereco = 'Rua sem fundo, 3435'
    WHERE cpf = '024';

-- --------------------------------------------------------
-- comando DELETE: excluir registros nas tabelas

DELETE
    FROM clientes
    WHERE cpf = '024';

-- --------------------------------------------------------
-- inserindo pedidos:

INSERT INTO pedidos (numero,data,status,cpf,cnpj,codigo) VALUES
(1001,'2025-04-15','análise','021','1011',11011);

INSERT INTO pedidos (numero,data,status,cpf,cnpj,codigo) VALUES
(1001,'2025-04-15','análise','021','1013',11013);