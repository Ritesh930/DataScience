from flask import Flask,render_template,request,url_for
app=Flask(__name__)

@app.route('/')  #route to the home page file

def home():  #hamesha file k naam se function banega
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__=='__main__':
    app.run(debug=True)