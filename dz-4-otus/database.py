from peewee import Model, SqliteDatabase, CharField, AutoField


db = SqliteDatabase('ware.db')


class Wares(Model):
    name = CharField()
    description = CharField()
    long_description = CharField()
    price = CharField()
    image = CharField()
    color = CharField()
    id_ware = AutoField(primary_key=True)

    class Meta:
        database = db  #


db.connect()
db.create_tables([Wares, ])

# Код необходимый для создания рандомных фейковых данных в БД, при необхдимости раскоментировать, использовать
# import mimesis
# import time
# for number in range(0, 30):
#     Wares.create(name=mimesis.Food(locale='ru').dish(),
#                  description=mimesis.Text(locale='ru').text(quantity=1),
#                  long_description=mimesis.Text(locale='ru').text(quantity=4),
#                  price=mimesis.Business(locale='en').price(minimum=10, maximum=50),
#                  image=mimesis.Internet.stock_image(width=320,height=240,keywords=['eat','food', 'breakfast']),
#                  color=mimesis.Text(locale='ru').color())
#     print(number)
#     time.sleep(2)


query = Wares.select()
