@app.route('/test')
def test():

POST_USERNAME = "python"
POST_PASSWORD = "python"

Session = sessionmaker(bind=engine)
s = Session()
query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
result = query.first()
if result:
return "Object found"
else:
return "Object not found " + POST_USERNAME + " " + POST_PASSWORD