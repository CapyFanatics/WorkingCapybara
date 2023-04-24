from App.database import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    uuid = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(200))



    def repr(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'uuid' : self.uuid,
            'image' : self.image
        }