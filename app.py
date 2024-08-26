from helpers.logging import logger
from helpers.database import get_db_connection
from flask import Flask, request, jsonify
from Globals import *

app = Flask(__name__)

@app.route("/")
def index():
    logger.info("Página inicial acessada!")
    """Retorna a versão da API."""
    return jsonify({"versao": 1}), 200

def get_usuarios():
    """Obtém todos os usuários do banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tb_usuario')
    resultset = cursor.fetchall()
    usuarios = [
        {
            "id": linha["id"],
            "nome": linha["nome"],
            "nascimento": linha["nascimento"]
        }
        for linha in resultset
    ]
    conn.close()
    return usuarios

def set_usuario(data):
    """Cria um novo usuário no banco de dados."""
    nome = data.get('nome')
    nascimento = data.get('nascimento')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO tb_usuario (nome, nascimento) VALUES (%s, %s) RETURNING id',
        (nome, nascimento)
    )
    id = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    data['id'] = id
    return data

@app.route("/usuarios", methods=['GET', 'POST'])
def usuarios():
    """Gerencia listagem e criação de usuários."""
    if request.method == 'GET':
        usuarios = get_usuarios()
        return jsonify(usuarios), 200
    elif request.method == 'POST':
        data = request.json
        data = set_usuario(data)
        return jsonify(data), 201

def get_usuario_by_id(user_id):
    """Obtém um usuário específico pelo ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM tb_usuario WHERE id = %s',
        (user_id,)
    )
    linha = cursor.fetchone()
    usuario_dict = None
    if linha:
        usuario_dict = {
            "id": linha["id"],
            "nome": linha["nome"],
            "nascimento": linha["nascimento"]
        }
    conn.close()
    return usuario_dict

def update_usuario(user_id, data):
    """Atualiza os dados de um usuário existente."""
    nome = data.get('nome')
    nascimento = data.get('nascimento')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE tb_usuario SET nome = %s, nascimento = %s WHERE id = %s',
        (nome, nascimento, user_id)
    )
    row_update = cursor.rowcount
    conn.commit()
    conn.close()
    return row_update

def delete_usuario(user_id):
    """Remove um usuário do banco de dados pelo ID e retorna o nome do usuário excluído."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Buscar o nome do usuário antes de excluir
    cursor.execute('SELECT nome FROM tb_usuario WHERE id = %s', (user_id,))
    usuario = cursor.fetchone()
    
    if usuario:
        nome = usuario["nome"]
        cursor.execute('DELETE FROM tb_usuario WHERE id = %s', (user_id,))
        conn.commit()
        conn.close()
        return nome
    else:
        conn.close()
        return None

@app.route("/usuarios/<int:user_id>", methods=['GET', 'DELETE', 'PUT'])
def usuario(user_id):
    """Gerencia um usuário específico com base no ID."""
    if request.method == 'GET':
        usuario = get_usuario_by_id(user_id)
        if usuario:
            return jsonify(usuario), 200
        else:
            return jsonify({}), 404
    elif request.method == 'PUT':
        data = request.json
        row_update = update_usuario(user_id, data)
        if row_update:
            return jsonify(data), 200
        else:
            return jsonify(data), 304
    elif request.method == 'DELETE':
        nome = delete_usuario(user_id)
        if nome:
            return jsonify({"message": f"Usuário '{nome}' foi excluído com sucesso."}), 200
        else:
            return jsonify({"message": "Usuário não encontrado."}), 404

if __name__ == "__main__":
    app.run(debug=True)
