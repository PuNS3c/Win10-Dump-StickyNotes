### Read StickyNotes on windows 10 Build 18363
### @PuNS3c
### .......

import sqlite3
import os

db = os.getenv('localappdata') + r"\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite"
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT * FROM Note")
rows = cur.fetchall()
for row in rows:
        print(row[0])
        input('\n\nPress any key to display next note...\n\n')
        
input('Press any key to exit...')
