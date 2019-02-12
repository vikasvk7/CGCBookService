import sqlite3

db = sqlite3.connect("Books.db")
cursor = db.execute("SELECT * FROM DONATED")
c=0
print("\n")
print("************DONATED BOOKS RECORD***************")
for row in cursor :
    if(c==0):
        print("NAME       ", "PHONE      ", "ROLL_NO    ", "   BOOK_DONATED       ")
        print("--------------------------------------------------")
    print(row[0],"    ",row[1],"   ",row[2],"     ",row[3])
    c+=1

print('\n')
print("************BORROWED BOOKS RECORD***************")
dursor = db.execute("SELECT * FROM BORROWED")
c = 0
for row in dursor :
    if(c==0):
        print("NAME       ", "PHONE        ", "BOOK_BORROWED    ")
        print("------------------------------------------------")
    print(row[0],"  ",row[1],"      ",row[2])
    c+=1

db.commit()
db.close()