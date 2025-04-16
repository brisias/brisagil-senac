CREATE DATABASE biblioteca

-- --------------------------------------------------------

CREATE TABLE alunos(
    matricula VARCHAR(10) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    email VARCHAR(60) NOT NULL,
    PRIMARY KEY (matricula)
); 

-- --------------------------------------------------------

CREATE TABLE funcionarios(
    siape VARCHAR(10) NOT NULL,
    tipo_usuario VARCHAR(14) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    email VARCHAR(60) NOT NULL,
    PRIMARY KEY (siape)
); 

-- --------------------------------------------------------

CREATE TABLE livros(
    isbn VARCHAR(13) NOT NULL,
    titulo VARCHAR(80) NOT NULL,
    autor_es VARCHAR(100) NOT NULL,
    editora VARCHAR(50) NOT NULL,
    categoria VARCHAR(30) NOT NULL,
    exemplares INTEGER NOT NULL,
    ano_publi VARCHAR(4) NOT NULL,
    PRIMARY KEY (isbn)
); 

-- --------------------------------------------------------

CREATE TABLE emprestimos(
    id_emprestimo INTEGER AUTO_INCREMENT,
    numero INTEGER NOT NULL,
    data_saida DATE NOT NULL,
    data_devolucao DATE NOT NULL,
    matricula VARCHAR(10) NOT NULL,
    siape VARCHAR(10) NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    PRIMARY KEY (id_emprestimo),
    FOREIGN KEY (matricula) REFERENCES alunos (matricula),
    FOREIGN KEY (siape) REFERENCES funcionarios (siape),
    FOREIGN KEY (isbn) REFERENCES livros (isbn)
);