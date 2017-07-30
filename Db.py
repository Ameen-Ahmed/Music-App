import sqlite3

class Cache:
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

    def check_data(self, song, artist):
        cursor = self.db.execute('SELECT (Song, Artist) FROM {}'.format(self.table))
        for row in cursor:
            if song == row['Song'] and artist == row['Artist']:
                return True
        return False

# def main():
#     pass
# if __name__ == '__main__':
#     main()