from flask import Blueprint, jsonify, request
import psycopg2

atividade_aluno_bp = Blueprint('atividade_aluno', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@atividade_aluno_bp.route('/', methods=['GET'])
def listar_atividades_alunos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Atividade_Aluno")
    atividades_alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(atividades_alunos)

@atividade_aluno_bp.route('/', methods=['POST'])
def criar_atividade_aluno():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Atividade_Aluno (id_atividade, id_aluno)
        VALUES (%s, %s)
    """, (dados['id_atividade'], dados['id_aluno']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Associação entre Atividade e Aluno criada com sucesso!"}), 201

@atividade_aluno_bp.route('/', methods=['DELETE'])
def excluir_atividade_aluno():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Atividade_Aluno
        WHERE id_atividade=%s AND id_aluno=%s
    """, (dados['id_atividade'], dados['id_aluno']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Associação entre Atividade e Aluno excluída com sucesso!"})