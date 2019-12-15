pythonファイルはメモ帳等で開いてください！

まずは credential.py に認証情報を記載してください。
```python
YAMATO_ID = 'your_yamato_id'
YAMATO_PW = 'your_yamato_password'
```
こんな風になればOK


まずは必要なパッケージをダウンロードします。コマンドプロンプトを開いてください。（windows の検索画面で「cmd」と検索すればでてくるかと、、）
```bash
cd %homepath%\Downloads\get_daily_record_20191204\get_daily_record_20191204
# ダウンロードしたディレクトリに移動します！

# windowsなら
dir
# macなら
ls
# としたときにおおよそ以下のようになっていればディレクトリは大丈夫です。
/*
2019/12/07  07:30               101 credential.py
2019/12/07  00:17               309 driver.py
2019/12/07  07:24                 0 error.log
2019/12/05  22:47             1,059 functions.py
2019/12/07  06:59               589 logger.py
2019/12/07  07:21                67 main.py
2019/12/07  07:35               326 README.md
2019/12/07  07:35                29 requirements.txt
2019/12/07  07:26    <DIR>          result
2019/12/07  07:20    <DIR>          yamato
2019/12/07  07:26             4,274 yamato.py
*/

# 必要なパッケージのダウンロード
pip install -r requirements.txt

# このときpipというコマンドは見つかりませんと出た場合はpathが通っていないので通してください。
# 連絡ください！

# pythonのバージョンの確認
python -V
> python 3.6.9
# などであればOK
# python 3.6, 3.7, 3.8ならOKです！

# 動作の実行
# 作成されるファイルはresultディレクトリ内の日付の場所に格納されます。
python main.py
# ↑を打ち込めば始まるかと思います！

```