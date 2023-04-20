from App.database import db

class UserExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    exercise = db.relationship('Exercise')
    date = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)

    def repr(self):
      return f'<UserExercise {self.id} : {self.name} User {self.user.username}>'


    def get_json(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'user' : self.user.username,
            'date' : self.date,
            'reps' : self.reps,
            'sets' : self.sets,
            'weight' : self.weight
        }
