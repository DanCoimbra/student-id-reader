import os, dotenv, requests
from PIL import Image
from io import BytesIO
from pyrogram import Client, filters

dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
app = Client('student-id-bot', bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.photo)
async def messages(client, message):
    img_token       = message.photo.file_id
    img_path_URL    = f"https://api.telegram.org/file/bot{BOT_TOKEN}/getFile?file_id={img_token}"
    img_path        = requests.get(img_path_URL, stream=True).json()
    print(img_token, img_path, sep='\n')
    #['result']['file_path']
    #img_URL         = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{img_path}"
    #img_bin         = requests.get(img_URL, stream=True)
    #img = Image.open(BytesIO(response.content))
    #img.show()
    await message.reply('Tnaks')

app.run()