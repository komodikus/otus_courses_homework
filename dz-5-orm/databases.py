import sqlite3
from models import values_of_table


def wrapstr(x):
    """ return 'str' if object is str"""
    if isinstance(x, str):
        return "'" + x + "'"
    else:
        return str(x)


class Database:
    def __init__(self, name_db):
        self._conn = sqlite3.connect(name_db, isolation_level=None)
        self._cur = self._conn.cursor()

    def create_table(self, name_table):
        if not name_table:
            raise Exception('Введите не пустое имя таблицы')
        try:
            self._cur.execute("""CREATE TABLE {}
                          ({});
                       """.format(name_table, values_of_table))
        except sqlite3.OperationalError:
            raise Exception('Таблица уже существует')

    def delete_table(self, name_table):
        self._cur.execute("""DROP TABLE IF EXISTS {};
                       """.format(name_table))

    def insert(self, name_table, columns, values):
        quoted_values = wrapstr(values.replace(' ', '').replace(',', '\',\''))
        # print("""INSERT INTO {name_table} ({columns})VALUES ({values});
        #                        """.format(name_table=name_table, columns=columns, values=quoted_values))
        try:
            self._cur.execute("""INSERT INTO {name_table} ({columns})VALUES ({values});
                               """.format(name_table=name_table, columns=columns, values=quoted_values))
        except sqlite3.OperationalError:
            print('Ошибка введенных данных')
        self._conn.commit()

    def insert_many(self, name_table, values):
        try:
            sql_request = ("INSERT INTO {name_table} VALUES ({question_marks_str})".format(name_table=name_table,
                                                                                           question_marks_str=', '.join(
                                                                                               ['?'] * len(values[0]))))
            self._cur.executemany(sql_request, values)
        except sqlite3.OperationalError:
            print('Ошибка введенных данных')
        self._conn.commit()

    def update(self, name_table, the_value_that_we_change, the_value_of_which_we_change, **kwargs):
        try:
            sql_expression = """UPDATE {name_table} SET {the_value_that_we_change} = {the_value_of_which_we_change}""".format(
                name_table=name_table, the_value_of_which_we_change='\'' + the_value_of_which_we_change + '\'',
                the_value_that_we_change=the_value_that_we_change)
        except sqlite3.OperationalError:
            print('Ошибка введенных данных')
        # print(sql_expression)
        if kwargs:
            def get_where_expression(expression):
                temporary_list = []
                for key, value in expression.items():
                    temporary_list.append('{}=\'{}\''.format(key, value))
                query_where = ' WHERE ' + ' AND '.join(temporary_list) if temporary_list else ''
                return query_where

            sql_expression += get_where_expression(kwargs)
            # print(sql_expression)
        self._conn.execute(sql_expression)
        self._conn.commit()

    def select(self, name_table, the_value_that_we_select, where):
        # print("SELECT {} FROM {}".format(the_value_that_we_select, name_table))
        #print("SELECT {} FROM {} WHERE {}".format(the_value_that_we_select, name_table, where))
        try:
            self._cur.execute("SELECT {} FROM {} WHERE {}".format(the_value_that_we_select, name_table, where))
            rows = self._cur.fetchall()
        except sqlite3.OperationalError:
            print('Ошибка введенных данных')
        #     print(*row)
        return rows

    def __close_db__(self):
        self._conn.close()


qwerty = Database('values')
qwerty.create_table('test_prm')
# qwerty.insert('hai', 'name,last_name,age', 'qwe,ssd,26')
# albums = [('huiae', 'Hunter', '45'),
#           ('Faces', 'QweRed', '23'),
#           ]
# qwerty.insert_many('hai', albums)

# print(qwerty.select('hai','last_name', 'name=\'eugen\''))
# qwerty.update('hai','name','kirill', name='zxc')
