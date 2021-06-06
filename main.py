from website import create_app

app = create_app()

# if statement only runs web server if its from main file
if __name__ ==  '__main__':
    # debug mode is true for now
    app.run(debug=True)