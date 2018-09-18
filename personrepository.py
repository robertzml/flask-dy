from mysqladapter import MysqlAdapter
from model.person import Person
import time

class PersonRepository:

    def parse_json(self, js):
        """
        解析上传数据包，并保存新用户
        截取倒数20个
        :param js: JSON数据包
        :return:
        """
        upload_count = len(js)

        slice = js[-20:]
        count = len(slice)

        mysql = MysqlAdapter()
        mysql.open()

        find_count = 0
        for i in range(count):
            dic = slice[i]

            p = Person()
            p.uid = dic['uid']
            p.nickname = dic['nickname']
            p.gender = dic['gender']
            p.follower_count = -1
            p.following_count = -1
            p.used = 0

            result = p.check_save(mysql)
            if result == 1:
                find_count += 1

        print('分析%d个用户，找到%d个新用户，上传%d个用户' % (count, find_count, upload_count))

        mysql.close()

