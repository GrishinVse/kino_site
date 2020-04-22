<<<<<<< HEAD
from app import app

if __name__ == '__main__':
    app.run(debug=True)

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
=======
from app import app

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 85d6b8ea0501ed3d4ece54d28aa109f945ee3ccb
