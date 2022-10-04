from dotenv import load_dotenv
import os

if os.path.isfile(".env"):
    load_dotenv()
else:
    print("No .env file found, assuming prod deployment with env injection")

from app import make_app

app = make_app()

if __name__ == "__main__":
    app.run(debug=True)
