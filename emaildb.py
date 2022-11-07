import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mboxshort.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    prieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = 7 ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (7, 1)''', (email,))
    else: 
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = 7',
                     (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER by count DESC LIMIT 10'

for rom in cur.execute(sqlstr)