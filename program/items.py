from sql_connection import get_sql_connection

def get_all_products(connection):

    mycursor = connection.cursor()

    sql = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name " \
        "FROM products inner join uom on products.uom_id=uom.uom_id"

    mycursor.execute(sql)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in mycursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response

def insert_new_product(connection, product):
    mycursor = connection.cursor()

    query = ("INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    mycursor.execute(query, data)
    connection.commit()

    return mycursor.lastrowid

def delete_product(connection, product_id):
    mycursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    mycursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 12))