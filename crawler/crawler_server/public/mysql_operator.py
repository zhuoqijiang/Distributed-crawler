from center.connect_pool import MysqlConnectPool

class MysqlOperator:
    @staticmethod
    def repace_into(table, message_dict):
        values = "("
        columns = "("
        for key in message_dict:
            values = values + "'" + str(message_dict[key]) + "'" + ","
            columns = columns + key + ","
        columns = columns[0:-1] + ")"
        values = values[0:-1] + ")"
        sql = ("REPLACE INTO %s %s VALUES %s") % (table, columns, values)
        mysql_instance = MysqlConnectPool.get_mysql_instance()
        try:
            mysql_instance.cursor.execute(sql)
            mysql_instance.conn.commit()
        except:
            mysql_instance.conn.rollback()
        MysqlConnectPool.back_mysql_instance(mysql_instance)

