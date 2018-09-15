import pymysql

class Person:
    id = ''
    nickname = ''
    gender = 0
    follower_count = -1
    following_count = -1
    status = 0

    # 插入前检查是否存在, 返回1表示没有此人， 返回2表示存在此人
    def check_save(self, mysql):
        check_sql = "SELECT id FROM person WHERE id = '%s'" % self.id
        count = mysql.count(check_sql)
        if count == 0:
            sql = "INSERT INTO person (id, nickname, gender, follower_count, following_count, status) "\
                  "VALUES('%s', '%s', %d, %d, %d, %d)" % \
                    (self.id, pymysql.escape_string(self.nickname), self.gender, self.follower_count, \
                     self.following_count, self.status)

            mysql.execute(sql)
            return 1
        else:
            return 2