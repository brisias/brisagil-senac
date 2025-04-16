CREATE DATABASE startup

-- --------------------------------------------------------

CREATE TABLE clientes(
    cpf VARCHAR(14) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    PRIMARY KEY (cpf)
); 

-- --------------------------------------------------------

CREATE TABLE fornecedores(
    cnpj VARCHAR(14) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    PRIMARY KEY (cpf)
); 

-- --------------------------------------------------------

CREATE TABLE equipamentos(
    codigo INTEGER NOT NULL,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    valor FLOAT NOT NULL,
    PRIMARY KEY (codigo)
); 

-- --------------------------------------------------------

CREATE TABLE pedidos1(
    numero INTEGER NOT NULL,
    data DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    cnpj VARCHAR(17) NOT NULL,
    codigo INTEGER NOT NULL,
    PRIMARY KEY (numero, cpf, cnpj, codigo),
    FOREIGN KEY (cpf) REFERENCES clientes (cpf),
    FOREIGN KEY (cnpj) REFERENCES fornecedores (cnpj),
    FOREIGN KEY (codigo) REFERENCES equipamentos (codigo)
);

-- --------------------------------------------------------

DROP TABLE pedidos1;

-- --------------------------------------------------------

CREATE TABLE pedidos(
    id_pedido INTEGER AUTO_INCREMENT,
    numero INTEGER NOT NULL,
    data DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    cnpj VARCHAR(17) NOT NULL,
    codigo INTEGER NOT NULL,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (cpf) REFERENCES clientes (cpf),
    FOREIGN KEY (cnpj) REFERENCES fornecedores (cnpj),
    FOREIGN KEY (codigo) REFERENCES equipamentos (codigo)
);