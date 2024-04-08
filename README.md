# 概要
株式会社CARTA HOLDINGSのサポーターズ主催の2020年ウインターハッカソンvol5のチーム初めてのgithub専用レポジトリ

# サービスのこと
### サービス名
媚みくじ

### アプリ概要
ゲーム内でお金を稼ぎ、稼いだお金でおみくじをするゲーム。おみくじに課金するほど良い結果がでるサービス。

### アプリ概要
コロナ禍のお正月でも楽しめるサービスのお題の元、おみくじをゲーム化+お笑い要素を取り込んだものを作ろうということがきっかけ。

### 使用フレームワーク
- Flask

### 使い方
1. venvをactivateする。
2. requirements.txt内をインストールする。
```
pip install -r requirements.txt
```
3. Djangoモデルの変更を検出し、それをマイグレーションファイルとして出力する。
```
python3 manage.py makemigrations
```
4. マイグレーションファイルをデータベースに適用して、データベースを最新の状態に更新
```
python3 manage.py migrate
```
5. サーバを起動する。
```
python3 manage.py runserver
```
## デモ
https://github.com/cmb-sy/Omikuji/assets/63276819/9082f426-3d5e-42f5-abf5-201895362a36
