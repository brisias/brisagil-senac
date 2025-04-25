INSERT INTO evento (idEvento,titulo,tipo_evento,descricao,capacidade_insc,datahora_inicio,datahora_fim,idLocal,idPalestrante,taxa_insc) VALUES
('2025DES015','Debulha: O que é que o Design tem?','Palestra','Revisão dos últimos anos da Semana de Design da UFRN',200,'05/05/2025 15:00:00','05/05/2025 17:00:00','DEP03AUD01','DSGN034',5.00),
('2025MAT028','Calculando de cabeça','Workshop','Oficina sobre cálculos rápidos usando seu computador biológico',20,'10/05/2025 09:00:00','10/05/2025 12:00:00','DEP04SAL05','MAT001',15.00);

-- --------------------------------------------------------

INSERT INTO local (idLocal,nome_local,tipo_local,setor,capacidade,recursos) VALUES
('DEP03AUD01','Auditório Professora Lorena Torres','Auditório','Departamento de Design (DepDSGN)',250,'ar-condicionado, projetor, microfones, caixas de som, cadeiras acolchoadas'),
('DEP04SAL05','Sala 05','Sala de aula','Setor de aulas 3',40,'ar-condicionado, projetor, quadro branco, cadeiras e mesas');

-- --------------------------------------------------------

INSERT INTO inscricao () VALUES
(),
();

-- --------------------------------------------------------

INSERT INTO participante () VALUES
(),
();

-- --------------------------------------------------------

INSERT INTO palestrante (idPalestrante,nome,contato,instituicao,mini_curriculo) VALUES
('DSGN034','Lourdes Lucrécia Silva','lu.lucrecia@ufrn.edu.br (84)99998-0000','UFRN','Doutora em Design Gráfico (UFPE)'),
('MAT001','Maurício Medeiros','mmat.medeiros@ufpb.edu.br (83)97777-3333','UFPB','Mestre em Estatística Descritiva (UFMG)');

-- --------------------------------------------------------

INSERT INTO certificado () VALUES
(),
();
