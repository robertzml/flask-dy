import pymysql


class MysqlAdapter:

    def open(self):
        self._db = pymysql.connect("localhost", "zml", "123456", "dy")


    def close(self):
        self._db.close()

    # 执行插入语句
    def execute(self, sql):
        cur = self._db.cursor()
        try:
            cur.execute(sql)
            self._db.commit()
        except Exception as err:
            self._db.rollback()
            print(sql)
            print(err)
        finally:
            cur.close()

    def query(self, sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def query_one(self, sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()

        return data

    # 获取查询结果数量
    def count(self, sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        count = cursor.rowcount
        cursor.close()

        return count


    def insert_person(self, uid, nickname, gender):
        cur = self._db.cursor()

        try:
            sql = "INSERT INTO person (uid, nickname, gender) VALUES('%s', '%s', %d)" % (uid, nickname, gender)

            cur.execute(sql)
            self._db.commit()
        except Exception as err:
            self._db.rollback()
            print(err)
        finally:
            cur.close()