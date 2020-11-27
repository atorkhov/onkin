from flask import Flask
from flask_file_upload import FileUpload
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '7104ba209f0cf2e63b28982f7b8782e8'
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://admin:12345@localhost/TestFileStream?driver=SQL Server?Trusted_Connection=yes"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

# Environment variables
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
UPLOAD_FOLDER = "C:/Documents"
ALLOWED_EXTENSIONS = ["jpg", "png", "mov", "mp4", "mpg"]
MAX_CONTENT_LENGTH = 1000 * 1024 * 1024  # 1000mb
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://admin:12345@localhost/TestFileStream?driver=SQL Server?Trusted_Connection=yes"

file_upload = FileUpload(
    app,
    db,
    upload_folder=UPLOAD_FOLDER,
    allowed_extensions=ALLOWED_EXTENSIONS,
    max_content_length=MAX_CONTENT_LENGTH,
    sqlalchemy_database_uri=SQLALCHEMY_DATABASE_URI,
)

# An example using the Flask factory pattern
def create_app():
    # Dynamically set config variables:
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

    file_upload.init_app(app, db)


from film_aggregator import routes  # , import_imdb_dataset
# import_imdb_dataset.run_db_imports()
