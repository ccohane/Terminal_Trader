#!/usr/bin/env python3

import model
import view
import time
import sys

def login():
    user_input=view.login_menu()
    if user_input.lower() == "r":
        user_name, password = view.register()
        loging_in=model.create_user(user_name,password)

        if loging_in== False:
            print("\nUsername is already taken")
            time.sleep(3)
            login()

    elif user_input.lower()== "l":
        user_name, password = view.register()
        loging_in=model.check_user(user_name, password)

        if loging_in== False:
            print("\nUsername or password is incorrect")
            time.sleep(3)
            login()

    if loging_in:
        game_loop(user_name)

def game_loop(user_name):
    while True:

        admin=model.get_status(user_name)
        if(admin==1):
            option=view.admin_menu()
            if option.lower() == "y":
                model.get_leaderboards()


        deposit_inputs=["d","deposit"]
        get_balance_inputs=["g"]
        buy_inputs=["b","buy"]
        sell_inputs=["s","sell"]
        lookup_inputs=["l","lookup"]
        quote_inputs=["q","quote"]
        holdings_inputs=["h","holdings"]
        transactions=["t"]
        dashboard=["a"]
        exit_inputs=["e","exit"]
        acceptable_inputs= buy_inputs \
                           + deposit_inputs \
                           + transactions \
                           + dashboard \
                           + get_balance_inputs \
                           + sell_inputs \
                           + lookup_inputs \
                           + quote_inputs \
                           + holdings_inputs \
                           + exit_inputs

        user_inputs=view.main_menu()

        if user_inputs.lower() in acceptable_inputs:
            user_inputs=user_inputs.lower()

            if user_inputs in buy_inputs:
                ticker,shares = view.buy_menu()
                model.buy(ticker.upper(),shares,user_name)
                time.sleep(5)

            elif user_inputs in sell_inputs:
                ticker,shares = view.sell_menu()
                model.sell(ticker.upper(),shares,user_name)
                time.sleep(5)

            elif user_inputs in lookup_inputs:
                print(model.lookup(view.lookup_menu()))
                time.sleep(5)

            elif user_inputs in quote_inputs:
                print(model.quote(view.quote_menu()))
                time.sleep(5)

            elif user_inputs in holdings_inputs:
                model.print_holdings(user_name)
                time.sleep(5)

            elif user_inputs in deposit_inputs:
                model.deposit(user_name, view.deposit_menu())
                time.sleep(5)

            elif user_inputs in get_balance_inputs:
                print(model.get_balance(user_name))
                time.sleep(5)

            elif user_inputs in transactions:
                model.print_transactions(user_name)
                time.sleep(5)

            elif user_inputs in dashboard:
                model.dashboard(user_name)
                time.sleep(15)

            elif user_inputs in exit_inputs:
                print("\nThank You For Using Terminal Trader!")
                time.sleep(3)
                sys.exit()

        else:
            view.error_message()
            time.sleep(3)
            game_loop(user_name)

        game_loop(user_name)

if __name__=="__main__":
    login()
#    game_loop("ccohane")

