from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello_if')
def hello_html():
    value = 27
    return render_template('condition.html', data=value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")