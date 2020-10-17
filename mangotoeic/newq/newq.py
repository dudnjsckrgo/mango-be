from mangotoeic.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR ,LONGTEXT, CHAR
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
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8',encoding='utf8',echo=True)        
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(NewQ(AnsA ='fin',AnsB='fin2',AnsC='fin3',AnsD='fin4',Answer="A",question="im so tired", Qid=1))
query =session.query(NewQ).filter((NewQ.id==1))
print(query)
for i in query:
    print(i)
session.commit()