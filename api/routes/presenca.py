from flask import Blueprint, jsonify, request
import psycopg2

presenca_bp = Blueprint('presenca', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@presenca_bp.route('/', methods=['GET'])
def listar_presencas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Presenca")
    presencas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(presencas)

@presenca_bp.route('/', methods=['POST'])
def criar_presenca():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Presenca (id_aluno, data_presenca, presente)
        VALUES (%s, %s, %s)
    """, (dados['id_aluno'], dados['data_presenca'], dados['presente']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Presença registrada com sucesso!"}), 201

@presenca_bp.route('/<int:id>', methods=['PUT'])
def atualizar_presenca(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Presenca
        SET id_aluno=%s, data_presenca=%s, presente=%s
        WHERE id_presenca=%s
    """, (dados['id_aluno'], dados['data_presenca'], dados['presente'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Presença atualizada com sucesso!"})

@presenca_bp.route('/<int:id>', methods=['DELETE'])
def excluir_presenca(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Presenca WHERE id_presenca=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Presença excluída com sucesso!"})