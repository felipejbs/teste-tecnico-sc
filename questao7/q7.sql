INSERT INTO clientes (nome, cpf, cidade)
SELECT nc.nome, nc.cpf, nc.cidade
FROM novos_clientes nc
WHERE nc.cpf NOT IN (
    SELECT cpf FROM clientes
);
