from wtforms import Form

from wtforms.fields import StringField
from wtforms.fields import SubmitField

# 顧客情報入力フォーム
class AddCustomerForm(Form):
    # 顧客名：文字列入力
    customer_name = StringField("顧客名")
    # 電話番号：文字列入力
    phone_number = StringField("電話番号",render_kw={"placeholder":"012-3456-7890"})
    # ボタン
    submit = SubmitField("送信")