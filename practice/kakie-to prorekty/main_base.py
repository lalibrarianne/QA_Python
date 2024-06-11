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
            
            create_view_query = '''CREATE VIEW teaice AS
                                SELECT * FROM `good`
                                WHERE name NOT LIKE "%Айс Ти%"'''
            cursor.execute(create_view_query)  
            print('View_ created')

            select_query = """
            SELECT * FROM teaice LIMIT 20;
            """
            cursor.execute(select_query)
            rows = cursor.fetchall()

            insert_into_q = 'UPDATE `good` SET `count` = 123 WHERE `name` LIKE "new_good";'
            cursor.execute(insert_into_q)
            connection.commit()
            print('record update')

            insert_into_q = 'UPDATE `good` SET `price` = 35 WHERE `name` ="new_good";'
            cursor.execute(insert_into_q)
            connection.commit()
            print('record update')


            check_query = 'SELECT * FROM `good` WHERE name = "new_good" AND `count` = 35;'
            cursor.execute(check_query)
            result = cursor.fetchone()
            if result:
               print('good')
            else:
               print('not good')


    
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
