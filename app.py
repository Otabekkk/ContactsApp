from flask import render_template, Flask, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ztw02@localhost:5432/contacts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy()
db.init_app(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    phone = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False)


@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts = contacts)



@app.route('/add', methods = ['GET', 'POST'])
def add_contact():
    if request.method  == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')

        new_contact = Contact(name = name, phone = phone, email = email)
        db.session.add(new_contact)
        db.session.commit()

        return redirect('/')
    
    return render_template('add.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug = True)