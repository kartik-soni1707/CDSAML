import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
V=pickle.load(open('enc.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    
    prediction = model.predict(V.transform(request.form.values()))

    if(prediction[0]==1):
        output="spam"
    else:
        output="ham"

    return render_template('index.html', prediction_text='Message is: $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)