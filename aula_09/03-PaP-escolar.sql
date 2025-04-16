CREATE DATABASE escolar

-- --------------------------------------------------------

CREATE TABLE Alunos(
    id_aluno INTEGER AUTO_INCREMENT,
    numero_matricula VARCHAR(20) NOT NULL,
    nome_completo VARCHAR(255),
    data_nascimento DATE,
    endereco_rua VARCHAR(255),
    endereco_numero VARCHAR(10),
    endereco_complemento VARCHAR(50),
    endereco_bairro VARCHAR(100),
    endereco_cidade VARCHAR(100),
    endereco_estado VARCHAR(50),
    endereco_cep VARCHAR(10),
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_matricula DATE,
    PRIMARY KEY (numero_matricula)
    );

    -- --------------------------------------------------------

    /* erro #1075 - erro na marcação da chave primária, quando usamos um AUTO_INCREMENT ele precisa ser usado como chave primária, nada impede o uso de duas chaves primárias (id_aluno e numero_matricula) ou uma chave única (UNIQUE KEY) para impedir que aja uma repetição na inserção da coluna; */

    -- --------------------------------------------------------

    CREATE TABLE Alunos(
    id_aluno INTEGER AUTO_INCREMENT,
    numero_matricula VARCHAR(20) NOT NULL,
    nome_completo VARCHAR(255),
    data_nascimento DATE,
    endereco_rua VARCHAR(255),
    endereco_numero VARCHAR(10),
    endereco_complemento VARCHAR(50),
    endereco_bairro VARCHAR(100),
    endereco_cidade VARCHAR(100),
    endereco_estado VARCHAR(50),
    endereco_cep VARCHAR(10),
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_matricula DATE,
    UNIQUE KEY (numero_matricula),
    PRIMARY KEY (id_aluno)
);

ou

CREATE TABLE Alunos(
    id_aluno INTEGER AUTO_INCREMENT,
    numero_matricula VARCHAR(20) NOT NULL,
    nome_completo VARCHAR(255),
    data_nascimento DATE,
    endereco_rua VARCHAR(255),
    endereco_numero VARCHAR(10),
    endereco_complemento VARCHAR(50),
    endereco_bairro VARCHAR(100),
    endereco_cidade VARCHAR(100),
    endereco_estado VARCHAR(50),
    endereco_cep VARCHAR(10),
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_matricula DATE,
    PRIMARY KEY (id_aluno, numero_matricula)
);