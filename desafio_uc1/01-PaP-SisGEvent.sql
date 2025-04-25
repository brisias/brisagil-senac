CREATE DATABASE SisGEvent

-- --------------------------------------------------------

CREATE TABLE evento (
    idEvento VARCHAR(13) NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    tipo_evento VARCHAR(25) NOT NULL, -- workshop, palestra, oficina, simpósio, etc.
    descricao VARCHAR(100) NOT NULL,
    datahora_inicio VARCHAR(20) NOT NULL, -- DD-MM-YYYY HH:MI:SS
    datahora_fim VARCHAR(20) NOT NULL, -- DD-MM-YYYY HH:MI:SS
    taxa_insc FLOAT,
    capacidade_insc INT NOT NULL,
    idLocal VARCHAR(13) NOT NULL,
    idPalestrante VARCHAR(13) NOT NULL,
    PRIMARY KEY (idEvento, titulo),
    FOREIGN KEY (idLocal) REFERENCES local (idLocal),
    FOREIGN KEY (idPalestrante) REFERENCES palestrante (idPalestrante)
); 

-- --------------------------------------------------------

CREATE TABLE local (
    idLocal VARCHAR(13) NOT NULL,
    nome_local VARCHAR(50) NOT NULL,
    tipo_local VARCHAR(30) NOT NULL, -- sala, auditório, ginásio, etc.
    setor VARCHAR(50) NOT NULL, -- setor da universidade em que o local fica
    capacidade INT NOT NULL,
    recursos VARCHAR(100),
    PRIMARY KEY (idLocal)
);

-- --------------------------------------------------------

CREATE TABLE participante (
    cpf VARCHAR(14) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(60) NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    categoria VARCHAR(25) NOT NULL, -- aluno, professor, servidor, etc.
    instituicao VARCHAR(50),
    PRIMARY KEY (cpf)
);

-- --------------------------------------------------------

CREATE TABLE palestrante (
    idPalestrante VARCHAR(13) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    contato VARCHAR(100) NOT NULL, -- e-mail / telefone
    mini_curriculo VARCHAR(100) NOT NULL,
    instituicao VARCHAR(50),
    PRIMARY KEY (idPalestrante)
);

-- --------------------------------------------------------

CREATE TABLE inscricao (
    idInscricao VARCHAR(13) NOT NULL,
    datahora_registro VARCHAR(20) NOT NULL, -- DD-MM-YYYY HH:MI:SS
    situacao VARCHAR(20) NOT NULL, -- pendente, confirmada, cancelada
    presenca VARCHAR(15), -- compareceu, não compareceu
    cpf VARCHAR(14) NOT NULL,
    idEvento VARCHAR(13) NOT NULL,
    PRIMARY KEY (idInscricao),
    FOREIGN KEY (cpf) REFERENCES participante (cpf),
    FOREIGN KEY (idEvento) REFERENCES evento (idEvento)
);

-- --------------------------------------------------------

CREATE TABLE certificado (
    idCertificado INTEGER AUTO_INCREMENT,
    carga_horaria VARCHAR(3) NOT NULL, -- HH'h'
    idInscricao VARCHAR(13) NOT NULL, 
    PRIMARY KEY (idCertificado),
    FOREIGN KEY (idInscricao) REFERENCES inscricao (idInscricao)
);
