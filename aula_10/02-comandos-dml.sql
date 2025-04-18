-- exibir/selecionar tudo de uma tabela

SELECT * FROM alunos;

-- ---------------------------------------
-- exibir/selecionar determinada(s) coluna(s) de uma tabela

SELECT nome_completo,email FROM alunos;

-- ---------------------------------------
-- aplicar filtros na exibição de determinada informação de uma coluna

SELECT nome_disciplina,carga_horaria
	FROM disciplinas 
	WHERE carga_horaria >= 60;

-- ---------------------------------------

SELECT nota
    FROM notas
    WHERE nota >=8.0 AND nota <=9.0;

-- ---------------------------------------

SELECT nome_completo, telefone, email
	FROM alunos

-- por padrão ele vai exibir as listas de acordo com a chave primária, para ordenar os registros de acordo com uma coluna, podemos usar o comando ORDER BY:

SELECT nome_completo, telefone, email
	FROM alunos
    ORDER BY nome_completo;

ou

SELECT nome_completo, telefone, email
	FROM alunos
    ORDER BY nome_completo DESC; -- para ordem decrescente

-- ---------------------------------------

SELECT nome_completo, numero_registro, areas_especializacao
	FROM professores
    ORDER BY nome_completo;

-- ---------------------------------------
-- para definir hierarquias na hora de organizar a ordenação, pode-se adicionar mais de um parâmetro como critério para o ORDER BY, por exemplo:

SELECT nome_completo, numero_registro, areas_especializacao
	FROM professores
    ORDER BY nome_completo, numero_registro;
    
    -- sabendo que o parâmetro que vem antes terá prioridade na ordem de organização, ele ordenará primeiramente por nome, em seguida, pelo número de registro.

-- ---------------------------------------
-- INNER JOIN: puxando informações cruzadas entre tabelas

SELECT P.nome_completo, T.nome_turma
	FROM professores P -- apelido para facilitar/diminuir o tamanho da frase/sintaxe
    INNER JOIN turmas T
    ON P.id_professor = T.id_professor_responsavel -- campo chave primária na tabela principal tem que ser == à chave estrangeira na segunda tabela

-- ---------------------------------------

SELECT A.nome_completo, M.data_matricula_turma
	FROM alunos A
    INNER JOIN matriculas M
    ON A.id_aluno = M.id_aluno

-- ---------------------------------------

SELECT A.nome_completo, M.data_matricula_turma, T.nome_turma
	FROM alunos A
    INNER JOIN matriculas M
    ON A.id_aluno = M.id_aluno
    INNER JOIN turmas T
    ON M.id_turma = T.id_turma
    ORDER BY M.data_matricula_turma DESC;

-- ---------------------------------------

SELECT P.nome_completo, P.areas_especializacao, D.nome_disciplina, carga_horaria
	FROM professores P
    INNER JOIN professores_disciplinas Pd
    ON P.id_professor = Pd.id_professor
    INNER JOIN disciplinas D
    ON Pd.id_disciplina = D.id_disciplina

-- ---------------------------------------

SELECT A.nome_completo, N.nota
    FROM alunos A
    INNER JOIN matriculas M
    ON A.id_aluno = M.id_matricula
    INNER JOIN notas N
    ON M.id_matricula = N.id_matricula
    ORDER BY N.nota DESC;

-- ---------------------------------------

SELECT A.nome_completo, N.nota, AV.tipo_avaliacao, D.nome_disciplina
    FROM alunos A
    INNER JOIN matriculas M
    ON A.id_aluno = M.id_matricula
    INNER JOIN notas N
    ON M.id_matricula = N.id_matricula
    INNER JOIN avaliacoes AV
    ON AV.id_avaliacao = N.id_avaliacao
    INNER JOIN disciplinas D
    ON D.id_disciplina = AV.id_disciplina
    ORDER BY N.nota DESC;

-- ---------------------------------------

SELECT A.nome_completo, N.nota, AV.tipo_avaliacao, D.nome_disciplina
    FROM alunos A
    INNER JOIN matriculas M
    ON A.id_aluno = M.id_matricula
    INNER JOIN notas N
    ON M.id_matricula = N.id_matricula
    INNER JOIN avaliacoes AV
    ON AV.id_avaliacao = N.id_avaliacao
    INNER JOIN disciplinas D
    ON D.id_disciplina = AV.id_disciplina
    ORDER BY D.nome_disciplina, N.nota DESC;

-- ---------------------------------------

SELECT A.nome_completo, N.nota, AV.tipo_avaliacao, D.nome_disciplina
    FROM alunos A
    INNER JOIN matriculas M
    ON A.id_aluno = M.id_matricula
    INNER JOIN notas N
    ON M.id_matricula = N.id_matricula
    INNER JOIN avaliacoes AV
    ON AV.id_avaliacao = N.id_avaliacao
    INNER JOIN disciplinas D
    ON D.id_disciplina = AV.id_disciplina
    WHERE av.tipo_avaliacao = 'Prova 1'
    ORDER BY D.nome_disciplina, N.nota DESC;