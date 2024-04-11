from flask import Flask, jsonify, request, render_template
app = Flask(__name__, static_url_path='/static')
session_count = 0


@app.route('/login')
def login():
    email_address = request.args.get('email_address')
    passwd = request.args.get('passwd')
    print(email_address, passwd)

    if email_address == 'dave@gmail.com' and passwd == '111':

        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)


@app.route('/html_test')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('login_rawtest.html')


def get_blog_page():
    global session_count
    session_count += 1
    if session_count % 2 == 0:
        return 'blog_A.html'
    else:
        return 'blog_B.html'


@app.route('/blog')
def blog_html():
    blog_name = get_blog_page()
    return render_template(blog_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
