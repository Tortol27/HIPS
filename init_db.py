import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="db_hips",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS sniffers;')
cur.execute('CREATE TABLE sniffer (name varchar (30));')

# Insert data into the table

""" 
cur.execute('INSERT INTO sniffer (name)'
            'VALUES (%s, %s)', ('solarwinds')
            ) """

""" cur.execute('INSERT INTO sniffer (name)'
            'VALUES ((solarwinds),(prtg),(manageengine),(omnipeek),(tcpdump),(windump),(wireshark),(fiddler),(netresec),(capsa),(ethereal))'
            ) """


""" cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            ) """

conn.commit()

cur.close()
conn.close()