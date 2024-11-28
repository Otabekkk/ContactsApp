from flask import render_template, Flask, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'your_postgre'
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


@app.route('/delete/<contact_id>')
def delete_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('index')) 


@app.route('/edit/<int:contact_id>', methods = ['GET', 'POST'])
def edit_contact(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit.html', contact = contact)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug = True)