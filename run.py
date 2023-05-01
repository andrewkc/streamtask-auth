from app import create_app, db

app = create_app()

if __name__ == "__main__":
    # host and port of MV Development1 
    # app.run(host="34.225.222.153", port=8080)
    app.run(host = "0.0.0.0", port = 7001)

