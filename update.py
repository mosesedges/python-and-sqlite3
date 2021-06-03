import sqlite3

db = sqlite3.connect('data.db')

db.execute('UPDATE users SET name = ?  WHERE id = ?',
           ('Alodia olunma', '<function uuid4 at 0x0000029B4036D040>'))

db.commit()
