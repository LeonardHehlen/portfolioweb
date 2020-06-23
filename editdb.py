from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from portefolio_app import db
from portefolio_app.models import Projects

project_list = Projects.query.all()
for i, project in enumerate(project_list):
    print(i, ' : ', project.description)

index = input("Enter the index for the project you want to edit.")
try:
    index = int(index)
except:
    print("Invalid Entry")
    pass

for i, project in enumerate(project_list):
    if i == index:
        project_to_edit = Projects.query.filter_by(title=project.title).first()

project_to_edit.description = "Permet de lire le serial et de récupérer le signal des potentiomètre afin d'envoyer un message midi correspondant."

db.session.add(project_to_edit)
db.session.commit()