
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


 

# def connection_on():
#     conn.cursor()

# def connection_close():
#     conn.close()    




print("****************************************************************")
def display_records(cursor):
    # connection_on()
    cursor.execute("SELECT * FROM Student_TB")
    records = cursor.fetchall()

    for record in records:
        
        print(record)
        print("****************************************************************")
        print()
    
conn = connect()  # Call the connect() function to establish a connection

if conn is None:
    exit()  # Exit the program if the connection fails



cursor = conn.cursor()









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

    # inset data
    elif choice == 1:
        roll = int(input("Enter a roll number: "))
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        val = (roll, first_name, last_name)

        try:
            
            sql="INSERT INTO Student_TB (roll_N, first_name, Last_name) VALUES (%s, %s, %s)"
            
            cursor.execute(sql, val)
            conn.commit()
            print("***************************************")
            print("Data inserted successfully!")
            print("**************************************")
            
        except:   
            print("**************************************")
            print("please delete dublicate data")
            print() 

            roll_to_delete = int(input("Enter a old roll number to delete: "))
            sql = "DELETE FROM Student_TB WHERE roll_N = %s"
            cursor.execute(sql, (roll_to_delete,))
            conn.commit()
            print("dublicate data delete successfully")
            
        


        
#delele data in data base
       
    elif choice == 2:
        roll_to_delete = int(input("Enter a roll number to delete: "))
        sql = "DELETE FROM Student_TB WHERE roll_N = %s"
        cursor.execute(sql, (roll_to_delete,))
        conn.commit()
        print("****************************************************************")
        print("Record deleted successfully!")
        print()
        cursor.close()



    # search_pattern of data in data base 
    elif choice == 3:
        search_pattern = input('Enter a Search record in table : ')

        cursor.execute("SELECT * FROM Student_TB WHERE first_name LIKE %s OR Last_name LIKE %s",
                       ('%' + search_pattern + '%', '%' + search_pattern + '%'))

        records = cursor.fetchall()
        if records:
            print("Matching records :")
            for record in records:
                print(record)
        else:
            print("**************************************")
            print("No match found.")

        

    #display all record
    elif choice == 4:
        print("Displaying all records:")
        display_records(cursor)


# update record in table
    elif choice == 6:
        while True:
                # roll 
                roll_to_update = int(input("Enter old roll number to update: "))
                new_roll = int(input("Enter the new roll number: "))
                sql = "UPDATE Student_TB SET roll_N = %s WHERE roll_N = %s"
                cursor.execute(sql, (new_roll, roll_to_update))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Record updated successfully!")
                else:
                    print("No matching record found for updating.")

            #  first _name
                first_name=input("enter old  firsst name=",)
                new_first_name=input("enter new first name=",)

                sql = "UPDATE Student_TB SET first_name = %s WHERE first_name = %s"
                cursor.execute(sql, (new_first_name, first_name))
                conn.commit()
                if cursor.rowcount > 0:
                    print("Record updated successfully!")
                else:
                    print("No matching record found for updating.")
                 

            #update last name
                old_last_name=input("Enter a last old name=",)
                new_last_name=input("Enter a last new last name=",)  
                sql="update Student_TB set last_name=%s where last_name=%s"
                cursor.execute(sql,(new_last_name,old_last_name)) 
                conn.commit()
                if cursor.rowcount>0:
                    print('Record update successfully')
                else:
                    print("No Maching record founding=",)     
                    print("**************************************************************")    

                
            
                break

conn.close()  # Close the database connection after the loop
