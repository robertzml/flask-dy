from mysqladapter import MysqlAdapter
from model.person import Person

class PersonRepository:

    # 解析上传数据包，并保存新用户
    def ParseJson(self, js):
        count = len(js)

        mysql = MysqlAdapter()
        mysql.open()

        find_count = 0
        for i in range(count):
            dic = js[i]

            p = Person()
            p.id = dic['uid']
            p.nickname = dic['nickname']
            p.gender = dic['gender']
            p.follower_count = -1
            p.following_count = -1
            p.status = 0

            result = p.check_save(mysql)
            if result == 1:
                find_count += 1

        print('找到%d个新用户' % find_count)

        mysql.close()

