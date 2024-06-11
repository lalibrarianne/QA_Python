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
            check_table = 'SHOW TABLES LIKE "order"'
            cursor.execute(check_table)
            result = cursor.fetchone()
            if result:
               print('Exist')
            else:
               print('not good')
            
            select_query = ''' SELECT *, DATE_FORMAT (creation_date, '%Y') AS   'yer_only' FROM `order` WHERE status_id IN (2, 4) '''
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for i in rows:
                i['creation_date'] = i['yer_only']
                del i['yer_only']
                print(i)

               
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
