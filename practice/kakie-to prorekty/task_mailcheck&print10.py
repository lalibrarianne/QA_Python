import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name


try:
    connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('success')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            check_table = 'SHOW TABLES LIKE "user"'
            cursor.execute(check_table)
            result = cursor.fetchone()
            if result:
               print('good')
            else:
               print('not good')
            mailcheck  = ''' CREATE VIEW 2017_users AS SELECT name, email, password, DATE_FORMAT(reg_date, '%d-%m-%Y') AS format_date FROM user WHERE email LIKE ('%gmail%') AND reg_date BETWEEN '2017-01-02' AND '2017-09-01' '''
            cursor.execute(mailcheck)
            result1 = cursor.fetchall()
            select_query = 'SELECT * FROM `2017_users`LIMIT 10'
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for i in rows:
                print(i)

            
            for i in result1:
                print(i)

    
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
