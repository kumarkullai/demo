from flask import Flask

app=Flask(__name__)
@app.route('/')
def kumar():
    return 'welcome'


if __name__=='main':
    app.run()