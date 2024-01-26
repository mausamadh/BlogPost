user = []
blog = []
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_URL = "YOUR CONNECTION HERE"

engine = sa.create_engine(SQLALCHEMY_URL)
Base = declarative_base()
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionFactory()

    try:
        return db
    except:
        db.rollback()

    finally:
        db.close()


# db = get_db()
# res = db.execute(sa.text("SELECT 1"))
# for i in res:
#     print(i)
