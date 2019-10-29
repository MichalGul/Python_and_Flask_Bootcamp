from basic import db, Puppy

#Creates all the tables --> transfom model class into DB Table
db.create_all()

sam = Puppy("Sammy", 3)
frank = Puppy("Frankie", 4)

# Powinny byc nony
print(sam.id)
print(frank.id)

#Dodanie obiektow do bazy
db.session.add_all([sam, frank])
# #2 metoda
# db.session.add(sam)
# db.session.add(frank)

#Zapisz zmiany do bazy danych
db.session.commit()

print(sam.id)
print(frank.id)
