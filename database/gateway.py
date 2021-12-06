#%%
import sys

sys.path.append('../')
import util.config as config
import mysql.connector
import json


class gateway():

    def __init__(self):
        self.db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            passwd=config.DB_PASS,
            database=config.DB,
            port=config.DB_PORT
        )
        self.cur = self.db.cursor()

    def test_gate(self):
        try:
            self.cur.execute("SELECT * FROM User")
        except:
            return json.dumps([{"message": "database connection failed"}]), 400
        # table = [{"aasdasd":"asdas"}]
        # for (user_id) in self.cur:
        #     table.append({111:user_id})
        # out = self.cur.fetchone()
        self.db.close()
        return json.dumps([{"message": "database connection success"}]), 200

    # Upload a new user to DB
    def register(self, username, password):
        try:
            sql = "INSERT INTO User (Username,Password) VALUES(%s,%s)"
            val = (username, password)
            self.cur.execute(sql, val)
            self.db.commit()
        except:
            return json.dumps([{"User not created": "database connection failed"}]), 400
        self.db.close()
        return json.dumps([{"Created Id should go here": "database connection success"}]), 200

    def login(self,username,password):
        try:
            sql = "Select * FROM User WHERE Username = %s AND Password = %s"
            val = (username, password)
            self.cur.execute(sql, val)
            myresult = self.cur.fetchone();
            myresult = self.cur.fetchone();
        except:
            return json.dumps([{"Query failed": "database connection failed"}]), 400
        self.db.close()
        #TODO: check if a valid user object is returned
        return json.dumps([{"ID": str(myresult[0])}]), 200

        #return json.dumps([{"Permission Denied": "Invalid username or email"}]), 201

    def get_file(self, key):

        pass

    def post_file(self, key):
        pass

    def close_gate(self):
        self.db.close()

    def write_file(data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)

    def get_file(self, key):
        pass
        sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""
        self.cur.execute(sql_fetch_blob_query, (key))

    # print("Id = ", row[0], )
    # file = row[1]
    # write_file(file, bioData)

    # get_file(1, "D:\Python\Articles\my_SQL\query_output\eric_photo.png",
    #     "D:\Python\Articles\my_SQL\query_output\eric_bioData.txt")

    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def post_file(self, key, bioFile):
        pass
        sql_insert_blob_query = """ INSERT INTO Files (original_file) VALUES (%s)"""
        # file = convertToBinaryData(bioFile)
        # result = self.cur.execute(sql_insert_blob_query,file)
        self.db.commit()

    # post_file("/Users/robg/IdeaProjects/FileAnalyzer/client/reactapp/src/pictures/README.txt")

    def close_gate(self):
        self.db.close()
