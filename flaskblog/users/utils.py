import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path,'static/profile_pics',picture_fn)
    smlimg = Image.open(form_picture)
    smlimg.thumbnail((125,125))
    smlimg.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = User.get_reset_token(user)
    msg = Message("Password Reset Request",
                    sender="noreply.floodwatch@gmail.com",
                    recipients=[user.email])
    msg.body = f'''
To reset your passowrd, visit the link below :

{ url_for('users.reset_token', token=token, _external=True) }

If you did not make this request, then ignore this email.
'''
    mail.send(msg)
