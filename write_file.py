import sys

class App:
    def __init__ (self, filePath):
        self.filePath = filePath
        self.data = ""
        
    def storeText(self):
        self.data = '''
                                TRY IT YOURSELF
Save each of the following exercises as a separate file, with a name like name. If you get stuck, take a break or see the suggestions in exercises.py.

1. Personal Message: Use a variable to represent a person’s name, and print 
a message to that person. Your message should be simple, such as, “Hello Eric, 
would you like to learn some Python today?”

2. Name Cases: Use a variable to represent a person’s name, and then print 
that person’s name in lowercase, uppercase, and title case.

3. Famous Quote: Find a quote from a famous person you admire. Print the 
quote and the name of its author. Your output should look something like the 
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never 
tried anything new.”

4. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous 
person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

5. Stripping Names: Use a variable to represent a person’s name, and 
include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, '\t' and '\n', at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip().

6. File Extensions: Python has a removesuffix() method that works exactly 
like removeprefix(). Assign the value 'python_notes.txt' to a variable called 
filename. Then use the removesuffix() method to display the filename without 
the file extension, like some file browsers do.
'''
    
    def writeFile(self):
        try:
            file = open(self.filePath, 'w') # Open a file in write mode
            file.write(self.data) # Write data to the file
            file.close() # Close the file when done
            print("File write complete")
            sys.exit(0)
            
        # Catch any exceptions raised
        except FileExistsError as error:
            print(f"File does not exist: {error}")
            sys.exit(1)
        except FileNotFoundError as error:
            print(f"File not found: {error}")
            sys.exit(1)
        

if(__name__ == "__main__"):
    app = App("./Lesson3/Exercises.txt")
    app.storeText()
    app.writeFile()