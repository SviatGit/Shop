def get_uoms(connection):
    mycursor = connection.cursor()
    query = ("SELECT * FROM uom")
    mycursor.execute(query)

    response = []

    for (uom_id, uom_name) in mycursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response

if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_uoms(connection))