from flask import Blueprint, jsonify, request
import psycopg2

pagamento_bp = Blueprint('pagamento', __name__)

def connect_db():
    return psycopg2.connect(
        host="db",
        database="escola",
        user="postgres",
        password="postgres"
    )

@pagamento_bp.route('/', methods=['GET'])
def listar_pagamentos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pagamento")
    pagamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(pagamentos)

@pagamento_bp.route('/', methods=['POST'])
def criar_pagamento():
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Pagamento (id_aluno, data_pagamento, valor_pago, forma_pagamento, referencia, status)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (dados['id_aluno'], dados['data_pagamento'], dados['valor_pago'], dados['forma_pagamento'], dados['referencia'], dados['status']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Pagamento registrado com sucesso!"}), 201

@pagamento_bp.route('/<int:id>', methods=['PUT'])
def atualizar_pagamento(id):
    dados = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Pagamento
        SET id_aluno=%s, data_pagamento=%s, valor_pago=%s, forma_pagamento=%s, referencia=%s, status=%s
        WHERE id_pagamento=%s
    """, (dados['id_aluno'], dados['data_pagamento'], dados['valor_pago'], dados['forma_pagamento'], dados['referencia'], dados['status'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Pagamento atualizado com sucesso!"})

@pagamento_bp.route('/<int:id>', methods=['DELETE'])
def excluir_pagamento(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pagamento WHERE id_pagamento=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Pagamento excluído com sucesso!"})