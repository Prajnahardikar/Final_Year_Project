from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request
import io
import csv
import pandas as pd
from numpy import array
from tensorflow.keras import models
app = Flask(__name__, template_folder='/content/drive/My Drive/FYP')
run_with_ngrok(app)   #starts ngrok when the app is run
@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/test", methods = ['POST', 'GET'])
def test():
  if request.method == 'POST':
    f = request.files['file']
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    df = pd.DataFrame(data=csv_input,index=None, columns=None)
    df = df.iloc[:,:56]
    df = df.transpose()
    df = array(df)
    df = df.astype(float)
    df = df.reshape(1,df.shape[0],251)
    probs = mdel.predict(df)
    probs = (probs>0.50)
    result = probs[0][0]
    return render_template('test.html', output = result)
  else:
    return render_template('test.html', output = None)
mdel = models.load_model('/content/drive/My Drive/FYP/TrainedModel')
app.run()