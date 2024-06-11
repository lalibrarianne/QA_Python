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
            try:
                check  = ''' CREATE VIEW new_users AS SELECT name, email, password, DATE_FORMAT(reg_date, '%Y') AS format_date FROM user WHERE (name LIKE 'A%' OR name LIKE 'А%' OR name LIKE 'B%' OR name LIKE 'Б%') AND YEAR(reg_date) = 2018 '''
                cursor.execute(check)
                
                result1 = cursor.fetchall()
                
                
            except:
                print('not found')
    
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
