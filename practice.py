
import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='studen_db',
                                       user='root',
                                       password='Rkpal@123')
        if conn.is_connected():
            print('Connected to MySQL database successfully')
            return conn  # Return the connection object

    except Error as e:
        print(e)

    return None  # Return None if the connection fails


 

def connection_on(conn):
    conn = mysql.connector.connect(host='localhost', database='studen_db', user='root', password='Rkpal@123')
    cursor = conn.cursor()
    return conn, cursor

def connection_close(conn_tuple):
    conn_tuple[1].close()
    conn_tuple[0].close()
    
print("**********************************")
def display_records():
    conn_tuple = connection_on(conn)
    conn_tuple[1].execute("SELECT * FROM Student_TB")
    records = conn_tuple[1].fetchall()
    connection_close(conn_tuple)
    for record in records:
        
        print(record)
        print("****************************************************************")
        print()
    
conn = connect()  # Call the connect() function to establish a connection

if conn is None:
    exit()  # Exit the program if the connection fails
  



# cursor = conn.cursor()


while True:
    print("1. for Insert data in table")
    print("2. for Delete data in data table ")
    print("3. Search user data in table")
    print("4. Display user record from table ")
    print("5. Exit")
    print("6.Update data")

    choice = int(input("Please enter your Choice: "))
    if choice == 5:
        break

    # insert data
    elif choice == 1:
        roll = int(input("Enter a roll number: "))
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        val = (roll, first_name, last_name)

        try:

            conn_tuple = connection_on(conn)
            
            sql="INSERT INTO Student_TB (roll_N, first_name, Last_name) VALUES (%s, %s, %s)"
            
            conn_tuple[1].execute(sql, val)
            conn_tuple[0].commit()
            print("***************************************")
            print("Data inserted successfully!")
            print("**************************************")
        
        except:   
            print("**************************************")
            print("please delete dublicate data")
            print() 
        
            roll_to_delete = int(input("Enter a old roll number to delete: "))
            sql = "DELETE FROM Student_TB WHERE roll_N = %s"
            conn_tuple[1].execute(sql, (roll_to_delete,))
            conn_tuple[0].commit()
            connection_close(conn_tuple)
            print("****************************************")
            print("dublicate data delete successfully")
            print()
        
#delele data in data base
      
    elif choice == 2:
        conn_tuple = connection_on(conn)
        roll_to_delete = int(input("Enter a roll number to delete: "))
        sql = "DELETE FROM Student_TB WHERE roll_N = %s"
        conn_tuple[1].execute(sql, (roll_to_delete,))
        conn_tuple[0].commit()
        print("****************************************************************")
        print("Record deleted successfully!")
        print()
        connection_close(conn_tuple)



    # search_pattern of data in data base 
    elif choice == 3:
            search_pattern = input('Enter a Search record in table : ')
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM Student_TB WHERE first_name LIKE %s OR Last_name LIKE %s",
                    ('%' + search_pattern + '%', '%' + search_pattern + '%')
                )
                records = cursor.fetchall()
                if records:
                    print("Matching records :")
                    for record in records:
                        print(record)
                else:
                    print("**************************************")
                    print("No match found.")
            except Error as e:
                print('Error fetching records:', e)
            finally:
                cursor.close()

    
        

    #display all record
    elif choice == 4:
        print("Displaying all records:")
        display_records()

    elif choice == 6:
     while True:
        new_roll = int(input("Enter the new roll number: "))
        roll_to_update = int(input("Enter old roll number to update: "))
        try:
            cursor = conn.cursor()
            sql = "UPDATE Student_TB SET roll_N = %s WHERE roll_N = %s"
            cursor.execute(sql, (new_roll,roll_to_update))
            conn.commit()
            if cursor.rowcount > 0:
                print("Record updated successfully!")
            else:
                print("No matching record found for updating.")
                break    
            
            # Update first_name and last_name in a similar way.

            first_name_to_update = input("Enter old first_name to update: ")
            new_first_name = input("Enter the new first_name: ")
            sql = "UPDATE Student_TB SET first_name = %s WHERE first_name = %s"
            cursor.execute(sql, (new_first_name, first_name_to_update))
            conn.commit()
            if cursor.rowcount > 0:
                print("Record updated successfully!")
            else:
                print("No matching record found for updating.")
                break

            last_name_to_update = input("Enter old last name to update: ")
            new_last_name = input("Enter the new last name: ")
            sql = "UPDATE Student_TB SET last_name = %s WHERE last_name = %s"
            cursor.execute(sql, (new_last_name, last_name_to_update))
            conn.commit()
            if cursor.rowcount > 0:
                print("Record updated successfully!")
            else:
                print("No matching record found for updating.")
                break
    
            break  # Exit the inner while loop after completing all updates.

        except Error as e:
            print('Error updating data:', e)
        finally:
            cursor.close()

