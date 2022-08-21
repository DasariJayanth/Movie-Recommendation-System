from mov_eng import db
from mov_eng import bcrypt
from mov_eng import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(),nullable=False,unique=True)
    email_address = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)

    def __repr__(self):
        return f'{self.id},{self.username},{self.email_address},{self.password_hash}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)