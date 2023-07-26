import re

n = int(input('Enter the number of stack elements: '))
stack = []

while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")
    

    choice = int(input("Please enter your Choice: "))
    if choice == 5:
        break

    elif choice == 1:
        if len(stack)>=n:
            print("stack is full",)
        else:    
           insrt = int(input('Enter a value to insert: '))
           stack.append(insrt)

    elif choice == 2:
        if stack:
            del stack[-1]
        else:
            print("Stack is empty. Cannot delete.")

    elif choice == 3:
        search_pattern = input('Enter a pattern to search: ')

        pattern_found = False
        for element in stack:
            
            result = re.search(search_pattern, str(element))
            if result:
                print(f"Pattern found in element: {element}")
                pattern_found = True
        if not pattern_found:
            print("No match found.")

    elif choice == 4:
        print(stack)

    # if len(stack)-1>=n:
       
    #  print("stack is full .")
    #  break



