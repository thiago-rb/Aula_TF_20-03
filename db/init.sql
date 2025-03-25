-- Configuração para o encoding do banco de dados
-- Certifique-se de que o banco "escola" seja criado com ENCODING 'UTF8'
CREATE DATABASE escola ENCODING 'UTF8';

-- Criação da tabela 'alunos'
CREATE TABLE IF NOT EXISTS alunos (
    aluno_id CHARACTER VARYING(5) NOT NULL PRIMARY KEY,
    nome CHARACTER VARYING(40) NOT NULL,
    endereco CHARACTER VARYING(60),
    cidade CHARACTER VARYING(15),
    estado CHARACTER VARYING(15),
    cep CHARACTER VARYING(10),
    pais CHARACTER VARYING(15),
    telefone CHARACTER VARYING(24)
);

-- Inserindo registros iniciais (evita duplicados usando 'ON CONFLICT DO NOTHING')
INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('001', 'João Silva', 'Rua Agosto', 'São Paulo', 'SP', '01001-000', 'Brasil', '923456789'),
('002', 'Maria Lima', 'Rua Fernando Salles', 'São Paulo', 'SP', '02002-000', 'Brasil', '987654321'),
('003', 'Carlos Souza', 'Rua Cariri', 'Belo Horizonte', 'MG', '03003-000', 'Brasil', '912233445'),
('004', 'Ana Pereira', 'Rua Vale da Paz', 'Curitiba', 'PR', '04004-000', 'Brasil', '956677889'),
('005', 'Paulo Oliveira', 'Rua Anhanguera', 'Florianópolis', 'SC', '05005-000', 'Brasil', '967788990'),
('006', 'Laura Santos', 'Rua dos Lírios', 'Fortaleza', 'CE', '06006-000', 'Brasil', '978899001'),
('007', 'Bruno Costa', 'Rua Juvenal', 'Manaus', 'AM', '07007-000', 'Brasil', '989900112'),
('008', 'Clara Nunes', 'Rua das Flores', 'Salvador', 'BA', '08008-000', 'Brasil', '990011223'),
('009', 'Rafael Almeida', 'Rua Cambucá', 'Recife', 'PE', '09009-000', 'Brasil', '901122334'),
('010', 'Fernanda Souza', 'Rua Damasco', 'Porto Alegre', 'RS', '10010-000', 'Brasil', '923123123')
ON CONFLICT (aluno_id) DO NOTHING;