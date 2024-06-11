select_query = """
            SELECT *
            FROM tea_without_ice_tea
            LIMIT 20;
            """
            cursor.execute(select_query)
            rows = cursor.fetchall()

            if rows:
                # Вывод выбранных позиций до изменений
                print("Позиции до изменений:")
                for row in rows:
                    print(row)

                # Обновление названий, стоимости и количества
                update_queries = []
                for row in rows:
                    new_name = row['name'] + ' (Updated)'
                    new_price = row['price'] + 10  # Пример изменения стоимости
                    new_quantity = row['quantity'] + 5  # Пример изменения количества
                    update_query = f"""
                    UPDATE good
                    SET name = '{new_name}', price = {new_price}, quantity = {new_quantity}
                    WHERE id = {row['id']};
                    """
                    update_queries.append(update_query)

                # Выполнение обновлений
                for query in update_queries:
                    cursor.execute(query)
                connection.commit()
                print("Обновления выполнены.")

                # Повторная выборка обновленных позиций для отображения
                cursor.execute(select_query)
                updated_rows = cursor.fetchall()

                # Вывод обновленных позиций
                print("Позиции после изменений:")
                for row in updated_rows:
                    print(row)
            else:
                print("Нет позиций, соответствующих условиям.")