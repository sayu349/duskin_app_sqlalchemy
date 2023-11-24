from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# 顧客情報入力フォームをインポート
from forms import UserInfoForm
# create_duskin_db.py から Customer モデルをインポート
from create_duskin_db import Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duskin.db'
db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def index():
    form = UserInfoForm(request.form)
    # Post
    if request.method == "POST":
        # データ受け取り
        customer_name = form.customer_name.data
        tel = form.tel.data
        # DBにデータ追加
        new_customer = Customer(customer_name=customer_name, phone_number=tel)  # Customer インスタンスの作成
        db.session.add(new_customer)
        db.session.commit()
        return render_template("success.html")
    # Get
    else:
        return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
