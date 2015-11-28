import sqlite3


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)')

def enter_date():
    c.execute('INSERT INTO example VALUES("Python", 2.7, "Beginner")')
    c.execute('INSERT INTO example VALUES("Python", 3.3, "Intermediate")')
    c.execute('INSERT INTO example VALUES("Python", 3.4, "Expert")')
    conn.commit()

def enter_dynamic_date():
    lang = raw_input("What language? >   ")
    version = float(raw_input("What version? >  "))
    skill = raw_input("What skill level? >  ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)"), (lang, version, skill)

    conn.commit()

# create_table()

# enter_date()

# enter_dynamic_date()

def read_from_db():
    sql = "SELECT * From example WHERE Skill == 'Intermediate' "

    for row in c.execute(sql):
        print(row)
        # print(row[0])

read_from_db()

conn.close()