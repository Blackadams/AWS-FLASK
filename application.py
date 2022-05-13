from flaskblog import create_app,db

application = create_app()

with application.app_context():
    db.create_all()

if __name__ == '__main__':
    application.run(host="0.0.0.0", debug=True)
    # app.run(debug=True)
