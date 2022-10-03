from website import create_app                  # importing function from init.py file

app = create_app()                               # calling the function

if __name__ == '__main__':                      #this means it will only run the "app" when called NOT when this main.py file loads.
    app.run(debug=True)                       #this starts our web app, if condition above is met