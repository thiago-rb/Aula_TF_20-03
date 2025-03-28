from flask import Blueprint, jsonify, request
import psycopg2

professor_bp = Blueprint('professor', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@professor_bp.route('/', methods=['GET'])
def listar_professores():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Professor")
    professores = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(professores)

@professor_bp.route('/', methods=['POST'])
def criar_professor():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Professor (nome_completo, email, telefone)
        VALUES (%s, %s, %s)
    """, (dados['nome_completo'], dados['email'], dados['telefone']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Professor criado com sucesso!"}), 201

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Professor
        SET nome_completo=%s, email=%s, telefone=%s
        WHERE id_professor=%s
    """, (dados['nome_completo'], dados['email'], dados['telefone'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Professor atualizado com sucesso!"})

@professor_bp.route('/<int:id>', methods=['DELETE'])
def excluir_professor(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Professor WHERE id_professor=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Professor excluído com sucesso!"})