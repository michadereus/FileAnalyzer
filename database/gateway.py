#%%
import sys
sys.path.append('../')
import util.config as config
import mysql.connector
import json
import numpy as np
import binascii

def write_to_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


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
            self.db.close()
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
            self.db.close()
            return json.dumps([{"Query failed": "database connection failed"}]), 400
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
            self.db.close()
            return json.dumps([{"Query failed": "database connection failed"}]), 400
        self.db.close()
        #TODO: check if a valid user object is returned
        return json.dumps([{"ID": str(myresult[0])}]), 200

        #return json.dumps([{"Permission Denied": "Invalid username or email"}]), 201
    
    def get_users(self):
        # Select * FROM User
        #TODO# test sql below and fill in fucntion
        sql = f"Select * FROM User"
        pass

    def get_user(self, user_id):
        # returns dict of single user 
        #TODO# test sql below and fill in fucntion
        sql = f"Select * FROM User WHERE User_Id = {user_id}"
        pass

    # PUT - UPDATES a user in the database with anew user_id value of <user_id> or a new password value of <passwrod>
    # Only the fields to be modified need be present in the response data.
    def put_user(self, user_id, username=None, password=None):
        # logic to validate input format
        if username:
            # if username is passed, set username in db
            #TODO# sql add update query
            sql = "UPDATE User SET User_Id = '{user_id}' WHERE username = '{username}'"
            self.cur.execute(sql)
            self.db.commit()
            self.db.close()
        else:
            res =  json.dumps([{"message": "new username format is not valid"}]), 400
        if password:
            # if password is passed, set username in db
            #TODO# sql add update query
            sql = "UPDATE User SET User_Id = '{user_id}' WHERE password = '{password}'"
            self.cur.execute(sql)
            self.db.commit()
            self.db.close()
        else:
            res = json.dumps([{"message": "new password format is not valid"}]), 400
        res = json.dumps([{"message": f"updated user: {str(user_id)}"}])
        self.db.close()
        return res, 200
        
    # POST - adds a user user_id to database
    def update_user(self, user_id, username, password):
        pass

    # POST - deleted a user user_id from database
    def delete_user(self, user_id, username, password):
        pass
    
    # GET - returns files from user User_ID
    def get_file(self, upload_id, og_file, csv_file):
        og_file = None
        csv_file = None
        try:
            self.cur.execute(f"SELECT * FROM File WHERE Upload_ID = '{upload_id}'")
            record = self.cur.fetchall()
            for (up_id, file_blob, csv_blob) in record:
                # print(file_blob,csv_blob)
                csv_file = csv_blob.decode()
                og_file = file_blob.decode()
        except:
            self.close_gate()
            return json.dumps([{"message": "failed to get file(s)"}]), 400
        self.close_gate()
        return json.dumps([{"Original_file":og_file, "CSV_file":csv_file}]), 200
        
    # POST - updates Original_file from user User_Id 
    def update_original_file(self, user_id, og_file):
        pass

    # POST - updates csv_file from user User_Id
    def update_csv_file(self, user_id, csv_file):
        pass


    def close_gate(self):
        self.db.close()
    

# g = gateway()
# g.test_gate()



# print("Id = ", row[0], )
# file = row[1]
# write_file(file, bioData)

# get_file(1, "D:\Python\Articles\my_SQL\query_output\eric_photo.png",
#     "D:\Python\Articles\my_SQL\query_output\eric_bioData.txt")

