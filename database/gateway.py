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
            self.cur.execute("SELECT * FROM test")
        except:
            return json.dumps([{"message":"not found"}]), 400
        table = []
        for (test1) in self.cur:
            table.append({"test_var":test1})
        self.db.close()
        return json.dumps(table), 200

    def close_gate(self):
        self.db.close()

    def get_file(self, key):
        pass

    def post_file(self, key):
        pass