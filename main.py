import sys
from flask import Flask
import threading

from src.core import main
from src.__init__ import _banner, log, mrh
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def run_flask_app():
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    while True:
        try:
            _banner()
            main()
        except KeyboardInterrupt:
            print()
            log(mrh + f"Successfully logged out of the bot\n")
            sys.exit()

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask_app)
    bot_thread = threading.Thread(target=run_bot)
    
    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()
