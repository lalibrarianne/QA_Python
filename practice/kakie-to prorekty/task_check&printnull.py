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
            check_table = 'SHOW TABLES LIKE "good_category"'
            cursor.execute(check_table)
            result = cursor.fetchone()
            if result:
               print('good')
            else:
               print('not good')
            nullcheck  = 'CREATE VIEW total_null AS SELECT (SELECT COUNT(*) FROM good_category WHERE id IS NULL) + (SELECT COUNT(*) FROM good_category WHERE parent_id IS NULL) +(SELECT COUNT(*) FROM good_category WHERE name IS NULL) AS total_null'
            cursor.execute(nullcheck)
            result1 = cursor.fetchall()
            select_query = 'SELECT * FROM `total_null`'
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
