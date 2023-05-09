import xml.etree.ElementTree as ET, sqlite3

create = sqlite3.connect('music_db12.sqlite')
wand = create.cursor()

wand.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
    
CREATE TABLE Artist (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
    
CREATE TABLE Album (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE,
    artist_id    INTEGER
);
    
CREATE TABLE Genre (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE  
);
    
CREATE TABLE Track (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE,
    album_id    INTEGER,
    genre_id     INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


def find( d ,tag_text):
    found = False
    for child in d:
        if found : return child.text
        if child.tag =='key' and child.text == tag_text:
           found = True
    return None


fname = input("Input your itunes data in xml format")
if len(fname) < 1:
    fname = 'Library.xml'
    
all_dicts = ET.parse(fname)
rev_d = all_dicts.findall('dict/dict/dict')
for dict in rev_d:
    if find(dict, 'Track ID')  is None:
        continue
    
    artist = find(dict,'Artist')
    name = find(dict,'Name')
    album = find(dict,'Album')
    len = find(dict,'Total Time')
    rating = find(dict,'Rating')
    count = find(dict,'Play Count')
    genre = find(dict,'Genre')
    
    if name is None or artist is None or album is None or genre is None:
        continue
    
    wand.execute('''
                 INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist, )
        )
    wand.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = wand.fetchone()[0]
    
    wand.execute('''INSERT OR IGNORE INTO Album (artist_id, title) VALUES ( ?, ? )''', (artist_id, album))
    wand.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = wand.fetchone()[0]
    
    wand.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? ) ''', (genre,))
    wand.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = wand.fetchone()[0]
    
    wand.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) 
                 VALUES (? , ? , ? , ? , ? , ? ) ''', (name, album_id,genre_id, len, rating, count)
    )
    
    wand.execute('''
        SELECT Track.title, Artist.name, Album.title, Genre.name 
        FROM Track JOIN Genre JOIN Album JOIN Artist 
        ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
        ORDER BY Artist.name LIMIT 3 ''')
    
    create.commit()