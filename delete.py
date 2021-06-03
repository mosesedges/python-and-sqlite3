import sqlite3

db = sqlite3.connect('data.db')

db.execute('DELETE FROM users WHERE id = ?',
           ('<function uuid4 at 0x000001DD33D0D040>',))

db.commit()
