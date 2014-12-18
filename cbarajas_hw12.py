import sqlite3

cur = sqlite3.connect('adventure.db')
cur.execute('CREATE TABLE Room (itemname TEXT, itemcomposition TEXT, itemtype TEXT)')

cur.execute("""INSERT INTO Room 
                    VALUES ('Sword', 'Steel', 'Interactable')""")
cur.execute("""INSERT INTO Room
                    VALUES ('Another Sword', 'Wood', 'Interactable')""")
cur.execute("""UPDATE Room SET itemcomposition = 'Wood'""")
cur.execute("""DELETE FROM Room WHERE itemcomposition = 'Wood';""")
cur.execute("""INSERT INTO Room VALUES ('Sad panda', 'Panda material', 'Interactable')""")
cur.execute("""SELECT itemname FROM Room WHERE itemcomposition = 'Panda Material';""")