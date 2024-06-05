import json
import sqlalchemy as sq
from main import DSN, Publisher, Book, Shop, Stock, Sale
from sqlalchemy.orm import sessionmaker

engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

# Задание №3

# Загрузка данных из JSON-файлов
with open('fixtures/tests_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Добавление данных в БД
for item in data:
    model = item['model']
    pk = item['pk']
    fields = item['fields']

    if model == 'publisher':
        publisher = Publisher(id=pk, name=fields['name'])
        session.add(publisher)
    elif model == 'book':
        book = Book(id=pk, title=fields['title'], id_publisher=fields['id_publisher'])
        session.add(book)
    elif model == 'shop':
        shop = Shop(id=pk, name=fields['name'])
        session.add(shop)
    elif model == 'stock':
        stock = Stock(id=pk, id_book=fields['id_book'], id_shop=fields['id_shop'], count=fields['count'])
        session.add(stock)
    elif model == 'sale':
        sale = Sale(id=pk, price=fields['price'], date_sale=fields['date_sale'], id_stock=fields['id_stock'], count=fields['count'])
        session.add(sale)

# Сохранение изменений в БД
session.commit()