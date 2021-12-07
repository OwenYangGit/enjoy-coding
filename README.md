## 閱讀前參考 pycharm 開發環境設定參考文件
https://drive.google.com/file/d/1897Tho01yrMmdCLIJXYKFWfucsIq3LUD/view?usp=sharing

## 設定 docker-compose 重要參數
- localtunnel 的 --subdomain 參數，可以配置固定的 subdomain url

## docker-compose 的 nginx
因為 localtunnel 設定 proxy 到某個 remote host 之後，若隔一段時間連不到會自動 crash，因此透過一個 proxy 用的 nginx 讓 localtunnel 確保不會斷線，並設定 default.conf proxy 到後端開發環境

## 若套件清單有更新，需要重新 build Dockerfile，舉例來說
```shell
# 先確保無任何專案下的 docker-compose 停止運行
docker-compose down
# 刪除原本的 image，以此專案為例
docker rmi enjoy-coding_python-39:latest
```

## 目前安裝的套件清單
```shell
pip install flask google-cloud-storage google-cloud-firestore line-bot-sdk gunicorn flask_cors
```