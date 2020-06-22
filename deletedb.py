from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from portefolio_app import db
from portefolio_app.models import Projects

project_list = Projects.query.all()
for i, project in enumerate(project_list):
    print(i, ' : ', project.title)

index = input("Enter the index for the project you want to delete.")
try:
    index = int(index)
except:
    print("Invalid Entry")
    pass

for i, project in enumerate(project_list):
    if i == index:
        project_to_del = Projects.query.filter_by(title=project.title).first()

print("Is this the project you want to delete ? y/n ")
print(project_to_del.title)
confirm = input()
if confirm == "y":
    db.session.delete(project_to_del)
    db.session.commit()
    print(project_to_del.title, " has been deleted")

if confirm == "n":
    print("Nothing has been modified.")

