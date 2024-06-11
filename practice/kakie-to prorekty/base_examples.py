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
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            #создал таблицу
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS `students`(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age INT NOT NULL
            );
            '''
            cursor.execute(create_table_query)
            print('table students created')


            #заполняю таблицу
            insert_query = '''
            INSERT INTO `students` (name,email,age) VALUES
            ('Inna Varlamova', 'inna@example.com', 20),
            ('Genry Smith', 'gensm@example.com', 21),
            ('Rita Vasilina', 'riva@example.com', 22),
            ('Ivan Petrov', 'ivape@example.com', 23),
            ('Teodor Rusvelt', 'teor@example.com', 24),
            ('Olga Nolina', 'onabina@example.com', 25),
            ('Ulya Horina', 'uhori@example.com', 21),
            ('Konstantin Netil', 'konet@example.com', 22),
            ('Ivan James', 'ian@example.com', 23),
            ('Sveta Lesina', 'svels@example.com', 24);
            '''
            cursor.execute(insert_query)
            connection.commit()
            print('data inserted')
        
        
            selectq = 'SELECT * FROM students ORDER BY id LIMIT 5'
            cursor.execute(selectq)
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








