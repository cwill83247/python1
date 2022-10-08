from website import create_app                  # std importing function from init.py file

app = create_app()                               # std calling the function

if __name__ == '__main__':                      # std this means it will only run the "app" when called NOT when this main.py file loads.
    app.run(debug=True)                       # std this starts our web app, if condition above is met