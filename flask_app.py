from flask import Flask,render_template,request
import csv



app_cs=Flask(__name__)
@app_cs.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app_cs.route('/data',methods=['GET','POST'])    
def data():
    if request.method=='POST':
        f=request.form['csvfile']
        data_app=[]
        with open('jobs.csv') as f:
            csvfile=csv.reader(f)
            for row in csvfile:
                data_app.append(row)
        print(data_app)        
    return render_template('data.html',data=data_app)

    
        





if __name__=='__main__':
    app_cs.run(debug=True)
