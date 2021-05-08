"""
Database version of the GUI Login System [Python3]

This script is the database version of the main script file. Almost every code is the same, but the difference is the storing of the data. The main.py script file stores the user credentials data in the data.json file, whereas this script would make the use of the sqlite3 databases.

Author : Rishav Das
Created on : May 06, 2021

Last modified by : -
Last modified on : -

Authors contributed to this script (Add your name below if you have contributed) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	from sqlite3 import connect
	from tkinter import *
	from tkinter import messagebox as mb
except Exception as e:
	# If there are any errors encountered while importing the modules, then we display the error message on the console screen

	input(f'[ Error : {e} ]\nPress enter key to continue...')
	exit()

# Connecting to the database.db file
# Note : If the file does not exists, then the connection automatically creates a new blank database file
sql = connect('database.db')
cursor = sql.cursor()

# Checking if the users table exists or not
cursor.execute('SELECT count(name) FROM sqlite_master WHERE type="table" AND name="users";')
if cursor.fetchone()[0] == False:
	# If the users table does not exist, then we create it

	cursor.execute('CREATE TABLE users (username VARCHAR(30), password VARCHAR(100));')

def createUser(username, password):
	""" This function creates a new user item using the user provided credentials and then saves the updated data in the data.json file. The function takes in two arguments : username, password. The username and password are the inputs that the user enters on the signup screen input boxes. """

	if (len(username) >= 5) and (len(password) >= 8) and (' ' not in username):
		# If the user entered username and password inputs are valid and then we continue

		# Checking the username and password pre-existence in the data
		cursor.execute(f'SELECT * FROM `users` WHERE `username`="{username}";')
		data = cursor.fetchall()

		if len(data) != 0:
			# If the user entered username already exists for a different user, then we display the error message to the user

			mb.showerror('Username exists', 'Another user with the same username exists. Please choose any other username.')
			return 0
		else:
			# If there are no pre-existing users with the same username, then we continue the process
		
			# Adding the user credentials to the database
			cursor.execute(f'INSERT INTO `users` (`username`, `password`) VALUES ("{username}", "{password}");')

			# Displaying the success message to the user and then switching to the login screen
			mb.showinfo('Sign up success', 'New user has been created using the specified username and password. Go to login page to test it out now.')
			signupWin.destroy()
			main()
			return 1
	else:
		# If the user entered username and password inputs are not valid, then we display the error message back to the user

		mb.showerror('Invalid inputs', 'Please enter proper input for username and password. The username should be atleast 5 characters long as well as it should be a alphanumeric term and should not contain any kind of symbols or special characters. The password should also be either equal or more than 8 characters and the password can include special characters.')
		return 0

def createSignupWin():
	""" This function creates the sign up screen on the main tkinter window of this script. The function takes no argument. """

	# Allowing some variables defined in this function to be globally accessed
	global signupWin

	# Creating a new window for the sign up box + destroying the older one
	win.destroy()
	signupWin = Tk()
	signupWin.title('Sign Up - Login System')
	signupWin.geometry('500x250')
	signupWin.resizable(0, 0)
	signupWin.config(background = 'black')

	# ----
	# Creating the widgets for the sign up window
	# ----
	# Creating the centered heading of the window
	Label(signupWin, text = 'Sign Up', foreground = 'green', background = 'black', font = ('', 20, 'bold', 'italic'),).pack(padx = 10, pady = 10)

	# Defining the username entry part
	frame1 = Frame(signupWin, background = 'black')
	frame1.pack(padx = 5, pady = (10, 5))
	Label(frame1, text = 'Username', foreground = 'green', background = 'black', font = ('', 12, '')).pack(side = LEFT, padx = 5)
	username = StringVar(signupWin)  # Defining a string var for storing the user entered username
	Entry(frame1, textvariable = username, font = ('', 12, '')).pack(side = RIGHT, padx = 5)

	# Defining the password entry part
	frame2 = Frame(signupWin, background = 'black')
	frame2.pack(padx = 5, pady = (5, 10))
	Label(frame2, text = 'Password', foreground = 'green', background = 'black', font = ('', 12, '')).pack(side = LEFT, padx = 5)
	password = StringVar(signupWin)  # Defining a string var for storing the user entered password
	Entry(frame2, textvariable = password, font = ('', 12, ''), show = '*').pack(side = RIGHT, padx = 5)

	# Defining the sign up button
	signupBtn = Button(signupWin, text = 'Sign up', foreground = 'black', background = 'green', activeforeground = 'green', activebackground = 'black', font = ('', 12, ''), relief = GROOVE, command = lambda : createUser(username.get(), password.get()))
	signupBtn.pack(pady = 5, padx = 5)
	# ----

	mainloop()

def authenticate(username, password):
	""" This function authenticates the user on the basis of the credentials provided using the arguments. This function takes two arguments (parameters) : username, password. When the user enters the username and passwords, this function should be called as well as the user entered data should be passed to it. The function can also be added to the onclick event listener of the login button. """

	authentication = 0  # Setting the authentication to false in first
	
	# Reading the data of the data.json file
	cursor.execute(f'SELECT * FROM `users` WHERE `username`="{username}";')
	data = cursor.fetchall()

	# Checking wheter the username exists or not
	if len(data) == 0:
		# If there are no such user on the database with the specified username, then we display the error message to the user

		mb.showerror('Log in failed', f'No such user with username "{username}"')
		return authentication
	else:
		# If there are some data fetched, then we assume that the user exists with the specified username

		data = data[0]
		if data[1] == password:
			# If the passwords are matched, then we display the success message to the user

			authentication = 1
			mb.showinfo('Log in success', f'Welcome {username}, you are logged in successfully!')
			
			# Destructing the main window frames and buttons
			frame1.destroy()
			frame2.destroy()
			loginBtn.destroy()
			signupBtn.destroy()

			# Writting the new label
			Label(win, text = f'Logged in as : {username}', foreground = 'green', background = 'black', font = ('', 12, '')).pack(padx = 5, pady = 5)
			return authentication
		else:
			# If the passwords do not match, then we display failure message to the user

			mb.showerror('Log in failed', f'Incorrect password for the user "{username}"')
			return authentication

def main():
	# DRIVER CODE

	# Allowing some variables defined in this function to be globally accessed
	global win, frame1, frame2, loginBtn, signupBtn

	# Defining the tkinter window
	win = Tk()
	win.title('Log In - Login System')
	win.geometry('500x250')
	win.resizable(0, 0)
	win.config(background = 'black')

	# Displaying the heading
	Label(
		win,
		text = 'GUI Login System',
		foreground = 'green',
		background = 'black',
		font = ('', 20, 'bold', 'italic'),
		).pack(padx = 10, pady = 10)

	# ----
	# Defining the login box
	# ----
	# Defining the username entry part
	frame1 = Frame(win, background = 'black')
	frame1.pack(padx = 5, pady = (10, 5))
	Label(frame1, text = 'Username', foreground = 'green', background = 'black', font = ('', 12, '')).pack(side = LEFT, padx = 5)
	username = StringVar(win)  # Defining a string var for storing the user entered username
	Entry(frame1, textvariable = username, font = ('', 12, '')).pack(side = RIGHT, padx = 5)

	# Defining the password entry part
	frame2 = Frame(win, background = 'black')
	frame2.pack(padx = 5, pady = (5, 10))
	Label(frame2, text = 'Password', foreground = 'green', background = 'black', font = ('', 12, '')).pack(side = LEFT, padx = 5)
	password = StringVar(win)  # Defining a string var for storing the user entered password
	Entry(frame2, textvariable = password, font = ('', 12, ''), show = '*').pack(side = RIGHT, padx = 5)

	# Defining the login button
	loginBtn = Button(win, text = 'Log In', foreground = 'black', background = 'green', activeforeground = 'green', activebackground = 'black', font = ('', 12, ''), relief = GROOVE, command = lambda : authenticate(username.get(), password.get()))
	loginBtn.pack(pady = 5, padx = 5)

	# Defining the signup button for switching to it whenever the user wants to create a new user account
	signupBtn = Button(win, text = 'Sign up', foreground = 'black', background = 'green', activeforeground = 'green', activebackground = 'black', font = ('', 12, ''), relief = GROOVE, command = createSignupWin)
	signupBtn.pack(pady = 5, padx = 5)
	# ----

	mainloop()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors during the process, then we display the error message to the user

		mb.showerror('Error', f'{e}')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user presses CTRL+C key combo, then we exit the script

		exit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error message on the console screen

		input(f'[ Error : {e} ]\nPress enter key to continue...')
		exit()