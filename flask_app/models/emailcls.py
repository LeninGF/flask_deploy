from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email():
    db = 'emails_schema'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save_email(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * from emails;"
        results = connectToMySQL(cls.db).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s"
        results = connectToMySQL(Email.db).query_db(query, email) # esta parte no me queda claro porque no paso email.id
        print(results)
        if len(results) >= 1:
            flash("Email ya disponible en la lista")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Dirección de Email inválida")
            is_valid = False
        return is_valid