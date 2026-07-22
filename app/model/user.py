from ..db import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from ..exts import bcrypt
from typing import List
import uuid
from flask_login import UserMixin


class User(db.Model,UserMixin):
    id:Mapped[uuid.UUID]=mapped_column(primary_key=True,default=uuid.uuid4)
    name:Mapped[str]=mapped_column(String(25),nullable=False)
    email:Mapped[str]=mapped_column(String(25),nullable=False,unique=True)
    password:Mapped[str]=mapped_column(String(255))
    all_url:Mapped[List['Url']]=relationship(back_populates='author')

    def set_password(self, password: str):
        self.password = bcrypt.generate_password_hash(
            password,
        )

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    @classmethod
    def get_by_email(cls,email)-> User:
        return cls.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
