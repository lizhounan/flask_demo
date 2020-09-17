from website import app
from website.database import db
db.create_all()
app.run(debug=True)

