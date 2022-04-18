# -*- coding: utf-8 -*-
__author__ = 'zhaohui'

import pymysql
import configparser


class Mysql:
    def __init__(self, db_host, db_port, db_user, db_pass, db_database):
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_database = db_database

    def __get_connect(self):
        if not self.db_database:
            raise (NameError, "no name error")
        self.conn = pymysql.connect(host=self.db_host, port=self.db_port, user=self.db_user,
                                    password=self.db_pass, database=self.db_database)
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "connection error")
        else:
            return cur

    '''
    for (...) {
        data['id'] = row[0]
        data['name'] = row[1]
        values.append(data)
    }
    my.domany(insert_sql, values)
    '''
    def domany(self, sql, values_list):
        cur = self.__get_connect()
        try:
            cur.executemany(sql, values_list)
        except Exception as err:
            self.conn.rollback()
            print(err)
        finally:
            self.conn.commit()
            # self.conn.close() 
    
    def do(self, sql):
        cur = self.__get_connect()
        try:
            result = cur.execute(sql)
        except Exception as err:
            self.conn.rollback()
            print('err', err)
        finally:
            self.conn.commit()
        return result
            # self.conn.close()

    def query(self, sql):
        cur = self.__get_connect()
        cur.execute(sql)
        res_list = cur.fetchall()
        self.conn.close()
        return res_list

    def execut_sql_status(self, sql):
        cur = self.__get_connect()
        res = cur.execute(sql)
        # self.conn.close()
        return res

    def close():
        self.conn.close()

if __name__ == '__main__':
    pass
