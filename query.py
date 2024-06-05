import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from main import DSN, Publisher, Book, Shop, Stock, Sale

# Подключение к БД
engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

# Задание №2

# Принятие имя или идентификатор издателя
input_value = input('Введите имя или идентификатор издателя: ')

# Поиск издателя по имени или идентификатору
if input_value.isdigit():
    publisher = session.query(Publisher).filter(
        (Publisher.name.ilike(f'%{input_value}%')) | (Publisher.id == int(input_value))
    ).first()
else:
    publisher = session.query(Publisher).filter(
        Publisher.name.ilike(f'%{input_value}%')
    ).first()

if publisher is None:
    print('Издатель не найден')
else:
    # Получение всех продаж книг этого издателя(автора)
    sales = session.query(Sale).join(Stock).join(Book).filter(Book.publisher == publisher).order_by(Sale.date_sale.desc()).all()

    # Вывод информации о каждой покупке
    for sale in sales:
        date_str = sale.date_sale.strftime('%d-%m-%Y')
        print(f'{sale.stock.book.title} | {sale.stock.shop.name} | {sale.price} | {date_str}')