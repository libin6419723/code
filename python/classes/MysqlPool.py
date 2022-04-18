# -*- coding: utf-8 -*-
__author__ = 'zhaohui'

import pymysql
from DBUtils.PooledDB import PooledDB


class MysqlPool:
    def __init__(self, db_host, db_port, db_user, db_pass, db_database):
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db = db_database
        self._conn = self.__create_pool()
        self._cursor = self._conn.cursor()

    def __create_pool(self):
        if not self.db:
            raise (NameError, "connection error")
        else:
            self.pool = PooledDB(creator=pymysql, mincached=5, maxcached=10, maxshared=8, maxconnections=12,
                                 host=self.db_host, port=self.db_port, user=self.db_user, password=self.db_pass,
                                 db=self.db)
            return self.pool.connection()

    def executemany_sql(self, sql, values_list):
        try:
            self._cursor.executemany(sql, values_list)
        except Exception as err:
            print(err)
        finally:
            self._conn.commit()

    def execut_sql(self, sql):
        self._cursor.execute(sql)
        res_list = self._cursor.fetchall()
        return res_list

    def execut_sql_status(self, sql):
        res = self._cursor.execute(sql)
        return res

    def execut_end(self):
        self._cursor.close()
        self._conn.close()


if __name__ == '__main__':
    pass