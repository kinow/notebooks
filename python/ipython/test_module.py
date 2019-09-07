from sqlalchemy import Column, Integer


def get_column():
	c = Column('id', Integer, primary_key=True)
	return c
