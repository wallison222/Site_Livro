from app import create_app

app = create_app()  # Certifique-se de que esta linha está correta

if __name__ == "__main__":
    app.run(debug=True)
