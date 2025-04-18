-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 17-Abr-2025 às 21:06
-- Versão do servidor: 5.7.36
-- versão do PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escolar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

CREATE TABLE `alunos` (
  `id_aluno` int(11) NOT NULL,
  `nome_completo` varchar(255) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `endereco_rua` varchar(255) DEFAULT NULL,
  `endereco_numero` varchar(10) DEFAULT NULL,
  `endereco_complemento` varchar(50) DEFAULT NULL,
  `endereco_bairro` varchar(100) DEFAULT NULL,
  `endereco_cidade` varchar(100) DEFAULT NULL,
  `endereco_estado` varchar(50) DEFAULT NULL,
  `endereco_cep` varchar(10) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `numero_matricula` varchar(20) NOT NULL,
  `data_matricula` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`id_aluno`, `nome_completo`, `data_nascimento`, `endereco_rua`, `endereco_numero`, `endereco_complemento`, `endereco_bairro`, `endereco_cidade`, `endereco_estado`, `endereco_cep`, `telefone`, `email`, `numero_matricula`, `data_matricula`) VALUES
(1, 'Ana Silva', '2008-05-10', 'Rua das Flores', '123', 'Apto 101', 'Jardim Botânico', 'Rio de Janeiro', 'RJ', '22450-000', '(21) 99999-1111', 'ana.silva@email.com', 'MAT001', '2024-01-15'),
(2, 'Pedro Oliveira', '2007-11-22', 'Avenida Atlântica', '456', NULL, 'Copacabana', 'Rio de Janeiro', 'RJ', '22021-000', '(21) 98888-2222', 'pedro.oliveira@email.com', 'MAT002', '2024-01-15'),
(3, 'Mariana Souza', '2009-03-01', 'Rua da Praia', '789', NULL, 'Ipanema', 'Rio de Janeiro', 'RJ', '22420-000', '(21) 97777-3333', 'mariana.souza@email.com', 'MAT003', '2024-01-16'),
(4, 'Lucas Santos', '2008-08-15', 'Rua do Sol', '1011', 'Casa 2', 'Flamengo', 'Rio de Janeiro', 'RJ', '22210-000', '(21) 96666-4444', 'lucas.santos@email.com', 'MAT004', '2024-01-16'),
(5, 'Beatriz Pereira', '2007-06-30', 'Rua da Paz', '1213', NULL, 'Botafogo', 'Rio de Janeiro', 'RJ', '22250-000', '(21) 95555-5555', 'beatriz.pereira@email.com', 'MAT005', '2024-01-17'),
(6, 'Gabriel Rodrigues', '2009-09-05', 'Travessa da Lapa', '1415', NULL, 'Centro', 'Rio de Janeiro', 'RJ', '20021-000', '(21) 94444-6666', 'gabriel.rodrigues@email.com', 'MAT006', '2024-01-17'),
(7, 'Isabela Lima', '2008-01-20', 'Alameda dos Anjos', '1617', 'Apto 202', 'Barra da Tijuca', 'Rio de Janeiro', 'RJ', '22631-000', '(21) 93333-7777', 'isabela.lima@email.com', 'MAT007', '2024-01-18'),
(8, 'Rafael Costa', '2007-04-12', 'Estrada das Paineiras', '1819', NULL, 'Santa Teresa', 'Rio de Janeiro', 'RJ', '20241-000', '(21) 92222-8888', 'rafael.costa@email.com', 'MAT008', '2024-01-18'),
(9, 'Sophia Fernandes', '2009-12-01', 'Rua da Mangueira', '2021', NULL, 'São Cristóvão', 'Rio de Janeiro', 'RJ', '20921-000', '(21) 91111-9999', 'sophia.fernandes@email.com', 'MAT009', '2024-01-19'),
(10, 'Enzo Pereira', '2008-07-07', 'Praça da Bandeira', '2223', 'Casa 3', 'Tijuca', 'Rio de Janeiro', 'RJ', '20510-000', '(21) 90000-0000', 'enzo.pereira@email.com', 'MAT010', '2024-01-19');

-- --------------------------------------------------------

--
-- Estrutura da tabela `avaliacoes`
--

