import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5tay0ut!'     # cryptographic key used to generate signatures/tokens
                                                                # Flask-WTF uses it to protect web forms against CSRF (Cross-Site Request Forgery)