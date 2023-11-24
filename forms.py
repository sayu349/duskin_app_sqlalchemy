from wtforms import Form

from wtforms.fields import (
    IntegerField,StringField, PasswordField,
    DateField,SelectField, BooleanField,
    TextAreaField,SubmitField
)
# python3.11以上の場合
from wtforms.fields.html5 import EmailField
#python 3.11未満の場合
#from wtforms.fields import EmailField

from wtforms.validators import (
    DataRequired, Email, EqualTo
)

# 顧客情報入力フォーム
class UserInfoForm(Form):
    # 顧客ID：数値入力
    customer_id = IntegerField("ID")
    # 顧客名：文字列入力
    customer_name = StringField("顧客名")
    # 電話番号：文字列入力
    tel = StringField("電話番号",render_kw={"placeholder":"012-3456-7890"})
    # ボタン
    submit = SubmitField("送信")