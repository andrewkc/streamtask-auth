
from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Rol(db.Model):
    __tablename__ = 'rol'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Rol {}>'.format(self.name)


class Action(db.Model):
    __tablename__ = 'action'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Action {}>'.format(self.name)


class Permission(db.Model):
    __tablename__ = 'permission'
    __table_args__ = {'schema': 'authentication'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Permission {}>'.format(self.name)


class PermissionAction(db.Model):
    __tablename__ = 'permission_action'
    __table_args__ = {'schema': 'authentication'}

    id_permission = db.Column(db.Integer, db.ForeignKey('permission.id'), primary_key=True)
    id_action = db.Column(db.Integer, db.ForeignKey('action.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<PermissionAction {}-{}>'.format(self.id_permission, self.id_action)

class UserRol(db.Model):
    __tablename__ = 'user_rol'
    __table_args__ = {'schema': 'authentication'}

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('rol.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<UserRol {}>'.format(self.id_user)
