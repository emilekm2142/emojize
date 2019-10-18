import os
os.system("easy_install morfeusz2-0.4.0-py3.6-win-amd64.egg")

from app import app

if __name__ == "__main__":
    app.run()