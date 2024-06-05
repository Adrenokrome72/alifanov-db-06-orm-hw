import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

# Задание №1

DSN = "postgresql+psycopg2://postgres:postgrespassadm@localhost:5432/publisher_db?client_encoding=utf8"
engine = sq.create_engine(DSN)

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(150), nullable=False)
    books = relationship("Book", back_populates="publisher")

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(150), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))
    publisher = relationship(Publisher, back_populates="books")
    stocks = relationship("Stock", back_populates="book")

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer)
    book = relationship(Book, back_populates="stocks")
    shop = relationship("Shop", back_populates="stocks")
    sales = relationship("Sale", back_populates="stock")

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(150), nullable=False)
    stocks = relationship("Stock", back_populates="shop")

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer)
    stock = relationship(Stock, back_populates="sales")

Base.metadata.create_all(engine)
