from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route('/login')
def login():
    username = request.args.get('user_name') #uri를 플라스크 내에서 넣어주기(실행)
    passwd = request.args.get('pw')
    email = request.args.get('email_address')
    print (username, passwd, email)
    
    if username == 'dave':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login.html') #템플릿 폴더에 있는 html파일을 리턴해주는 역할


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