CREATE TABLE `avaliacoes` (
  `id_avaliacao` int(11) NOT NULL,
  `id_disciplina` int(11) NOT NULL,
  `id_turma` int(11) NOT NULL,
  `data_avaliacao` date NOT NULL,
  `tipo_avaliacao` varchar(50) DEFAULT NULL,
  `peso` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `avaliacoes`
--

INSERT INTO `avaliacoes` (`id_avaliacao`, `id_disciplina`, `id_turma`, `data_avaliacao`, `tipo_avaliacao`, `peso`) VALUES
(1, 1, 1, '2024-03-10', 'Prova 1', '0.40'),
(2, 2, 1, '2024-03-15', 'Trabalho 1', '0.30'),
(3, 3, 2, '2024-03-12', 'Prova 1', '0.50'),
(4, 4, 2, '2024-03-18', 'Participação', '0.20'),
(5, 5, 3, '2024-03-20', 'Prova 1', '0.60'),
(6, 6, 3, '2024-03-25', 'Trabalho em Grupo', '0.40'),
(7, 7, 4, '2024-03-22', 'Prova 1', '0.50'),
(8, 8, 4, '2024-03-28', 'Relatório', '0.30'),
(9, 9, 5, '2024-03-30', 'Avaliação Prática', '0.70'),
(10, 10, 5, '2024-04-05', 'Projeto', '0.50');

-- --------------------------------------------------------

--
-- Estrutura da tabela `disciplinas`
--

CREATE TABLE `disciplinas` (
  `id_disciplina` int(11) NOT NULL,
  `nome_disciplina` varchar(100) NOT NULL,
  `codigo_disciplina` varchar(10) NOT NULL,
  `carga_horaria` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `disciplinas`
--

INSERT INTO `disciplinas` (`id_disciplina`, `nome_disciplina`, `codigo_disciplina`, `carga_horaria`) VALUES
(1, 'Matemática', 'MAT101', 80),
(2, 'Português', 'POR101', 80),
(3, 'História', 'HIS101', 60),
(4, 'Ciências', 'CIE101', 60),
(5, 'Geografia', 'GEO101', 60),
(6, 'Inglês', 'ING101', 40),
(7, 'Física', 'FIS101', 60),
(8, 'Química', 'QUI101', 60),
(9, 'Educação Física', 'EDF101', 40),
(10, 'Artes', 'ART101', 40);

-- --------------------------------------------------------

--
-- Estrutura da tabela `matriculas`
--

CREATE TABLE `matriculas` (
  `id_matricula` int(11) NOT NULL,
  `id_aluno` int(11) NOT NULL,
  `id_turma` int(11) NOT NULL,
  `data_matricula_turma` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `matriculas`
--

INSERT INTO `matriculas` (`id_matricula`, `id_aluno`, `id_turma`, `data_matricula_turma`) VALUES
(1, 1, 1, '2024-02-01'),
(2, 2, 1, '2024-02-01'),
(3, 3, 2, '2024-02-02'),
(4, 4, 2, '2024-02-02'),
(5, 5, 3, '2024-02-03'),
(6, 6, 3, '2024-02-03'),
(7, 7, 4, '2024-02-04'),
(8, 8, 4, '2024-02-04'),
(9, 9, 5, '2024-02-05'),
(10, 10, 5, '2024-02-05');

-- --------------------------------------------------------

--
-- Estrutura da tabela `notas`
--

CREATE TABLE `notas` (
  `id_nota` int(11) NOT NULL,
  `id_matricula` int(11) NOT NULL,
  `id_avaliacao` int(11) NOT NULL,
  `nota` decimal(4,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `notas`
--

INSERT INTO `notas` (`id_nota`, `id_matricula`, `id_avaliacao`, `nota`) VALUES
(1, 1, 1, '8.50'),
(2, 1, 2, '7.00'),
(3, 2, 1, '9.00'),
(4, 2, 2, '8.00'),
(5, 3, 3, '7.50'),
(6, 3, 4, '9.00'),
(7, 4, 3, '6.00'),
(8, 4, 4, '8.50'),
(9, 5, 5, '9.50'),
(10, 5, 6, '8.00');

-- --------------------------------------------------------

--
-- Estrutura da tabela `professores`
--

CREATE TABLE `professores` (
  `id_professor` int(11) NOT NULL,
  `nome_completo` varchar(255) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `endereco_rua` varchar(255) DEFAULT NULL,
  `endereco_numero` varchar(10) DEFAULT NULL,
  `endereco_complemento` varchar(50) DEFAULT NULL,
  `endereco_bairro` varchar(100) DEFAULT NULL,
  `endereco_cidade` varchar(100) DEFAULT NULL,
  `endereco_estado` varchar(50) DEFAULT NULL,
  `endereco_cep` varchar(10) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `numero_registro` varchar(20) NOT NULL,
  `areas_especializacao` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `professores`
--

INSERT INTO `professores` (`id_professor`, `nome_completo`, `data_nascimento`, `endereco_rua`, `endereco_numero`, `endereco_complemento`, `endereco_bairro`, `endereco_cidade`, `endereco_estado`, `endereco_cep`, `telefone`, `email`, `numero_registro`, `areas_especializacao`) VALUES
(1, 'Carlos Alberto', '1975-03-15', 'Rua dos Professores', '50', NULL, 'Laranjeiras', 'Rio de Janeiro', 'RJ', '22240-000', '(21) 98765-4321', 'carlos.alberto@email.com', 'PROF001', 'Matemática'),
(2, 'Ana Paula', '1982-07-20', 'Avenida Brasil', '1000', 'Sala 2', 'Penha', 'Rio de Janeiro', 'RJ', '21020-000', '(21) 91234-5678', 'ana.paula@email.com', 'PROF002', 'Português'),
(3, 'Ricardo Gomes', '1978-11-01', 'Rua da História', '25', 'Apto 301', 'Glória', 'Rio de Janeiro', 'RJ', '20240-000', '(21) 98877-6655', 'ricardo.gomes@email.com', 'PROF003', 'História'),
(4, 'Fernanda Marques', '1985-05-12', 'Travessa da Ciência', '150', NULL, 'Cidade Nova', 'Rio de Janeiro', 'RJ', '20211-000', '(21) 97654-3210', 'fernanda.marques@email.com', 'PROF004', 'Ciências'),
(5, 'Marcelo Oliveira', '1979-09-28', 'Alameda das Artes', '80', 'Casa 1', 'Catete', 'Rio de Janeiro', 'RJ', '22221-000', '(21) 96543-2109', 'marcelo.oliveira@email.com', 'PROF005', 'Geografia'),
(6, 'Patrícia Souza', '1983-01-05', 'Estrada do Conhecimento', '200', NULL, 'Jacarepaguá', 'Rio de Janeiro', 'RJ', '22750-000', '(21) 95432-1098', 'patricia.souza@email.com', 'PROF006', 'Inglês'),
(7, 'Gustavo Lima', '1977-06-18', 'Rua da Inovação', '30', 'Apto 103', 'Méier', 'Rio de Janeiro', 'RJ', '20720-000', '(21) 94321-0987', 'gustavo.lima@email.com', 'PROF007', 'Física'),
(8, 'Carla Rocha', '1986-10-22', 'Praça da Educação', '120', NULL, 'Andaraí', 'Rio de Janeiro', 'RJ', '20540-000', '(21) 93210-9876', 'carla.rocha@email.com', 'PROF008', 'Química'),
(9, 'Bruno Mendes', '1980-04-03', 'Avenida da Escola', '70', 'Sala 5', 'Madureira', 'Rio de Janeiro', 'RJ', '21310-000', '(21) 92109-8765', 'bruno.mendes@email.com', 'PROF009', 'Educação Física'),
(10, 'Juliana Costa', '1984-12-10', 'Travessa do Saber', '95', NULL, 'Campo Grande', 'Rio de Janeiro', 'RJ', '23050-000', '(21) 91098-7654', 'juliana.costa@email.com', 'PROF010', 'Artes');

-- --------------------------------------------------------

--
-- Estrutura da tabela `professores_disciplinas`
--

CREATE TABLE `professores_disciplinas` (
  `id_professor_disciplina` int(11) NOT NULL,
  `id_professor` int(11) NOT NULL,
  `id_disciplina` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `professores_disciplinas`
--

INSERT INTO `professores_disciplinas` (`id_professor_disciplina`, `id_professor`, `id_disciplina`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10);

-- --------------------------------------------------------

--
-- Estrutura da tabela `turmas`
--

CREATE TABLE `turmas` (
  `id_turma` int(11) NOT NULL,
  `nome_turma` varchar(50) NOT NULL,
  `ano_letivo` int(11) NOT NULL,
  `id_professor_responsavel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `turmas`
--

INSERT INTO `turmas` (`id_turma`, `nome_turma`, `ano_letivo`, `id_professor_responsavel`) VALUES
(1, '7º ano A', 2024, 1),
(2, '7º ano B', 2024, 2),
(3, '8º ano A', 2024, 3),
(4, '8º ano B', 2024, 4),
(5, '9º ano A', 2024, 5),
(6, '1º ano EM', 2024, 6),
(7, '2º ano EM', 2024, 7),
(8, '3º ano EM', 2024, 8),
(9, '6º ano A', 2025, 9),
(10, '6º ano B', 2025, 10);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`id_aluno`),
  ADD UNIQUE KEY `numero_matricula` (`numero_matricula`);

--
-- Índices para tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  ADD PRIMARY KEY (`id_avaliacao`),
  ADD KEY `id_disciplina` (`id_disciplina`),
  ADD KEY `id_turma` (`id_turma`);

--
-- Índices para tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  ADD PRIMARY KEY (`id_disciplina`),
  ADD UNIQUE KEY `codigo_disciplina` (`codigo_disciplina`);

--
-- Índices para tabela `matriculas`
--
ALTER TABLE `matriculas`
  ADD PRIMARY KEY (`id_matricula`),
  ADD UNIQUE KEY `id_aluno` (`id_aluno`,`id_turma`),
  ADD KEY `id_turma` (`id_turma`);

--
-- Índices para tabela `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`id_nota`),
  ADD UNIQUE KEY `id_matricula` (`id_matricula`,`id_avaliacao`),
  ADD KEY `id_avaliacao` (`id_avaliacao`);

--
-- Índices para tabela `professores`
--
ALTER TABLE `professores`
  ADD PRIMARY KEY (`id_professor`),
  ADD UNIQUE KEY `numero_registro` (`numero_registro`);

--
-- Índices para tabela `professores_disciplinas`
--
ALTER TABLE `professores_disciplinas`
  ADD PRIMARY KEY (`id_professor_disciplina`),
  ADD UNIQUE KEY `id_professor` (`id_professor`,`id_disciplina`),
  ADD KEY `id_disciplina` (`id_disciplina`);

--
-- Índices para tabela `turmas`
--
ALTER TABLE `turmas`
  ADD PRIMARY KEY (`id_turma`),
  ADD KEY `id_professor_responsavel` (`id_professor_responsavel`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `alunos`
--
ALTER TABLE `alunos`
  MODIFY `id_aluno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  MODIFY `id_avaliacao` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `disciplinas`
--
ALTER TABLE `disciplinas`
  MODIFY `id_disciplina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `matriculas`
--
ALTER TABLE `matriculas`
  MODIFY `id_matricula` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `notas`
--
ALTER TABLE `notas`
  MODIFY `id_nota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `professores`
--
ALTER TABLE `professores`
  MODIFY `id_professor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `professores_disciplinas`
--
ALTER TABLE `professores_disciplinas`
  MODIFY `id_professor_disciplina` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `turmas`
--
ALTER TABLE `turmas`
  MODIFY `id_turma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  ADD CONSTRAINT `avaliacoes_ibfk_1` FOREIGN KEY (`id_disciplina`) REFERENCES `disciplinas` (`id_disciplina`),
  ADD CONSTRAINT `avaliacoes_ibfk_2` FOREIGN KEY (`id_turma`) REFERENCES `turmas` (`id_turma`);

--
-- Limitadores para a tabela `matriculas`
--
ALTER TABLE `matriculas`
  ADD CONSTRAINT `matriculas_ibfk_1` FOREIGN KEY (`id_aluno`) REFERENCES `alunos` (`id_aluno`),
  ADD CONSTRAINT `matriculas_ibfk_2` FOREIGN KEY (`id_turma`) REFERENCES `turmas` (`id_turma`);

--
-- Limitadores para a tabela `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`id_matricula`) REFERENCES `matriculas` (`id_matricula`),
  ADD CONSTRAINT `notas_ibfk_2` FOREIGN KEY (`id_avaliacao`) REFERENCES `avaliacoes` (`id_avaliacao`);

--
-- Limitadores para a tabela `professores_disciplinas`
--
ALTER TABLE `professores_disciplinas`
  ADD CONSTRAINT `professores_disciplinas_ibfk_1` FOREIGN KEY (`id_professor`) REFERENCES `professores` (`id_professor`),
  ADD CONSTRAINT `professores_disciplinas_ibfk_2` FOREIGN KEY (`id_disciplina`) REFERENCES `disciplinas` (`id_disciplina`);

--
-- Limitadores para a tabela `turmas`
--
ALTER TABLE `turmas`
  ADD CONSTRAINT `turmas_ibfk_1` FOREIGN KEY (`id_professor_responsavel`) REFERENCES `professores` (`id_professor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
