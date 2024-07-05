import psycopg2

# Connect to the database

db_config = {

    "dbname": "tls_employee",
    "user": "postgres",
    "password": "pass123",
    "host": "localhost",
    "port": "5432"
}

try:
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("select * from tls_employee.public.persons p")
    cursor.execute("Insert into tls_employee.public.persons (personid, lastname, firstname, city, address) values (3, 'Papas', 'Maria', 'Kamara', 'Patra')")
    # Fetch all the records
    records = cursor.fetchall()
    print(records)
    connection.commit()
    for record in records:
        # print(f'''{record}
        # ''')

        # for field in record:
        #     print(field, end=" ")
        print(f'''ID: {record[0]}, First Name: {record[1]}, Last Name: {record[2]}, Address: {record[3]}
        ''')

    connection.close()
except psycopg2.Error as e:
    print("Error while connecting to PostgreSQL", e)