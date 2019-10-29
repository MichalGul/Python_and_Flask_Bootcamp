# BASIC.py
# CREATE ENTRIES INTO THE TABLES
from models import db, Puppy, Owner, Toy

#Creating 2 PUPPIES
rufus = Puppy("Rufus")
fido = Puppy("Fido")

#ADD PUPPIES TO DB

db.session.add_all([rufus, fido])
db.session.commit()

# CHECK!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# CREATE OWNER OBJECT
jose = Owner('Jose', rufus.id)

# GIVE RUFUS some toys
toy_1 = Toy("Bone", rufus.id)
toy_2 = Toy("Chew Toy", rufus.id)

# Add created objects to database
db.session.add_all([jose, toy_1, toy_2])
db.session.commit()

# GRAB RUFUS AFTER THOSE ADDITIONS
rufus = Puppy.query.filter_by(name="Rufus").first()
print(rufus)

rufus.report_toys()

#delete rufus
second_pup = Puppy.query.filter_by(name="Rufus").first()
db.session.delete(second_pup)
db.session.commit()
