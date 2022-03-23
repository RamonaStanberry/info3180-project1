from . import db

class Property(db.Model):
    __tablename__= 'property'

    propertyid=db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(255))
    bedrooms = db.Column(db.Numeric(1000,1))
    bathrooms = db.Column(db.Numeric(1000,1))
    location = db.Column(db.String(255))
    price = db.Column(db.Numeric(1000,2))
    description = db.Column(db.String(500))
    type = db.Column(db.String(10))
    photo = db.Column(db.String(500))

    def __init__(self,title,bedrooms,bathrooms,location,price,description,type,photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.description = description
        self.type = type
        self.photo = photo