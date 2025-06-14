from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = "earthquakes" # custom table name
    
    id = db.Column(db.Integer, primary_key=True)    # primary key column 
    magnitude = db.Column(db.Float)                 # float column    
    location = db.Column(db.String)                 # string column 
    year = db.Column(db.Integer)                    # integer column
    
    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
