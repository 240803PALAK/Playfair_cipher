from flask import Flask, render_template, request,jsonify
from encrypt import encryptt
from decrypt import decryptt
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt',methods=['POST','GET'])
def encrypt():
    plaintext = request.json['plaintext']
    key = request.json['key']
    ciphertext,matrix=encryptt(plaintext,key)
    return jsonify({'ciphertext': ciphertext, 'key': key,'matrix':matrix})

@app.route('/decrypt',methods=['POST','GET'])
def decrypt():
    ciphertext = request.json['ciphertext']
    plaintext = request.json['plaintextstore']
    matrix = request.json['matrixstore']
    decryptplain=decryptt(ciphertext,matrix,plaintext)
    return jsonify({'plaintext':decryptplain})
if __name__ == '__main__':
    app.run(debug=True)