# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .Exercise import Exercise_views
from .UserExercise import userexercise_views


views = [user_views, index_views, auth_views, Exercise_views, userexercise_views] 
# blueprints must be added to this list