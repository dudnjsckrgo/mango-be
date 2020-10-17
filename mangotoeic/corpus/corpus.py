from mangotoeic.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR ,LONGTEXT
class  Corpus(Base):
    __tablename__ ="Corpus"
    __table_args__={'mysql_collate':'utf8_general_ci'}
    id = Column(Integer, primary_key = True, index = True)

    corpus = Column(VARCHAR(200))


    def __repr__(self):
        return f'Corpus(id=\'{self.id}\',corpus=\'{self.corpus}\',)'
engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8',encoding='utf8',echo=True)        
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(Corpus(corpus ='thomas is so tired'))
query =session.query(Corpus).filter((Corpus.id==1))
print(query)
for i in query:
    print(i)
session.commit()