from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for


db = SQLAlchemy()


class Base(db.Model):
    """ 所有 model 的一个基类，默认添加了时间戳 """
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base, UserMixin):

    __tablename__ = 'user'
    # 用数值表示角色，方便判断是否有权限, 比如说有个操作要角色为员工
    # 以及上的用户才可以做，那么只要判断 user.role >= ROLE_STAFF
    # 就可以了，数值之间设置了 10 的间隔是为了方便以后加入其它角色
    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    job = db.Column(db.String(64))

    publish_courses = db.relationship('Course')
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        """ Python 风格 getter """
        return self._password
    
    @password.setter
    def password(self, orig_password):
        """ Python 风格的 setter 这样设置 user.password 就会自动为 password 生成哈希值存入 _passowrd 字段 """
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        """ 判断用户输入的密码和存储的 hasd 密码是否相等 """
        return check_password_hash(self._password, password)
    

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_staff(self):
        return self.role == self.ROLE_STAFF


class Course(Base):

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    description = db.Column(db.String(256))
    image_url = db.Column(db.String(256))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'))
    author = db.relationship('User', uselist=False)
    chapters = db.relationship('Chapter')
    
    def __repr__(self):
        return '<Course:{}>'.format(self.name)

    @property
    def url(self):
        return url_for('course.detail', course_id = self.id)


class Chapter(Base):
    __tablename__ = 'chapter'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(256))
    video_url = db.Column(db.String(256))
    video_duration = db.Column(db.String(24))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'))
    course = db.relationship('Course', uselist=False)

    def __repr__(self):
        return '<Chapter:{}>'.format(self.name)