# suskin_app_sqlalchemy

## What is this？？
flask-sqlalchemyを使って、dbを構築・操作します。
db作成からデータ入力までのサンプルコードとして使えます。

## 概要
- db_info.pyに全てのdbの構成情報を書き記しています
- create_duskin_db.pyで、dbを作成
- forms.pyにて、入力フォームフォーマットを作成
- main.pyにて、データの受け渡し、dbへデータ入力・出力をします

## 使い方
- dbを作成（再作成）する場合
    - create_duskin_db.pyを実行する
- dbにデータを入力してみたい場合
    - main.pyを実行して、動きを確認してください

## 捕捉
- create_duskin_db.pyは、dbを削除したときにだけ使います
    - 削除したdbの再作成には、create_duskin_db.pyを使うということ
- dbは、"instance/duskin.db"にあります
    - db内を覗きたい場合には、VSCodeの拡張機能である"SQLite Viewer"などを活用してください