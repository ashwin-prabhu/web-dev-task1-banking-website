from flask import Flask, render_template, url_for, request, redirect
import datetime
app = Flask(__name__)

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banking.db'
db = SQLAlchemy(app)

class customers(db.Model):
    acc_no = db.Column(db.String(6), primary_key = True)
    cus_name = db.Column(db.String(30))
    email_id = db.Column(db.String(40))
    bal_amount = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.acc_no},{self.cus_name},{self.email_id},{self.bal_amount}"

class transactions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fr_acc = db.Column(db.String(6))
    to_acc = db.Column(db.String(6))
    amt = db.Column(db.Integer)
    time = db.Column(db.String(18))

    def __repr__(self):
        return f"{self.id},{self.fr_acc},{self.to_acc},{self.amt},{self.time}"


def getdata_cust():
    db_obj = customers.query.all() 
    cus_list = []
    for i in range (len(db_obj)):
        db_str = str(db_obj[i])
        cus_list.append(db_str.split(","))
        cus_list[i][3] = int(cus_list[i][3])
    return cus_list

def getdata_trans():    
    db_obj = transactions.query.all() 
    trans_list = []
    for i in range (len(db_obj)):
        db_str = str(db_obj[i])
        trans_list.append(db_str.split(","))
        trans_list[i][0] = int(trans_list[i][0])
        trans_list[i][3] = int(trans_list[i][3])
    return trans_list



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/customers",methods = ['POST','GET'])
def customer():
    data = getdata_cust()
    data1 = getdata_trans()
    if request.method == 'POST':
        print("Hi!")
        id = len(data1)+1
        fr_acc = "WB0001"
        name = request.form["name"]
        for i in data:
            if(name == i[1]):
                to_acc = i[0]
        amt = request.form["amt"]
        
        time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p %Z")
        new = transactions(id=id,fr_acc=fr_acc,to_acc=to_acc,amt=amt,time=time)
        db.session.add(new)
        db.session.commit()
        db.session.query(customers).filter(customers.acc_no == fr_acc).update({customers.bal_amount:customers.bal_amount - amt})
        db.session.commit()
        db.session.query(customers).filter(customers.acc_no == to_acc).update({customers.bal_amount:customers.bal_amount + amt})
        db.session.commit()
        return redirect("/customers")
    return render_template("allcustomers.html", data = data)

@app.route("/transactions")
def transaction():
    data = getdata_trans()
    return render_template("alltransactions.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)