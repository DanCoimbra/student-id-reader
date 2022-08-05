import requests
from PIL import Image
from flask import Flask, request

app = Flask(__name__)

@app.route('/img', methods=['POST'])
def img():
    client_request  = request.get_json()
    img_token       = client_request['img_token']
    img_url         = f"https://api.telegram.org/file/bot{bot_token}/{img_token}"
    response        = requests.get(img_url)
    img             = Image.open(response.raw)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)