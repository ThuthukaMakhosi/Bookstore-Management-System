#A program that can be used by a bookstore clerk

#import sqlite3 database
import sqlite3
db = sqlite3.connect('ebookstore') #ebookstore database
cursor = db.cursor()  # Get a cursor object

#Creating table called books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
''')
db.commit()
cursor = db.cursor()

# Insert book 1
cursor.execute('''INSERT INTO books 
                VALUES (3001, "A Tale of Two Cities", 'Charles Dickens', 30);''')
print('First book inserted')

# Insert book 2
cursor.execute('''INSERT INTO books 
                 VALUES (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40);''')
print('Second book inserted')

# Insert book 3
cursor.execute('''INSERT INTO books 
                  VALUES (3003, "The Lion, the Witch and the Wardrobe", 'C. S. Lewis', 25);''')
print('Third book inserted')

# Insert book 4
cursor.execute('''INSERT INTO books 
                    VALUES (3004, "The Lord of the Rings", 'J.R.R Tolkien', 37);''')
print('Fourth book inserted')

# Insert book 5
cursor.execute('''INSERT INTO books 
                 VALUES (3005, 'Alice in Wonderland', 'Lewis Carroll', 12);''')
print('Fifth book inserted')

#prints out all the books
cursor.execute('''SELECT * FROM books''')
new_table = cursor.fetchall()
for new in new_table:
    print(new)
db.commit()

#while loop to access different menu options
while True:
    menu = '''
Select one of the options below:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
    '''
    print(menu)

    #Prompts user to enter menu option
    option = str(input('Please enter an option(e.g. input 3 to delete book): '))

    #If statement to allow user to enter new book
    if option == '1':

        #while loop to ensure correct value type is entered
        while True:
            try:
                #stores all the book identies in a list 
                cursor.execute('''SELECT id FROM books''')
                id_number = cursor.fetchall()
                identities = []

                #for loop to store  each book identity in the list
                for new in id_number:
                    numbers = str(new).strip('( ,)')
                    identities.append(int(numbers))

                #prompts user  to enter Book id
                id = int(input('Enter book ID: '))

                #while loop to check if book id exits in the database
                while id in identities:
                    print('Book ID already exists')
                    id = int(input('Enter a different book ID: '))
                break
            except ValueError:
                print('Invalid value')
        

        #prompts user to enter Book Title and Author
        Title =input('Enter book TITLE: ')
        Author = input('Enter book AUTHOR: ')
        
        #while loop to ensure correct value type is entered
        while True:
            try:
                Qty = int(input('Enter book QUANTITY: '))
                break
            except ValueError:
                print('Invalid value')

        #Inserts book information in the database
        cursor.execute('''INSERT INTO books
                  VALUES(?,?,?,?)''', (id, Title, Author, Qty))
        
        #outputs updated table
        cursor.execute('''SELECT * FROM books''')
        updated_lib = cursor.fetchall()
        for u in updated_lib:
            print(u)
        print('Book inserted')

        db.commit()

    #statement to allow user to update a book
    elif option == '2':
        #while loop to ensure correct value type is entered
        while True:
            try:
                #stores all the book identies in a list 
                cursor.execute('''SELECT id FROM books''')
                id_number = cursor.fetchall()
                identities = []
                for num in id_number:
                    numbers = str(num).strip('( ,)')
                    identities.append(int(numbers))

                #prompts user  to enter Book id to be updated
                id = int(input('Enter ID of the book you want to update: '))
                while id not in identities:
                    print('Book ID does not exist')
                    id = int(input('Enter a correct book ID: '))
                break
            except ValueError:
                print('Invalid value')

        #prompts user to user new Book Title and Author
        Title =input('Enter new book TITLE: ')
        Author = input('Enter new book AUTHOR: ')
        
        #while loop to ensure correct value type is entered
        while True:
            try:
                Qty = int(input('Enter new book QUANTITY: '))
                break
            except ValueError:
                print('Invalid value')
        
        #statements to update table
        cursor.execute('''UPDATE books SET Title = ? WHERE id = ? ''', (Title, id))
        cursor.execute('''UPDATE books SET Author = ? WHERE id = ? ''', (Author, id))
        cursor.execute('''UPDATE books SET Qty = ? WHERE id = ? ''', (Qty, id))

        #outputs updated table
        cursor.execute('''SELECT * FROM books''')
        added_book = cursor.fetchall()
        for book in added_book:
            print(book)
        print('Book data updated!')
        db.commit()
    
    #statement to allow user to delete books
    elif option == '3':
        #while loop to ensure correct value type is entered
        while True:
            try:
                #stores all the book identies in a list 
                cursor.execute('''SELECT id FROM books''')
                id_number = cursor.fetchall()
                identities = []
                for num in id_number:
                    numbers = str(num).strip('( ,)')
                    identities.append(int(numbers))

                #prompts user  to enter ID for the book they want to delete
                id = int(input('Enter book ID to be deleted: '))
                while id not in identities:
                    print('Book ID does not exist')
                    id = int(input('Enter a correct book ID: '))
                break
            except ValueError:
                print('Invalid value')

        #deletes specified book
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))

        #outputs updated table
        cursor.execute('''SELECT * FROM books''')
        deleted = cursor.fetchall()
        for book in deleted:
            print(book)
        print('Book deleted')
        db.commit()
        
    #Statement to search for book using ID
    elif option == '4':
        #while loop to ensure correct value type is entered
        while True:
            try:
                #stores all the book identies in a list 
                cursor.execute('''SELECT id FROM books''')
                id_number = cursor.fetchall()
                identities = []
                for num in id_number:
                    numbers = str(num).strip('( ,)')
                    identities.append(int(numbers))

                #prompts user  to enter ID for the book they want to search
                id = int(input('Search book (Use ID): '))
                while id not in identities:
                    print('Book ID does not exist')
                    id = int(input('Search book: '))
                break
            except ValueError:
                print('Invalid value')
        
        #outputs information about search book
        cursor.execute('''SELECT id, Title, Author, Qty FROM books WHERE id=?''', (id,))
        search = cursor.fetchone()
        print(search)

        db.commit()

    #exits the program
    elif option == '0': 
        db.commit()
        db.close()
        exit()
  
    else:
        print('Invalid input. Try again!')   



    


