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

    def add_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercise_id)

        if exercise:
            try:
                user_exercise = UserExercise(self.id, exercise_id, name, reps, sets)
                db.session.add(user_exercise)
                db.session.commit()
                return user_exercise
            except Exception:
                db.session.rollback()
                return None

        return None

    def delete_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercise_id)

        if exercise.user == self:
            db.session.delete(exercise)
            db.session.commit()
            return True
        return None

    def edit_exercise(self, exercise_id, name, reps, sets):
        exercise = Exercise.query.get(exercise_id)

        if exercise.user == self:
            exercise.name = name
            exercise.reps = reps
            exercise.sets = sets

            db.session.add(exercise)
            db.session.commit()
            return True
        return None

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
