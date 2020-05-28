from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from portefolio_app import db
from portefolio_app.models import Projects


title = input("title: ")
description = input("description: ")
link = input("link: ")
img = input("img: ")


project = Projects(title = title, description = description, link = link, img = img)

db.session.add(project)
db.session.commit()