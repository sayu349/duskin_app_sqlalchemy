from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# 顧客情報入力フォームをインポート
from forms import AddCustomerForm
# db_info.py から Customer モデルをインポート
from db_info import db
from db_info import Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duskin.db'
db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/customer")
def customer():
    # DB接続
    with app.app_context():
        # DBから必要な情報を取得
        customer_list = Customer.query.all()
    # データ出力
    return render_template("customer.html", customer_list=customer_list)

@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    form = AddCustomerForm(request.form)
    # Post
    if request.method == "POST":
        # データ受け取り
        customer_name = form.customer_name.data
        phone_number = form.phone_number.data
        # DBにデータ追加
        new_customer = Customer(customer_name=customer_name, phone_number=phone_number)  # Customer インスタンスの作成
        db.session.add(new_customer)
        db.session.commit()
        db.session.close()
        # データ出力
        return render_template("success.html", customer_name=customer_name,phone_number=phone_number)
    # Get
    else:
        return render_template("add_customer.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
