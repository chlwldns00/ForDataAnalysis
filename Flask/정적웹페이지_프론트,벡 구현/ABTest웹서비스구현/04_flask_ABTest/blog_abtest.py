from flask import Flask, jsonify, request, render_template, session, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user, fresh_login_required
from blog_control.user_mgmt import User
from blog_view import blog
import os
from flask_cors import CORS
import datetime


# https 를 쓰지 않을 경우, 보안 이슈로 에러가 남 (다음 설정을 통해 http 에서도 에러가 나지 않도록 함)
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)
app.secret_key = 'dave_server1'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

# User session management setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


@app.before_request
def before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get(
            'HTTP_X_REAL_IP', request.remote_addr)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
