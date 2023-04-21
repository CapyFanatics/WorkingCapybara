from App.database import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    exercise_type = db.Column(db.String(120), nullable=False)
    muscle_group = db.Column(db.String(120), nullable=False)
    difficulty = db.Column(db.String(120), nullable=False)



    def repr(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'exercise type' : self.exercise_type,
            'muscle group' : self.muscle_group,
            'Difficulty' :self.difficulty
        }