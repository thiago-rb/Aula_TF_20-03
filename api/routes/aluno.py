from flask import Blueprint, jsonify, request
import psycopg2

aluno_bp = Blueprint('aluno', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@aluno_bp.route('/', methods=['GET'])
def listar_alunos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Aluno")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(alunos)

@aluno_bp.route('/', methods=['POST'])
def criar_aluno():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Aluno (nome_completo, data_nascimento, id_turma, nome_responsavel, telefone_responsavel, email_responsavel, informacoes_adicionais)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (dados['nome_completo'], dados['data_nascimento'], dados['id_turma'], dados['nome_responsavel'], dados['telefone_responsavel'], dados['email_responsavel'], dados.get('informacoes_adicionais')))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Aluno criado com sucesso!"}), 201

@aluno_bp.route('/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Aluno
        SET nome_completo=%s, data_nascimento=%s, id_turma=%s, nome_responsavel=%s, telefone_responsavel=%s, email_responsavel=%s, informacoes_adicionais=%s
        WHERE id_aluno=%s
    """, (dados['nome_completo'], dados['data_nascimento'], dados['id_turma'], dados['nome_responsavel'], dados['telefone_responsavel'], dados['email_responsavel'], dados.get('informacoes_adicionais'), id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Aluno atualizado com sucesso!"})

@aluno_bp.route('/<int:id>', methods=['DELETE'])
def excluir_aluno(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Aluno WHERE id_aluno=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Aluno excluído com sucesso!"})