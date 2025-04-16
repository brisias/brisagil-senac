INSERT INTO alunos (matricula,cpf,nome,endereco,telefone,email) VALUES
('202102B381','111.333.222-99','Lúcia Luciléia Luciene','Rua Um, 20','(83)99459-9355','lu.luci.luci@mail.com'),
('202301A013','222.111.444-03','Dênis Dionísio Dantas','Rua Rosa, 315','(21)97835-9947','DDDantas.03@mail.com');

-- --------------------------------------------------------

INSERT INTO funcionarios (siape,tipo_usuario,cpf,nome,endereco,telefone,email) VALUES
('2020100384','administrativo','503.150.798-00','Karen Kathleen Kutz','Rua Treze de Maio, 113','(54)99777-5412','karen.kerida@mail.com'),
('2007030114','docente','083.213.543-63','Frederica Fernandes Freire','Avenida Sete, 87','(23)98346-6454','fred.freire@mail.com');

-- --------------------------------------------------------

INSERT INTO livros (isbn,ano_publi,autor_es,categoria,editora,exemplares,titulo) VALUES
('9788569020202','2017','MUKASONGA, Scholastique','Romance francês','Editora Nós','53','Nossa senhora do Nilo'),
('9788535930344','2005','SARAMAGO, José','Romance português','Companhia das Letras','103','As intermitências da morte');

-- --------------------------------------------------------

INSERT INTO emprestimos (numero,data_saida,data_devolucao,matricula,siape,isbn) VALUES
(102,'2025-04-15','2025-05-15','-','2007030114','9788535930344'),
(103,'2025-04-15','2025-05-05','-','2020100384','9788535930344'),
(103,'2025-04-15','2025-05-05','-','2020100384','9788569020202'),
(104,'2025-04-15','2025-04-25','202301A013','-','9788569020202');