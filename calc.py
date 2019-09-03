#!/bin/bash/env python
import os
logo='''\033[1;33mChoose operation:
[1] Addition                                                    
[2] Subtraction
[3] Multiplication
[4] Division
'''
def choose():
  try:
  	os.system('clear')
  	print(logo)
  	opt=int(input('\033[1;33mEnter the number of the option: '))
  	if opt==1:
  		add()
  	elif opt==2:
  		sub()
  	elif opt==3:
  		mul()
  	elif opt==4:
  		div()
  	else:
  		print('\033[1;31mWrong input. Try again.')
  		choose()

  except KeyboardInterrupt:
        print('\033[1;33m[*]Exception: KeyboardInterrupt')
        os.system('sleep 0.5s')
        print('\033[1;31m[×]Exiting Program')
        os.system('sleep 1s')
  except ValueError:
        print('\033[1;31mWrong or Empty input. Try again')
        choose()
  except EOFError:
  	print("")
  	print('\033[1;31m[x]Exiting Program..')
  	exit()
  except TabError:
  	choose()
def again():
  try:
  	a=str(input('\033[1;36mDo you want to try again?[y/n]: '))
  	if a=='y':
  		os.system('clear')
  		choose()
  	elif a=='n':
  		exit()
  	else:
  		print('\033[1;33mWrong input')
  		again()
  except KeyboardInterrupt:
  	exit()

def add():
  try:
  	os.system('clear')
  	x=int(input('\033[1;34mEnter the first number: '))
  	y=int(input('\033[1;34mEnter the second number: '))
  	print('\033[1;32mResult: ',x+y)
  	again()
  except KeyboardInterrupt:
  	print('\033[1;33m[*]Exception: KeyboardInterrupt')
  	os.system('sleep 0.5s')
  	print('\033[1;31m[×]Exiting Program')
  	os.system('sleep 1s')
  except ValueError:
  	print('\033[1;31mWrong or Empty input. Try again')
  	add()

def sub():
  try:
        os.system('clear')
        x=int(input('\033[1;34mEnter the first number: '))
        y=int(input('\033[1;34mEnter the second number: '))
        print('\033[1;32mResult: ',x-y)
        again()
  except KeyboardInterrupt:
        print('\033[1;33m[*]Exception: KeyboardInterrupt')
        os.system('sleep 0.5s')
        print('\033[1;31m[×]Exiting Program')
        os.system('sleep 1s')
  except ValueError:
        print('\033[1;31mWrong or Empty input. Try again')
        sub()
  except EOFError:
  	print("")
  	print('\033[1;31m[x]Exiting Program')
  	exit()

def div():
  try:
  	os.system('clear')
  	x=int(input('\033[1;34mEnter the first number: '))
  	y=int(input('\033[1;34mEnter the second number: '))
  	print('\033[1;32mResult: ',x/y)
  	again()
  except KeyboardInterrupt:
        print('\033[1;33m[*]Exception: KeyboardInterrupt')
        os.system('sleep 0.5s')
        print('\033[1;31m[×]Exiting Program')
        os.system('sleep 1s')
  except ValueError:
        print('\033[1;31mWrong or Empty input. Try again')
        div()
  except ZeroDivisionError:
  	print('\033[1;31mOops! You can\'t devide something by Zero')
  	div()
def mul():
  try:
        os.system('clear')
        x=int(input('\033[1;34mEnter the first number: '))
        y=int(input('\033[1;34mEnter the second number: '))
        print('\033[1;32mResult: ',x*y)
        again()
  except KeyboardInterrupt:
        print('\033[1;33m[*]Exception: KeyboardInterrupt')
        os.system('sleep 0.5s')
        print('\033[1;31m[×]Exiting Program')
        os.system('sleep 1s')
  except ValueError:
        print('\033[1;31mWrong or Empty input. Try again')
        mul()

choose()
