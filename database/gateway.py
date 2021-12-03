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
            return json.dumps([{"message":"database connection failed"}]), 400
        # table = [{"aasdasd":"asdas"}]
        # for (user_id) in self.cur:
        #     table.append({111:user_id})
        # out = self.cur.fetchone()
        self.db.close()
        return json.dumps([{"message":"database connection success"}]), 200

    def get_file(self, key):

        pass

    def post_file(self, key):
        pass

    def close_gate(self):
        self.db.close()