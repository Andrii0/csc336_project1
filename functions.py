import csv
import psycopg2

#config for login to psql
config = {
                "user": 'victor',
                "database": 'pipesoftdb'
}

#connect and get cursor
#try:
conn = psycopg2.connect("user='victor' dbname='pipesoftdb' password=''")
#except:
#    print "I am unable to connect to the database"
#try: 
#except:
#    print "I can't drop our test database!"

#function names are self explanatory
#query in each function is a string that will be passed to cursors execute() function
#notice this does not run the query until connections commit() function is called

def drop_table(table):
    cur = conn.cursor()
    query = ("Drop table %s" %(table))
    cur.execute(query)
    print("table %s dropped" %(table))
    cur.close()

def create_game_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE game (
        game_id VARCHAR(8) NOT NULL, 
        title VARCHAR(50) NOT NULL, 
        year INT NOT NULL, 
        developer VARCHAR(50), 
        publisher VARCHAR(50), 
        rating VARCHAR NOT NULL, 
        genre VARCHAR(50), 
        price FLOAT, 
        description VARCHAR(50),			
        PRIMARY KEY (game_id)
        );""")
    try:
        cur.execute(query)
    except: 
        print "didn't execute"
    print("table game created")
    cur.close()

def create_member_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE member (
        member_id VARCHAR(8) NOT NULL,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        balance FLOAT,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        
        PRIMARY KEY (member_id)
        );""")
    cur.execute(query)
    print("table member created")
    cur.close()

def create_shopping_cart_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE shopping_cart (
        member_id VARCHAR(8) NOT NULL,
        num_of_items INT,
        game_id VARCHAR(8) NOT NULL,
        
        PRIMARY KEY (member_id, game_id),
        CONSTRAINT no_member FOREIGN KEY (member_id) REFERENCES member(member_id),
        CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
        );""")
    cur.execute(query)
    print("table shopping_cart created")
    cur.close()

def create_admin_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE admin (
        admin_id VARCHAR(8) NOT NULL,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL,
        rank INT NOT NULL,
        
        PRIMARY KEY (admin_id)
        );""")
    cur.execute(query)
    print("table admin created")
    cur.close()

def create_poster_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE poster (
        game_id VARCHAR(8) NOT NULL,
        link VARCHAR(100) NOT NULL,
        
        PRIMARY KEY(game_id),
        CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
        );""")
    cur.execute(query)
    print("table poster created")
    cur.close()

def create_friends_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE friends (
        member_id VARCHAR(8) NOT NULL,
        friend_id VARCHAR(8) NOT NULL,
        
        PRIMARY KEY (member_id, friend_id),
        CONSTRAINT no_member FOREIGN KEY (member_id) REFERENCES member(member_id),
        CONSTRAINT no_friend FOREIGN KEY (friend_id) REFERENCES member(member_id)
                    );""")
    cur.execute(query)
    print("table friends created")
    cur.close()

def create_reviews_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE reviews (
        game_id VARCHAR(8) NOT NULL,
        member_id VARCHAR(8) NOT NULL,
        score FLOAT,
        feedbck VARCHAR(200) NOT NULL,
        time TIMESTAMP NOT NULL,
        
        PRIMARY KEY (member_id, time),
        CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id),
        CONSTRAINT no_member FOREIGN KEY (member_id) REFERENCES member(member_id)
        );""")
    cur.execute(query)
    print("table reviews created")
    cur.close()

def create_requirements_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE requirements (
        game_id VARCHAR(8) NOT NULL,
        min_cpu VARCHAR(50),
        min_storage VARCHAR(50),
        min_ram VARCHAR(50),
        
        PRIMARY KEY (game_id),
        CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
        );""")
    cur.execute(query)
    print("table requirements created")
    cur.close()

def add_game(game_id,title,year,developer,publisher,rating,genre,price,description):
    cur = conn.cursor()
    query = ("INSERT INTO game (game_id,title,year,developer,publisher,rating,genre,price,description) VALUES ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s')" %(game_id, title, year, developer, publisher, rating, genre, price, description))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_member(id, name, age, balance, password, email):
    cur = conn.cursor()
    query = ("INSERT INTO member (member_id, name, age, balance, password, email) VALUES ('%s','%s','%s','%s','%s','%s')" %(id, name, age, balance, password, email))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_shopping_cart(id, num_of_items, game_ids):
    cur = conn.cursor()
    query = ("INSERT INTO shopping_cart (id, num_of_items, game_ids) VALUES ('%s', '%s', '%s')" %(id, num_of_items, game_ids))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_admin(admin_id, name, email, password, rank):
    cur = conn.cursor()
    query = ("INSERT INTO admin (admin_id, name, email, password, rank) VALUES ('%s', '%s', '%s', '%s', '%s')" %(admin_id, name, email, password, rank))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_poster(game_id, link):
    cur = conn.cursor()
    query = ("INSER INTO posters (game_id, link) VALUES ('%s', '%s')" %(game_id, link))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_friend(id, friend_id):
    cur = conn.cursor()
    query = ("INSERT INTO friends (id, friend_id) VALUES ('%s', '%s')" %(id, friend_id))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_review(game_id, id, score, feedback, datetime):
    cur = conn.cursor()
    query = ("INSERT INTO reviews (game_id, id, score, feedback, date/time)" %(game_id, id, score, feedback, data/time))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_requirements(game_id, min_cpu, min_storage, min_ram):
    cur = conn.cursor()
    query = ("INSERT INTO requirements (game_id, min_cpu, min_storage, min_ram)" %(game_id, min_cpu, min_storage, min_ram))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_player_number(game_id, single, online, local_co_op, online_co_op):
    cur = conn.cursor()
    query = ("INSERT INTO player_number (game_id, single, online, local_co_op, online_co_op)" %(game_id, single, online, local_co_op, online_co_op))
    cur.execute(query)
    conn.commit()
    cur.close()

def fill_games():
    cur = conn.cursor()
    with open('game_data.csv', 'r') as games:
        reader = csv.reader(games)
        next(games)
        for row in reader:
            cur.execute("INSERT INTO game (game_id,title,year,developer,publisher,rating,genre,price,description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    row
                    )
    cur.close()

def fill_members():
    cur = conn.cursor()
    with open('member_data.csv', 'r') as members:
        reader = csv.reader(members)
        next(members)
        for row in reader:
            cur.execute("INSERT INTO member (member_id, name, age, balance, password, email) VALUES (%s, %s, %s, %s, %s, %s)",
            row
            )
    cur.close()

#functions to retrive values from the database
def select_all_from_table(table):
    cur = conn.cursor()
    query = ("""Select * from %s""" %(table))
    cur.execute(query)
    conn.commit()
    #for tuple in cursor:
    #    print(f"{tuple}")
    return cur

def select_from_table(table, attribute, value):
    cur = conn.cursor()
    query = ("Select * from %s where %s='%s'" %(table, attribute, value))
    cur.execute(query)
    conn.commit()
    #for tuple in cur:
    #    print("{tuple}")
    return cur

#create_game_table();
#fill_games();
#select_from_table('game', 'title', 'FIFA');

#create_member_table();
#fill_members();
conn.commit()
