import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.connect_db')  # Mock para simular a função de conexão com o banco
def test_listar_alunos(mock_connect_db, client):
    # Simulando retorno do banco de dados
    mock_connect_db.return_value.__enter__.return_value.cursor.return_value.fetchall.return_value = [
        ("001", "João Silva", "Rua Agosto", "São Paulo", "SP", "01001-000", "Brasil", "923456789"),
        ("002", "Maria Lima", "Rua Fernando Salles", "São Paulo", "SP", "02002-000", "Brasil", "987654321"),
    ]
    response = client.get('/alunos')
    assert response.status_code == 200
    assert len(response.json) == 2

@patch('app.connect_db')  # Mock para simular a função de conexão com o banco
def test_cadastrar_aluno(mock_connect_db, client):
    response_mock = mock_connect_db.return_value.__enter__.return_value.cursor.return_value
    response_mock.rowcount = 1  # Simula que uma linha foi inserida

    novo_aluno = {
        "aluno_id": "011",
        "nome": "Novo Aluno",
        "endereco": "Rua Teste",
        "cidade": "Teste City",
        "estado": "TS",
        "cep": "11111-111",
        "pais": "Brasil",
        "telefone": "123456789"
    }
    response = client.post('/alunos', json=novo_aluno)
    assert response.status_code == 201
    assert response.json["message"] == "Aluno cadastrado com sucesso!"

@patch('app.connect_db')  # Mock para simular a função de conexão com o banco
def test_atualizar_aluno(mock_connect_db, client):
    response_mock = mock_connect_db.return_value.__enter__.return_value.cursor.return_value
    response_mock.rowcount = 1  # Simula que uma linha foi atualizada

    aluno_atualizado = {
        "nome": "Aluno Atualizado",
        "endereco": "Rua Atualizada",
        "cidade": "Atual City",
        "estado": "AT",
        "cep": "22222-222",
        "pais": "Brasil",
        "telefone": "987654321"
    }
    response = client.put('/alunos/011', json=aluno_atualizado)
    assert response.status_code == 200
    assert response.json["message"] == "Aluno atualizado com sucesso!"

@patch('app.connect_db')  # Mock para simular a função de conexão com o banco
def test_excluir_aluno(mock_connect_db, client):
    response_mock = mock_connect_db.return_value.__enter__.return_value.cursor.return_value
    response_mock.rowcount = 1  # Simula que uma linha foi excluída

    response = client.delete('/alunos/011')
    assert response.status_code == 200
    assert response.json["message"] == "Aluno excluído com sucesso!"