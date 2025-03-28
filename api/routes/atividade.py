from flask import Blueprint, jsonify, request
import psycopg2

atividade_bp = Blueprint('atividade', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@atividade_bp.route('/', methods=['GET'])
def listar_atividades():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Atividade")
    atividades = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(atividades)

@atividade_bp.route('/', methods=['POST'])
def criar_atividade():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Atividade (descricao, data_realizacao)
        VALUES (%s, %s)
    """, (dados['descricao'], dados['data_realizacao']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Atividade criada com sucesso!"}), 201

@atividade_bp.route('/<int:id>', methods=['PUT'])
def atualizar_atividade(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Atividade
        SET descricao=%s, data_realizacao=%s
        WHERE id_atividade=%s
    """, (dados['descricao'], dados['data_realizacao'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Atividade atualizada com sucesso!"})

@atividade_bp.route('/<int:id>', methods=['DELETE'])
def excluir_atividade(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Atividade WHERE id_atividade=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Atividade excluída com sucesso!"})