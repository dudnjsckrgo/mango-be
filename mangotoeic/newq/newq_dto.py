from mangotoeic.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR ,LONGTEXT,CHAR
class  NewQ(Base):
    __tablename__ ="NewQ"
    __table_args__={'mysql_collate':'utf8_general_ci'}
    id = Column(Integer, primary_key = True, index = True)

    Qid = Column(Integer)
    question = Column(VARCHAR(300))
    AnsA = Column(CHAR(10))
    AnsB = Column(CHAR(10))
    AnsC = Column(CHAR(10))
    AnsD = Column(CHAR(10))
    Answer = Column(CHAR(1))

    def __repr__(self):
        return f'Corpus(id=\'{self.id}\',AnsA=\'{self.AnsA}\',AnsB=\'{self.AnsB}\',AnsC=\'{self.AnsC}\',AnsD=\'{self.AnsD}\',Answer=\'{self.Answer}\',)'

    @property
    def serialize(self):
        return {
            'Qid' : self.Qid,
            'question' : self.question,
            'AnsA' : self.AnsA,
            'AnsB' : self.AnsB,
            'AnsC' : self.AnsC,
            'AnsD' : self.AnsD,
            'Answer' : self.Answer,
        }



class NewQDto(object):
    id: int
    Qid: int
    question: str
    AnsA: str
    AnsB: str
    AnsC: str
    AnsD: str
    Answer: str