UPDATE tabela_destino tad
JOIN tabela_origem tao ON tad.id = tao.id
SET tad.nome = tao.nome,
    tad.email = tao.email,
    tad.status = tao.ativo,
    tad.data_ultima_atualizacao = NOW();
