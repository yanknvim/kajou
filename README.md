<h1 align="center">kajou</h1>
<h2 align="center">Minimal and Enough m3u playlist manager FOR ME</h2>

# 概要
　kajou(箇条)は、python製のミニマルなm3uプレイリストのマネージャーです。ほぼほぼ自分のために作りました。

# インストール
```
$ python3 setup.py install
```

# 使い方
```
kajou add [path] [playlist]
# パスで指定された楽曲ファイルをプレイリストの末尾に追加

kajou insert [path] [index] [playlist]
# プレイリストのindexで指定された場所にパスで指定された楽曲ファイルを追加

kajou list [playlist]
# 指定されたプレイリストにはいっている楽曲をリストアップ

kajou remove [index] [playlist]
# 指定されたトラックをプレイリストから削除

kajou sort [playlist]
# プレイリストをソート

kajou shuffle [playlist]
# プレイリストをシャッフル
```
なお、この中に出てくる`[index]`はすべて1スタートです。

# 依存関係
- fire
- mutagen

