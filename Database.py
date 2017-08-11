# Ameen Ahmed
# github.com/Ameen-Ahmed/SongSearch

import sqlite3
import Web
from datetime import datetime

class Database:
    def __init__(self, providers, **kwargs):
        self.filename = kwargs.get('filename', 'cache.db')
        self.table = kwargs.get('table', 'recent')
        self.db = sqlite3.connect(self.filename)
        self.db.row_factory = sqlite3.Row
        create_str = 'CREATE TABLE IF NOT EXISTS {} (Song TEXT, Artist TEXT, '
        for key, value in providers.items():
            create_str += key + ' TEXT, '
        create_str = create_str + 'Time TEXT)'
        self.db.execute(create_str.format(self.table))

    def insert(self, row):
        row.append(datetime.strftime(datetime.now(), '%H:%M:%S'))
        self.db.execute('INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?)'.format(self.table), row)

    def retrieve(self, song, artist):
        cursor = self.db.execute('SELECT * FROM {} WHERE Song = ? AND Artist = ?'.format(self.table), (song, artist))
        return cursor.fetchone()

    def disp_rows(self):
        cursor = self.db.execute('SELECT * FROM {} ORDER BY Time'.format(self.table))
        for row in cursor.fetchall():
            print(tuple(row))

    def update_time(self, song, artist):
        self.db.execute('UPDATE {} SET Time = ? WHERE Song = ? AND Artist = ?'.format(
                self.table), (datetime.strftime(datetime.now(), '%H:%M:%S'), song, artist))

    def update(self, song, artist, key):
        self.update_time(song, artist)
        if self.db.execute('SELECT Song, Artist FROM {} WHERE ? = \'NO ENTRY\''.format(self.table), (key,)):
            web_link = Web.search_key(key, song, artist)
            self.db.execute('UPDATE {} SET {} = ? WHERE Song = ? AND Artist = ?'.format(self.table, key),
                            (web_link, song, artist))

    def check_data(self, song, artist):
        cursor = self.db.execute('SELECT Song, Artist FROM {}'.format(self.table))
        for row in cursor:
            if song == row['Song'] and artist == row['Artist']:
                return True
        return False
