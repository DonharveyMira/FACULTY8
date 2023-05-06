#patient database
import sqlite3

class Patient_Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS patient(
            id Integer Primary Key,
            name text,
            address text,
            birthday text,
            age text,
            contact text,
            martial text,
            height text, 
            weight text,
            pulse text,
            bodytemp text,
            reciding text,
            working text,
            rdb1 boolean,
            rdb2 boolean,
            rdb3 boolean,
            rdb4 boolean,
            rdb5 boolean,
            rdb6 boolean,
            rdb7 boolean
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, address, birthday, age, contact, martial, height, weight, pulse, bodytemp):
        self.cur.execute("INSERT into patient values (NULL,?,?,?,?,?,?,?,?,?,?)",
                         (name, address , birthday , age, contact, martial, height, weight, pulse, bodytemp))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from patient")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from patient where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, address , birthday , age, contact, martial, height, weight, pulse, bodytemp):
        self.cur.execute(
            "update patient set name=?, address=?, birthday=?, age=?, contact=?, martial=?, heigth=?, weight=?, pulse=?, bodytemp=? where id=?",
            (name,address, birthday, age, contact, martial, height, weight, pulse, bodytemp, id))
        self.con.commit()


    def updateMeds(self, bpm, bodytemp, home, work, rdb1, rdb2, rdb3, rdb4, rdb5, rdb6, rdb7 ):
        self.cur.execute( 
            "update patient set bpm=?, bodytemp=?, home=?, work=?, rdb1=?, rdb2=?, rdb3=?, rdb4=?, rdb5=?, rdb6=?, rdb7=? where id=?",
            (bpm, bodytemp, home, work, rdb1, rdb2, rdb3, rdb4, rdb5, rdb6, rdb7, id))
        self.con.commit()
