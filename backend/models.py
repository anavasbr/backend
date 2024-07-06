from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()
ma = Marshmallow()

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    prazo = db.Column(db.DateTime, nullable=False)

class TarefaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarefa

tarefa_schema = TarefaSchema()
tarefas_schema = TarefaSchema(many=True)
