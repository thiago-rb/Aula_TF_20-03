from flask import Blueprint, jsonify, request
import psycopg2

usuario_bp = Blueprint('usuario', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

# Rota para listar todos os usuários
@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuario")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)

# Rota para criar um novo usuário
@usuario_bp.route('/', methods=['POST'])
def criar_usuario():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Usuario (login, senha, nivel_acesso, id_professor)
        VALUES (%s, %s, %s, %s)
    """, (dados['login'], dados['senha'], dados['nivel_acesso'], dados.get('id_professor')))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário criado com sucesso!"}), 201

# Rota para atualizar um usuário existente
@usuario_bp.route('/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Usuario
        SET login=%s, senha=%s, nivel_acesso=%s, id_professor=%s
        WHERE id_usuario=%s
    """, (dados['login'], dados['senha'], dados['nivel_acesso'], dados.get('id_professor'), id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário atualizado com sucesso!"})

# Rota para excluir um usuário
@usuario_bp.route('/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuario WHERE id_usuario=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário excluído com sucesso!"})