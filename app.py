from flask import Flask, render_template, request, send_file
import os
from qrcodegen import qrCodeGen

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = False
    if request.method == 'POST':
        url = request.form['url']
        qrCodeGen(url)
        qr_code = True
    return render_template('index.html', qr_code=qr_code)

@app.route('/qrcode.png')
def qrcode_image():
    if os.path.exists('qrcode.png'):
        return send_file('qrcode.png', mimetype='image/png')
    return '', 404

if __name__ == '__main__':
    app.run(debug=True)