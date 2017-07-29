import sqlite3

class Cache_db:
    def __init__(self, providers, **kwargs):
        self.filename = kwargs.get('filename', 'cache')
        self.table = kwargs.get('table', 'recent')
        self.db = sqlite3.connect(self.filename)
        create_str = 'CREATE TABLE IF NOT EXISTS {} (Song TEXT, Artist TEXT, '
        for key, value in providers.items():
            create_str += key + ' TEXT, '
        create_str = create_str + 'Time TEXT)'
        self.db.execute(create_str.format(self.table))
        self.count = 0

    def insert(self, row):
        self.count =+ 1
        self.db.execute('INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?)'.format(self.table), row)

    def disp_rows(self):
        cursor = self.db.execute('SELECT * FROM {} ORDER BY Time'.format(self.table))
        return cursor
def main():
    my_dict = {'Youtube': 1,
               'SoundCloud': 2,
               'Audiomack': 3}
    x = Cache_db(my_dict)
    x.insert(('Loud Pack', 'Tory Lanez', None, None, None, 'NOW'))
    for row in x.disp_rows():
        print(row)
if __name__ == '__main__':
    main()