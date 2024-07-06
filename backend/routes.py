from flask import request, jsonify
from .models import db, Tarefa, tarefa_schema, tarefas_schema
from datetime import datetime

def init_routes(app):
    @app.route('/cadastrar_tarefa', methods=['POST'])
    def cadastrar_tarefa():
        titulo = request.json['titulo']
        descricao = request.json.get('descricao', '')
        prazo_str = request.json['prazo']
        prazo = datetime.fromisoformat(prazo_str)
        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, prazo=prazo)
        db.session.add(nova_tarefa)
        db.session.commit()
        return jsonify(tarefa_schema.dump(nova_tarefa))

    @app.route('/buscar_tarefas', methods=['GET'])
    def buscar_tarefas():
        todas_tarefas = Tarefa.query.all()
        result = tarefas_schema.dump(todas_tarefas)
        return jsonify(result)

    @app.route('/editar_tarefa/<id>', methods=['PUT'])
    def editar_tarefa(id):
        tarefa = Tarefa.query.get(id)
        tarefa.titulo = request.json['titulo']
        tarefa.descricao = request.json.get('descricao', tarefa.descricao)
        prazo_str = request.json['prazo']
        tarefa.prazo = datetime.fromisoformat(prazo_str)
        db.session.commit()
        return jsonify(tarefa_schema.dump(tarefa))

    @app.route('/deletar_tarefa/<id>', methods=['DELETE'])
    def deletar_tarefa(id):
        tarefa = Tarefa.query.get(id)
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify(tarefa_schema.dump(tarefa))
