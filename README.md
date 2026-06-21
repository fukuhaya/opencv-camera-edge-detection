\# OpenCV Camera Edge Detection



PCカメラを使ってリアルタイム映像を取得し、OpenCVでCannyエッジ検出を行うデモです。



\## 目的



SLAMや画像処理の基礎として、カメラ入力、グレースケール変換、エッジ検出、リアルタイム表示の流れを理解することを目的としています。

\##Environment
OS	Windows
CPU	Intel Core i5
Memory	8GB RAM

\## 使用技術



\- Python

\- OpenCV

\- Web Camera



\## 実行方法



```bash

pip install -r requirements.txt

python src/main.py



\## 操作方法

q キーで終了

\##学んだこと

OpenCVでカメラ映像を取得する方法

グレースケール変換の方法

Cannyエッジ検出の使い方

リアルタイム画像処理の基本構造

\##今後の改善

特徴点検出を追加する

オプティカルフローを実装する

カメラキャリブレーションに発展させる

簡易SLAMにつなげる

