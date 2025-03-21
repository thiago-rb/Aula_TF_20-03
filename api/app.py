from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configurações do banco de dados
DB_CONFIG = {
    "dbname": "escola",
    "user": "postgres",
    "password": "postgres",
    "host": "db",
    "port": "5432"
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alunos;")
        alunos = cursor.fetchall()
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.get_json()
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (data['aluno_id'], data['nome'], data.get('endereco'), data.get('cidade'),
             data.get('estado'), data.get('cep'), data.get('pais'), data.get('telefone'))
        )
        conn.commit()
    return jsonify({"message": "Aluno cadastrado com sucesso!"}), 201

@app.route('/alunos/<id>', methods=['PUT'])
def atualizar_aluno(id):
    data = request.get_json()
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE alunos SET nome = %s, endereco = %s, cidade = %s, estado = %s, cep = %s, pais = %s, telefone = %s WHERE aluno_id = %s",
            (data['nome'], data.get('endereco'), data.get('cidade'), data.get('estado'),
             data.get('cep'), data.get('pais'), data.get('telefone'), id)
        )
        conn.commit()
    return jsonify({"message": "Aluno atualizado com sucesso!"})

@app.route('/alunos/<id>', methods=['DELETE'])
def excluir_aluno(id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM alunos WHERE aluno_id = %s", (id,))
        conn.commit()
    return jsonify({"message": "Aluno excluído com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
