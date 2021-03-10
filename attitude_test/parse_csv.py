import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('attitude_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS deployments')
conn.execute('DROP TABLE IF EXISTS ID')
conn.execute('DROP TABLE IF EXISTS gender')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE ID (ID TEXT, Time TEXT, language TEXT, Country TEXT, choice TEXT, threat TEXT)')
conn.execute('CREATE TABLE gender (ID TEXT, Country TEXT, education_level_reduced TEXT, age_group TEXT, IIC TEXT, long_term_priority TEXT)')
conn.execute('CREATE TABLE deployments (ID TEXT, Time TEXT, language TEXT, Country TEXT, gender TEXT, education_level_reduced TEXT, age_group TEXT, IIC TEXT, choice TEXT, long_term_priority TEXT, threat TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('United Republic of Tanzania.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:

        ID = row[0]
        Time = row[1]
        language = row[2]
        Country = row[4]
        gender = row[6]
        education_level_reduced = row[7]
        age_group = row[10]
        IIC = row[12]
        choice = row[14]
        long_term_priority = row[15]
        threat = row[16]

        cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?,?,?,?,?,?,?)', (ID, Time, language, Country, gender, education_level_reduced, age_group, IIC, choice, long_term_priority, threat))
        conn.commit()
print("deployment data parsed successfully");



# open the file to read it into the database
with open('United Republic of Tanzania.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        
        ID = row[0]
        Time = row[1]
        language = row[2]
        Country = row[4]
        choice = row[14]
        threat = row[16]


        cur.execute('INSERT INTO ID VALUES (?,?,?,?,?,?)', (ID, Time, language, Country, choice, threat))
        conn.commit()
print("ID data parsed successfully");



# open the file to read it into the database
with open('United Republic of Tanzania.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        
        ID = row[0]
        Country = row[4]
        education_level_reduced = row[7]
        age_group = row[10]
        IIC = row[12]
        long_term_priority = row[15]
       

        cur.execute('INSERT INTO gender VALUES (?,?,?,?,?,?)', (ID, Country, education_level_reduced, age_group, IIC, long_term_priority))
        conn.commit()
print("gender data parsed successfully");



