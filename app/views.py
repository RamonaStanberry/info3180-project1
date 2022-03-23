"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from crypt import methods
from app import app,db
from flask import render_template, request, redirect, url_for, flash,session, send_from_directory
from werkzeug.utils import secure_filename
from app.property import propertyForm
from app.models import Property
###
# Routing for your application.
###

@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']),filename)

@app.route('/')
def home():
    
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create',methods=['GET', 'POST'])
def create():
    thisForm=propertyForm()
    if request.method=='POST':
        if thisForm.validate_on_submit():
            title = thisForm.title.data
            bedrooms= thisForm.bedrooms.data
            bathrooms= thisForm.bathrooms.data
            location= thisForm.location.data
            price= thisForm.price.data
            type= thisForm.type.data
            description= thisForm.description.data
            photo= thisForm.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            db.session.add(Property(title,bedrooms,bathrooms,location,price,description,type,filename))
            db.session.commit()
            flash('Property Added Successfully!', 'success')
            return redirect(url_for('properties'))
        else:
            flash_errors(thisForm)
    return render_template("create.html",form=thisForm)


@app.route('/properties')
def properties():
    property = Property.query.all()
    return render_template('properties.html',property=property)


@app.route('/properties/<propertyid>')
def showProperty(propertyid):
    propid = Property.query.filter_by(propertyid=propertyid).first()
    return render_template('indivual_property.html', propid=propid)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
