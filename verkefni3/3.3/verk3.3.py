from app import app
from app import db
from app.models import User, Post
User()
Post()

u = User(username='john', email='john@example.com')
db.session.add(u)
db.session.commit()

u = User.query.get(1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

 # get all posts written by a user
u = User.query.get(1)
posts = u.posts.all()
posts()

# print post author and body for all posts
posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)

# get all users in reverse alphabetical order
User.query.order_by(User.username.desc()).all()

app.run()