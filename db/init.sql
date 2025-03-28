-- Criação das tabelas
CREATE TABLE Aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    id_turma INT,
    nome_responsavel VARCHAR(255) NOT NULL,
    telefone_responsavel VARCHAR(20) NOT NULL,
    email_responsavel VARCHAR(100) NOT NULL,
    informacoes_adicionais TEXT,
    FOREIGN KEY (id_turma) REFERENCES Turma(id_turma)
);

CREATE TABLE Turma (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome_turma VARCHAR(50) NOT NULL,
    id_professor INT,
    horario VARCHAR(100) NOT NULL,
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
    id_aluno INT NOT NULL,
    data_pagamento DATE NOT NULL,
    valor_pago DECIMAL(10, 2) NOT NULL,
    forma_pagamento VARCHAR(50) NOT NULL,
    referencia VARCHAR(100),
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

CREATE TABLE Presenca (
    id_presenca INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
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
    id_atividade INT NOT NULL,
    id_aluno INT NOT NULL,
    PRIMARY KEY (id_atividade, id_aluno),
    FOREIGN KEY (id_atividade) REFERENCES Atividade(id_atividade),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nivel_acesso VARCHAR(20) NOT NULL,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES Professor(id_professor)
);

-- Inserção de dados
INSERT INTO Professor (nome_completo, email, telefone) VALUES
('Ana Souza', 'ana.souza@escola.com', '11987654321'),
('Carlos Pereira', 'carlos.pereira@escola.com', '11912345678');

INSERT INTO Turma (nome_turma, id_professor, horario) VALUES
('Turma A', 1, '08:00 - 12:00'),
('Turma B', 2, '13:00 - 17:00');

INSERT INTO Aluno (nome_completo, data_nascimento, id_turma, nome_responsavel, telefone_responsavel, email_responsavel, informacoes_adicionais) VALUES
('João Silva', '2010-05-22', 1, 'Maria Silva', '11987654322', 'maria.silva@gmail.com', 'Sem alergias'),
('Luiza Almeida', '2011-08-15', 2, 'Pedro Almeida', '11912345679', 'pedro.almeida@gmail.com', NULL);

INSERT INTO Pagamento (id_aluno, data_pagamento, valor_pago, forma_pagamento, referencia, status) VALUES
(1, '2025-03-15', 500.00, 'Cartão', 'Mensalidade Março', 'Pago'),
(2, '2025-03-16', 500.00, 'Boleto', 'Mensalidade Março', 'Pendente');

INSERT INTO Presenca (id_aluno, data_presenca, presente) VALUES
(1, '2025-03-20', TRUE),
(2, '2025-03-20', FALSE);

INSERT INTO Atividade (descricao, data_realizacao) VALUES
('Pintura de paisagens', '2025-03-25'),
('Montagem de quebra-cabeça', '2025-03-26');

INSERT INTO Atividade_Aluno (id_atividade, id_aluno) VALUES
(1, 1),
(2, 2);

INSERT INTO Usuario (login, senha, nivel_acesso, id_professor) VALUES
('admin', 'hash_senha_admin', 'administrador', NULL),
('carlos.professor', 'hash_senha_carlos', 'professor', 2);