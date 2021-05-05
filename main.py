"""
GUI Login using tkinter [Python3]

This script is a simple implementation of login system type thing using python with a touch of graphics using tkinter framework.

Author : Lucky Verma (https://github.com/luckyverma-sudo)
Created on : May 4, 2021

Last modified by : Rishav Das (https://github.com/luckyverma-sudo)
Last modified on : May 5, 2021

Changes made in last modification :
1. Changed the entire structure of the project, removed files, replaced the main script with the main.py file.
2. Created main.py file + added the complete set of error free code into it.
3. Added proper data storing and fetching functionality to the script. Changed the old ways of data storing as it was full of errors and mistakes, new way of the data storing is using JSON files. We will store the user credentials in the data.json file, and for each login verification we will check for the existing (already stored) user credentials in that file. Added the function 'authenticate(username, password)'' which is automatically called with passing correct arguments, when the user presses the login button on tkinter window of this tool. Also the function then checks wheter the user entered credentials are correct or not with the existing user credentials in the data.json file. If the user enters a correct username and password, then we continue to welcome the newly logged in user, else if the user enters wrong username and password combination, then we raise an error message back to the user. The error messages as well as the other info messages are also created using the messagebox class of the tkinter module. The script currently uses two modules : tkinter and json. Tkinter module is used for creating the graphical objects and the entire GUI window, and on the other hand we use the json module to work with the json data in our application. The sign up feature will be added soon.

Authors contributed to this script (Add your name below if you have contributed) :
1. Lucky Verma (github:https://github.com/luckyverma-sudo/, email:@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	from tkinter import *
	from tkinter import messagebox as mb
	from json import loads, dumps
except Exception as e:
	# If there are any errors encountered during the importing of the modules, then we display the error on the console screen

	input(f'\n[ Error : {e} ]\nPress enter key to continue...')

def authenticate(username, password):
	""" This function authenticates the user on the basis of the credentials provided using the arguments. This function takes two arguments (parameters) : username, password. When the user enters the username and passwords, this function should be called as well as the user entered data should be passed to it. The function can also be added to the onclick event listener of the login button. """

	# Reading the data of the data.json file
	data = loads(open('data.json', 'r').read())

	# Checking wheter the user entered username does exist or not
	authentication = 0  # Setting the authentication to false in first
	for item in data:
		if username == item["username"]:
			# If the user exist on the data files, then we continue to check passwords

			if password == item["password"]:
				# If the passwords are matched, then we display the success message to the user

				authentication = 1
				mb.showinfo('Log in success', f'Welcome {username}, you are logged in successfully!')

				# Destructing the main window frames and buttons
				frame1.destroy()
				frame2.destroy()
				loginBtn.destroy()

				# Writting the new label
				Label(win, text = f'Logged in as : {username}', foreground = 'green', background = 'black', font = ('', 12, '')).pack(padx = 5, pady = 5)
				return authentication
			else:
				# If the passwords do not match, then we display failure message to the user

				mb.showerror('Log in failed', f'Incorrect password for the user "{username}"')
				return authentication

	# Checking the authentication if we are out of the loop
	if authentication == False:
		# If the user is still not authenticated, that means the username entered does not exists

		mb.showerror('Log in failed', f'No such user with username "{username}"')
		return authentication

def main():
	# DRIVER CODE

	# Making some variables declared in this function global
	global win, frame1, frame2, loginBtn

	# Defining the tkinter window
	win = Tk()
	win.title('Login box')
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