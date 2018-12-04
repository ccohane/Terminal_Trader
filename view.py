#!/usr/bin/env python3
import os

def login_menu():
    header()
    return input("\nDo you want to [R]egister or [L]ogin? ")

def register():
    header()
    user_name=input("\nEnter a Username: ")
    password= input("\nEnter a Password: ")
    return user_name, password

def header():
    os.system("clear")
    print("Welcome to terminal trader")
    
def admin_menu():
    return input("Do you want to see the top users? [Y]es [N]o")
    
def main_menu():
    header()
    print("\n[D]eposit [B]uy [S]ell [L]ookup [Q]uote [H]oldings [G]et Balance [T]ransaction History [A]Dashboard [E]xit")
    user=input("\nWhat do you want to do: ")
    return user

def error_message():
    return "Error"

def quote_menu():
    header()
    return input("\nEnter Ticker Symbol: ")
    
def lookup_menu():
    header()
    return input("\nEnter Company name: ")

def buy_menu():
    header()
    ticker = input("\nEnter Ticker Symbol: ")
    shares= int(input("\nNumber of shares to buy: "))
    return ticker, shares

def sell_menu():
    header()
    ticker = input("\nEnter Ticker Symbol: ")
    shares= int(input("\nNumber of shares to sell: "))
    return ticker, shares

def deposit_menu():
    header()
    return input("\nEnter amount to transfer into securities account: ")
