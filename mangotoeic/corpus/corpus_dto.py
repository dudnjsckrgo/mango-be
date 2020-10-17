from sqlalchemy import Column, Integer 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class  Corpus(Base):
    __tablename__ ="Corpus"
    __table_args__={'mysql_collate':'utf8_general_ci'}
    id = Column(Integer, primary_key = True, index = True)
    CorId= Column(Integer)
    corpus = Column(VARCHAR(200))
    

    def __repr__(self):
        return f'Corpus(id=\'{self.id}\',CorId=\'{self.CorId}\',corpus=\'{self.corpus}\',)'

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'CorId' : self.corpus_Id,
            'corpus' : self.corpus,
            
        }



class UserDto(object):
    id: int
    corpus_Id: int
    corpus: str