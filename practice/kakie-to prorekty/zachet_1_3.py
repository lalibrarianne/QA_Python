import pymysql
import pymysql.cursors
from main_config_base import host, user, password, db_name

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

    # Проверка существования таблицы order
    try:
        with connection.cursor() as cursor:
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS `team`(
            id INT AUTO_INCREMENT PRIMARY KEY,
            team_name VARCHAR(255) NOT NULL,
            member_count INT NOT NULL CHECK (member_count <= 10)
            );
            '''
            cursor.execute(create_table_query)
            print('table created')


            #заполняю таблицу
            insert_query = '''
            INSERT INTO `team` (team_name, member_count) VALUES
            ('Brita',8),
            ('Larisa',7),
            ('Kremen',2),
            ('Losos',5),
            ('Jac',9),
            ('Brita',8),
            ('Orbita',8),
            ('Kolissa',4),
            ('Voss',1),
            ('Kloss',5); 
            '''
            cursor.execute(insert_query)
            connection.commit()
            print('data inserted')

            select_query = ''' SELECT * FROM `team` WHERE member_count > 5 '''
            cursor.execute(select_query)
            rows = cursor.fetchall()
            for i in rows:
                print(i)
            
            
    except Exception as e:
        print('An error ')
        print(e)        
           
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)
