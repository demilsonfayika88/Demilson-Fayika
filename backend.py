import sqlite3

def connect():
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS skutable (id INTEGER PRIMARY KEY, title CHAR (255), quantity  INT,price DOUBLE)")
    conn.commit()
    conn.close()

def insert(title,quantity,price):
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO skutable VALUES (NULL,?,?,?)",(title,quantity,price))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM skutable")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(id="",title="",quantity="",price=""):
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM skutable WHERE id=? OR title=? OR quantity=? OR price=?", (id,title,quantity,price))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM skutable WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,quantity,price):
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute("UPDATE skutable SET title=?, quantity=?, price=? WHERE id=?",(title,quantity,price,id))
    conn.commit()
    conn.close()

def laapsearch(quantity="",):
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM skutable WHERE quantity > 0")
    rows=cur.fetchall()
    conn.close()
    return rows

def lasopsearch(quantity="",):
    conn=sqlite3.connect("sku.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM skutable WHERE quantity=0")
    rows=cur.fetchall()
    conn.close()
    return rows


connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
