from ..db import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
import uuid
from sqlalchemy import ForeignKey
from datetime import datetime

class Url(db.Model):
    id:Mapped[uuid.UUID]=mapped_column(primary_key=True,default=uuid.uuid7)
    original_url:Mapped[str]=mapped_column(nullable=False)
    slug:Mapped[str]=mapped_column(nullable=False)
    nb_click:Mapped[int]=mapped_column(default=0)
    date_creation:Mapped[datetime]=mapped_column(default=datetime.utcnow)
    date_expirate:Mapped[datetime| None]
    id_author:Mapped[uuid.UUID]=mapped_column(ForeignKey('user.id'))
    author:Mapped['User']=relationship(back_populates='all_url')

    def save(self):
        db.session.add(self)
        db.session.commit()