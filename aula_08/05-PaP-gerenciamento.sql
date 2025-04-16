CREATE DATABASE SisGePro

-- --------------------------------------------------------

CREATE TABLE projeto(
    id_projeto VARCHAR(15) NOT NULL,
    nome VARCHAR(70) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    data_inicio VARCHAR(10) NOT NULL,
    data_fim VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_projeto)
); 

-- --------------------------------------------------------

CREATE TABLE tarefa(
    id_tarefa VARCHAR(6) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    data_inicio VARCHAR(10) NOT NULL,
    data_fim VARCHAR(10) NOT NULL,
    andamento VARCHAR(30) NOT NULL,
    id_projeto VARCHAR(15) NOT NULL,
    PRIMARY KEY (id_tarefa),
    FOREIGN KEY (id_projeto) REFERENCES projeto (id_projeto)
); 

-- --------------------------------------------------------

CREATE TABLE usuario(
    id_usuario VARCHAR(20) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(60) NOT NULL,
    PRIMARY KEY (id_usuario)
);

-- --------------------------------------------------------

CREATE TABLE atribuicao(
    id_atribuicao VARCHAR(20) NOT NULL,
    id_usuario VARCHAR(20) NOT NULL,
    id_tarefa VARCHAR(6) NOT NULL,
    data_atribuicao VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_atribuicao),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
    FOREIGN KEY (id_tarefa) REFERENCES tarefa (id_tarefa)
);