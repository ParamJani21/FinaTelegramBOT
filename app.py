from flask import Flask,render_template
from threding import Thread

app=Flask(__name__)

@app.route('/')
def hello-world():
    return 'GreyMatters'
def run():
    app.run(host='0.0.0.0',port=8000)

def keep_alive():
    t =Thread(target=run)
    t.start()
if__name__=="__main__":
    app.run()
