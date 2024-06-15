from flask import Flask, render_template, request # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle 
with open (r"C:\Users\LOHITH KUMAR\Downloads\Liver-patient-analysis-using-machine-learning-main (1)\liver patient\project\flask\liver_analysis.pkl",'rb+') as file:
        model = pickle.load(file)
        
app=Flask(__name__) # our flask app

@app.route('/') 
def home():
    return render_template('home.html')
@app.route('/predict', methods=['POST',"GET"] ) 
def index() :
    return render_template("index.html")

@app.route('/data_predict', methods=['POST','GET']) 
def predict():
    age = request.form['age'] 
    gender = request.form['gender'] 
    tb = request.form['tb'] 
    db = request.form['db'] 
    ap = request.form['ap'] 
    aa1 = request.form['aa1'] 
    aa2 = request.form['aa2'] 
    tp = request.form['tp']
    a = request.form['a'] 
    agr = request.form['agr']
    
    # coverting data into float format
    data = [[float(age), float(gender), float(tb), float(db), float(ap),float(aa1),float(aa2),float(tp),float(a),float(agr)]] 
    with open (r"C:\Users\LOHITH KUMAR\Downloads\Liver-patient-analysis-using-machine-learning-main (1)\liver patient\project\flask\liver_analysis.pkl",'rb+') as file:
        model = pickle.load(file)
    prediction= model.predict(data)[0]
    if (prediction == 1):
        return render_template('chance.html', prediction='You have a liver desease problem, You must and should consult a doctor. Take care')
    else:
        return render_template('noChance.html', prediction='You dont have a liver desease problem')

if __name__ == '__main__':
    app.run()