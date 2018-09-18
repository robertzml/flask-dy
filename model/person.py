import pymysql

class Person:
    uid = ''
    nickname = ''
    gender = 0
    follower_count = -1
    following_count = -1
    used = 0

    # 插入前检查是否存在, 返回1表示没有此人， 返回2表示存在此人
    def check_save(self, mysql):
        check_sql = "SELECT uid FROM person WHERE uid = '%s'" % self.uid
        count = mysql.count(check_sql)
        if count == 0:
            sql = "INSERT INTO person (uid, nickname, gender, follower_count, following_count, used) "\
                  "VALUES('%s', '%s', %d, %d, %d, %d)" % \
                    (self.uid, pymysql.escape_string(self.nickname), self.gender, self.follower_count, \
                     self.following_count, self.used)

            mysql.execute(sql)
            return 1
        else:
            return 2