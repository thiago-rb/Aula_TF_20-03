from flask import Blueprint, jsonify, request
import psycopg2

turma_bp = Blueprint('turma', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@turma_bp.route('/', methods=['GET'])
def listar_turmas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Turma")
    turmas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(turmas)

@turma_bp.route('/', methods=['POST'])
def criar_turma():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Turma (nome_turma, id_professor, horario)
        VALUES (%s, %s, %s)
    """, (dados['nome_turma'], dados['id_professor'], dados['horario']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Turma criada com sucesso!"}), 201

@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Turma
        SET nome_turma=%s, id_professor=%s, horario=%s
        WHERE id_turma=%s
    """, (dados['nome_turma'], dados['id_professor'], dados['horario'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Turma atualizada com sucesso!"})

@turma_bp.route('/<int:id>', methods=['DELETE'])
def excluir_turma(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Turma WHERE id_turma=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Turma excluída com sucesso!"})