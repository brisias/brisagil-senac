CREATE DATABASE loja_online

-- --------------------------------------------------------

CREATE TABLE cliente(
    id_cliente VARCHAR(13) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(60) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_cliente)
); 

-- --------------------------------------------------------

CREATE TABLE produto(
    id_produto VARCHAR(10) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    preco FLOAT NOT NULL,
    estoque INTEGER NOT NULL,
    PRIMARY KEY (id_produto)
); 

-- --------------------------------------------------------

CREATE TABLE pedido(
    id_pedido INTEGER NOT NULL,
    data_pedido DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    id_cliente VARCHAR(13) NOT NULL,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

-- --------------------------------------------------------

CREATE TABLE item_pedido(
    id_item VARCHAR(20) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_und FLOAT NOT NULL,
    id_pedido INTEGER NOT NULL,
    id_produto VARCHAR(10) NOT NULL,
    PRIMARY KEY (id_item),
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);