import logging
from flask import Flask
from flask_talisman import Talisman # Tambahkan ini
from flask_cors import CORS         # Tambahkan ini

app = Flask(__name__)

# Konfigurasi Security Headers (Exercise 4)
talisman = Talisman(app)

# Konfigurasi CORS (Exercise 7)
CORS(app)

# Sisanya tetap sama (import routes, dll)
from service import routes, models