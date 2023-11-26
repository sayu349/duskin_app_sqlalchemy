from flask import Flask
from db_info import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///duskin.db'
db.init_app(app)

"""
▼▼▼--------------------以下DB作成--------------------▼▼▼
"""

# DB立ち上げ
with app.app_context():
    # db_info.pyにある、各Class情報に従ってDB作成
    db.create_all()

"""
▲▲▲--------------------以上DB作成--------------------▲▲▲
"""