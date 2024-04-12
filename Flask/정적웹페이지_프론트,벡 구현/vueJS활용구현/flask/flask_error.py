from flask import Flask
import requests

app = Flask(__name__)


@app.errorhandler(404)  ## 이 error handler 데코레이터를 추가하면, 설정된 메세지가 에러메세지로 뜬다
def page_not_found(error):
    return "<h1>404 Error</h1>", 404


@app.route("/google") # 다른 웹사이트를 restAPI로 호출할수있다.
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
