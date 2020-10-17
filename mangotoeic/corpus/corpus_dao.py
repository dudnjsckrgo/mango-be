from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mangotoeic.ext.db import Base
from mangotoeic.corpus import Corpus
import pandas as pd
'''
어플리케이션이 SQLAlchemy ORM을 사용한다면, 
객체에 바인딩된 쿼리를 위해서 Session 객체를 사용해야 한다. 
이는 session.add(), session.rollback(), session.commit(), session.close()를 통해 
트랜잭션을 단일 작업 단위로 관리하기 좋고, 
이러한 특징을 통해 Python의 Context Manager 패턴을 사용하기에도 좋다.
'''
class CorpusDao():
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def insert_corpus(self):
        session.add(Corpus(corpus_Id=1,corpus ='thomas is so tired'))
        session.commit()

    def fetch_corpus(self):
        query = session.query(Corpus).filter((Corpus.id == 1))
        return query[0]

    def fetch_all_corpuses(self):
        querys = self.session.query(Corpus).all()
        return querys

    def update_corpus(self, corpus_id, column, value):
        corpus = self.session.query(Corpus).filter(Corpus.corpus_id == corpus_id).update({column : value})
        self.session.commit()

    def delete_corpus(self, corpus_id):
        corpus = self.session.query(Corpus).filter(Corpus.corpus_id == corpus_id).first()
        self.session.delete(corpus)
        self.session.commit()
    def corpusdata_to_sql(self,data_path):
        data_path
        df = pd.read_csv(data_path) # 정제된 데이터로 변경 예정
        # df_sample = df[['user_id', 'content_id', 'user_answer', 'answered_correctly', 'prior_question_elapsed_time']]
        # df_sample_head = df_sample.head(100)
        self.conn = self.engine.connect()
        # self.base.metadata.create_all(self.engine)
        df.to_sql(name='Corpus', con=self.conn, if_exists='append', index=False)
if __name__ == "__main__":
    corpusdao = CorpusDao()
    # userdao.userdata_to_sql()
    # userdao.add_user('666')
    # userdao.delete_user('115')
    corpusdao.update_corpus('5382', 'content_id', '777')
    