from flask import Flask, render_template, request, url_for,jsonify
import joblib
scaler=joblib.load(r"C:\Users\yadav\DataScience\KNN\scaler.lb")
kmeans=joblib.load(r"C:\Users\yadav\DataScience\KNN\crop_reco_kmeans.lb")
df=joblib.load(r"C:\Users\yadav\DataScience\KNN\crop_reco_df.lb")

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])  
def predict():
    if request.method == 'POST':
        n = int(request.form['nitrogen'])   #
        p= int(request.form['phosphorus'])
        k= int(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        userdata = [n,p,k,temperature,humidity,ph,rainfall]
        trans_data=scaler.transform([userdata])
        predict=kmeans.predict(trans_data)[0]
        print(predict)  
        dt=dict(df[df["cluster_8"]==predict]["Crop"].value_counts())   #
        return render_template("index.html",dt=dt)
    
        ls=[]
        for k,v in dt.items():
            if v>=70:
             ls.append(k)
        return jsonify(ls)








if __name__ == '__main__':
    app.run(debug=True)