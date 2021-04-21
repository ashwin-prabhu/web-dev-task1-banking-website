from flask import Flask, render_template, url_for, request, redirect
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

#db.create_all()

# new = customers(acc_no = "WB0001",cus_name = "Manoah", email_id = "manoah922001@wbbank.com", bal_amount = "10000000")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0002",cus_name = "Keerthivasan", email_id = "kd100100@wbbank.com", bal_amount = "5000")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0003",cus_name = "Aravind", email_id = "aravind@wbbank.com", bal_amount = "4000")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0004",cus_name = "Harshith", email_id = "harshith@wbbank.com", bal_amount = "100")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0005",cus_name = "Prince", email_id = "prince@wbbank.com", bal_amount = "100")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0006",cus_name = "Whiskey", email_id = "whiskey@wbbank.com", bal_amount = "100")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0007",cus_name = "Balaji", email_id = "balaji@wbbank.com", bal_amount = "100")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0008",cus_name = "Power", email_id = "power@wbbank.com", bal_amount = "1000")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0009",cus_name = "Praveen", email_id = "praveen@wbbank.com", bal_amount = "1000")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0010",cus_name = "Jaiprakash", email_id = "jaiprakash@wbbank.com", bal_amount = "3000")
# db.session.add(new)
# db.session.commit()

# new = customers(acc_no = "WB0011",cus_name = "Bharath", email_id = "bharath@wbbank.com", bal_amount = "1000")
# db.session.add(new)
# db.session.commit()

def getdata():
    db_obj = customers.query.all() 
    cus_list = []
    for i in range (len(db_obj)):
        db_str = str(db_obj[i])
        cus_list.append(db_str.split(","))
        cus_list[i][3] = int(cus_list[i][3])
    
    db_obj = transactions.query.all() 
    trans_list = []
    for i in range (len(db_obj)):
        db_str = str(db_obj[i])
        trans_list.append(db_str.split(","))
        trans_list[i][0] = int(trans_list[i][0])
        trans_list[i][3] = int(trans_list[i][3])
    
    return cus_list,trans_list

