# アンケートを取得する Lambda (Python)

前提:ジョークソフトです

入力された名前に対して、集計した結果を返却します

想定しているイメージは、グラフを描画するための画面を用意して、そこからこの Lambda を呼びデータを取得することを目的としています

（※ 誰が投票したかは保持する気はないですし、何回でも投票可能としています）

## 開発環境

* Windows10
* Python3.8
* AWS SAM

環境構築については以下を参照ください

https://qiita.com/morio1101/items/0f98c987332e16b74a58


## 動作確認

### 前提

dynamo DB に `questionnaire` テーブルを作成しておくこと

### ローカル環境で動作確認する方法

```bash
 sam local start-api
```

http://127.0.0.1:3000/viewer?name=test

以下のようなレスポンスが返ってくれば環境が出来ている状態になります
```
{"name": "xxx",...}
```

### AWS 上で確認する方法

S3 のバケットにファイルを配置したりするので IAM に注意してください

```bash
sam build --use-container
sam deploy
```

## 使用方法

### api

* Request
  * GET
* URL
  * /answer
* Query String
  * name
    * ユーザ名（一意）
  * infra_skill
    * インフラスキル
  * pg_skill
    * プログラミングスキル
  * op_skill
    * 運用スキル
  * comm_skill
    * コミュニケーション力
  * strength
    * 体力
  * management
    * マネジメント力
  * kindness
    * やさしさ