import os
os.system("apt install python3-morfeusz2")

from app import app

if __name__ == "__main__":
    app.run()