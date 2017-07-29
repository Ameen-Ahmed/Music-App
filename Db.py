import sqlite3

class Cache_db:
    def __init__(self, providers, **kwargs):
        self.filename = kwargs.get('filename', 'cache')
        self.table = kwargs.get('table', 'recent')
        self.db = sqlite3.connect(self.filename)
        create_str = 'CREATE TABLE IF NOT EXISTS {} ('
        for key, value in providers.items():
            create_str += key + 'TEXT, '
        create_str = create_str[-2] + ')'
        self.db.execute(create_str.format(self.table))

