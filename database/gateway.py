#%%

import sys
sys.path.append('../')
import util.config as config
import mysql.connector
import json
import numpy as np
import binascii

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


    def wite_binary(self, data, filename, type):
        print("-opening blob")
        if type == 1:
            print("-writing to binary file")
            with open(filename, 'wb') as file:
                file.write(bytearray(data))
        else:
            print("-writing to regular file")
            with open(filename, 'w') as file:
                file.write(data)
        print("-written")
        # with open(filename, mode='rb') as file: # b is important -> binary
        #     content = file.read()
        #     print(content)
        # return content

    def read_binary(self, filename):
        print("-opening binary file")
        with open(filename, 'rb') as file: # b is important -> binary
            print("-reading binary file")
            buffer = file.read()
            print("-read")
            for i in buffer:
                print(i)


    def test_gate(self):
        try:
            self.cur.execute("SELECT * FROM User")
        except:
            return json.dumps([{"message":"database connection failed"}]), 400
        self.db.close()

        return json.dumps([{"message":"database connection success"}]), 200

    def get_input_file(self, upload_id):
        try:
            self.cur.execute(f"SELECT Original_file FROM File WHERE Upload_ID = '{upload_id}'")
            for (upload_id,csv_file,file) in self.cur:
                file_result = file
            # write_to_file(db_file,"data_blob")
            self.db.close()
            return file_result, 200
        except:
            return "Unable to fetch input file."
    
    def get_csv(self, upload_id):
        try:
            self.cur.execute(f"SELECT * FROM File WHERE Upload_ID = '{upload_id}'")
            record = self.cur.fetchall()
            for (up_id,file,csv_file) in record:
                # print(up_id,file,csv_file)
                csv_file = csv_file.decode('utf8')
                # bytes_array = np.frombuffer(csv_file, ndtype='B')
                # print(bytearray())
                # bytes_decoded = str(bytes_array).encode().decode('utf8')
                self.db.close()

            # self.cur.close()
            return csv_file, 200
        except:
            return "get csv failed", 400
    
    def get_files_utf8(self, upload_id):
        try:
            og_file = None
            csv_file = None
            self.cur.execute(f"SELECT * FROM File WHERE Upload_ID = '{upload_id}'")
            record = self.cur.fetchall()
            for (up_id, file_blob, csv_blob) in record:
                # print(file_blob,csv_blob)
                csv_file = csv_blob.decode()
                og_file = file_blob.decode()

                self.db.close()
        except:
            return json.dumps([{"Original_file":og_file, "CSV_file":csv_file}]), 400
        return json.dumps([{"Original_file":og_file, "CSV_file":csv_file}]), 200
        self.close_gate()
    
    def close_gate(self):
        self.db.close()
    

g = gateway()
# g.test_gate()
res, code =  g.get_files_utf8(13)


# print(g.binary_file_to_data("temp_binary_file"))
# with open("temp_binary_file", 'rb') as file: # b is important -> binary
#     print(file.read())
# array.array2string
# for n in res:
#     print(str(n).encode().decode('ASCII'))
# print(res)

# g.test_gate()
# csvreader = csv.reader(response)
# rows = []
# for row in csvreader:
#     rows.append(rows)
# print(rows)


    # def get_file(self, key):
    #     pass
    #     sql_fetch_blob_query = """SELECT * from python_employee where id = %s"""
    #     self.cur.execute(sql_fetch_blob_query, (key))
    #     print("Id = ", row[0], )
    #     file = row[1]
    #     write_file(file, bioData)
    #     readBLOB(1, "D:\Python\Articles\my_SQL\query_output\eric_bioData.txt")

    # def post_file(self, key,bioFile):
    #     pass
    #     sql_insert_blob_query = """ INSERT INTO Files (original_file) VALUES (%s)"""
    #     file = convertToBinaryData(bioFile)
    #     result = self.cur.execute(sql_insert_blob_query,file)
    #     self.db.commit()
        
    # wpost_file("/Users/robg/IdeaProjects/FileAnalyzer/client/reactapp/src/pictures/README.txt")




# %%
