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

CREATE TABLE Turma (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome_turma VARCHAR(50) NOT NULL,
    id_professor INT,
    horario VARCHAR(100),
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
);

CREATE TABLE Professor (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

CREATE TABLE Pagamento (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    data_pagamento DATE NOT NULL,
    valor_pago DECIMAL(10,2) NOT NULL,
    forma_pagamento VARCHAR(50),
    referencia VARCHAR(100),
    status VARCHAR(20),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

CREATE TABLE Presenca (
    id_presenca INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    data_presenca DATE NOT NULL,
    presente BOOLEAN NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

CREATE TABLE Atividade (
    id_atividade INT AUTO_INCREMENT PRIMARY KEY,
    descricao TEXT NOT NULL,
    data_realizacao DATE NOT NULL
);

CREATE TABLE Atividade_Aluno (
    id_atividade INT,
    id_aluno INT,
    PRIMARY KEY (id_atividade, id_aluno),
    FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nivel_acesso VARCHAR(20),
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
);