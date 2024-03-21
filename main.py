from flask import Flask

aplikasi = Flask(__name__)

@aplikasi.route('/',methods=['GET'])
def main():
    return "halo"

aplikasi.run(host="0.0.0.0",port=8000)