# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 17:51:17 2016

@author: Yuxuan
"""

#Testing
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

statement= '''Select Track.title, Artist.name, Album.title, Genre.name
    FROM Track Join Genre Join Album Join Artist
    On Track.genre_id = Genre.id and Track.album_id = Album.id
        And Album.artist_id = Artist.id
    Order By Artist.name LIMIT 3'''
    
statement2 = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''
            
for row in cur.execute(statement2):
    print(row[0], row[1], row[2], row[3])
