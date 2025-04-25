-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 25-Abr-2025 às 00:14
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
-- Banco de dados: `sisgevent`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `certificado`
--

CREATE TABLE `certificado` (
  `idCertificado` int(11) NOT NULL,
  `carga_horaria` varchar(3) NOT NULL,
  `idInscricao` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `evento`
--

CREATE TABLE `evento` (
  `idEvento` varchar(13) NOT NULL,
  `titulo` varchar(50) NOT NULL,
  `tipo_evento` varchar(25) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `datahora_inicio` varchar(20) NOT NULL,
  `datahora_fim` varchar(20) NOT NULL,
  `taxa_insc` float DEFAULT NULL,
  `capacidade_insc` int(11) NOT NULL,
  `idLocal` varchar(13) NOT NULL,
  `idPalestrante` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `evento`
--

INSERT INTO `evento` (`idEvento`, `titulo`, `tipo_evento`, `descricao`, `datahora_inicio`, `datahora_fim`, `taxa_insc`, `capacidade_insc`, `idLocal`, `idPalestrante`) VALUES
('2025DES015', 'Debulha: O que é que o Design tem?', 'Palestra', 'Revisão dos últimos anos da Semana de Design da UFRN', '05/05/2025 15:00:00', '05/05/2025 17:00:00', 5, 200, 'DEP03AUD01', 'DSGN034'),
('2025MAT028', 'Calculando de cabeça', 'Workshop', 'Oficina sobre cálculos rápidos usando seu computador biológico', '10/05/2025 09:00:00', '10/05/2025 12:00:00', 15, 20, 'DEP04SAL05', 'MAT001');

-- --------------------------------------------------------

--
-- Estrutura da tabela `inscricao`
--

CREATE TABLE `inscricao` (
  `idInscricao` varchar(13) NOT NULL,
  `datahora_registro` varchar(20) NOT NULL,
  `situacao` varchar(20) NOT NULL,
  `presenca` varchar(15) DEFAULT NULL,
  `cpf` varchar(14) NOT NULL,
  `idEvento` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `local`
--

CREATE TABLE `local` (
  `idLocal` varchar(13) NOT NULL,
  `nome_local` varchar(50) NOT NULL,
  `tipo_local` varchar(30) NOT NULL,
  `setor` varchar(50) NOT NULL,
  `capacidade` int(11) NOT NULL,
  `recursos` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `local`
--

INSERT INTO `local` (`idLocal`, `nome_local`, `tipo_local`, `setor`, `capacidade`, `recursos`) VALUES
('DEP03AUD01', 'Auditório Professora Lorena Torres', 'Auditório', 'Departamento de Design (DepDSGN)', 250, 'ar-condicionado, projetor, microfones, caixas de som, cadeiras acolchoadas'),
('DEP04SAL05', 'Sala 05', 'Sala de aula', 'Setor de aulas 3', 40, 'ar-condicionado, projetor, quadro branco, cadeiras e mesas');

-- --------------------------------------------------------

--
-- Estrutura da tabela `palestrante`
--

CREATE TABLE `palestrante` (
  `idPalestrante` varchar(13) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `contato` varchar(100) NOT NULL,
  `mini_curriculo` varchar(100) NOT NULL,
  `instituicao` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `palestrante`
--

INSERT INTO `palestrante` (`idPalestrante`, `nome`, `contato`, `mini_curriculo`, `instituicao`) VALUES
('DSGN034', 'Lourdes Lucrécia Silva', 'lu.lucrecia@ufrn.edu.br (84)99998-0000', 'Doutora em Design Gráfico (UFPE)', 'UFRN'),
('MAT001', 'Maurício Medeiros', 'mmat.medeiros@ufpb.edu.br (83)97777-3333', 'Mestre em Estatística Descritiva (UFMG)', 'UFPB');

-- --------------------------------------------------------

--
-- Estrutura da tabela `participante`
--

CREATE TABLE `participante` (
  `cpf` varchar(14) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `email` varchar(60) NOT NULL,
  `telefone` varchar(14) NOT NULL,
  `categoria` varchar(25) NOT NULL,
  `instituicao` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `certificado`
--
ALTER TABLE `certificado`
  ADD PRIMARY KEY (`idCertificado`),
  ADD KEY `idInscricao` (`idInscricao`);

--
-- Índices para tabela `evento`
--
ALTER TABLE `evento`
  ADD PRIMARY KEY (`idEvento`,`titulo`),
  ADD KEY `idLocal` (`idLocal`),
  ADD KEY `idPalestrante` (`idPalestrante`);

--
-- Índices para tabela `inscricao`
--
ALTER TABLE `inscricao`
  ADD PRIMARY KEY (`idInscricao`),
  ADD KEY `cpf` (`cpf`),
  ADD KEY `idEvento` (`idEvento`);

--
-- Índices para tabela `local`
--
ALTER TABLE `local`
  ADD PRIMARY KEY (`idLocal`);

--
-- Índices para tabela `palestrante`
--
ALTER TABLE `palestrante`
  ADD PRIMARY KEY (`idPalestrante`);

--
-- Índices para tabela `participante`
--
ALTER TABLE `participante`
  ADD PRIMARY KEY (`cpf`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `certificado`
--
ALTER TABLE `certificado`
  MODIFY `idCertificado` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `certificado`
--
ALTER TABLE `certificado`
  ADD CONSTRAINT `certificado_ibfk_1` FOREIGN KEY (`idInscricao`) REFERENCES `inscricao` (`idInscricao`);

--
-- Limitadores para a tabela `evento`
--
ALTER TABLE `evento`
  ADD CONSTRAINT `evento_ibfk_1` FOREIGN KEY (`idLocal`) REFERENCES `local` (`idLocal`),
  ADD CONSTRAINT `evento_ibfk_2` FOREIGN KEY (`idPalestrante`) REFERENCES `palestrante` (`idPalestrante`);

--
-- Limitadores para a tabela `inscricao`
--
ALTER TABLE `inscricao`
  ADD CONSTRAINT `inscricao_ibfk_1` FOREIGN KEY (`cpf`) REFERENCES `participante` (`cpf`),
  ADD CONSTRAINT `inscricao_ibfk_2` FOREIGN KEY (`idEvento`) REFERENCES `evento` (`idEvento`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
