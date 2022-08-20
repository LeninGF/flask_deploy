from flask import render_template, request, redirect
from flask_app.models.emailcls import Email
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add-email', methods=['POST'])
def add_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    data = {"email": request.form["email"]}
    Email.save_email(data)
    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.get_all()
    return render_template("success.html", emails = emails)

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id":id
    }
    Email.destroy(data)
    return redirect('/success')