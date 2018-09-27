from project import db
from project.models import Item


# create the database and the database table
db.create_all()

# insert item data
item1 = Item('Slow-Cooker Tacos', 'Delicious ground beef that has been simmering in taco seasoning and sauce.  Perfect with hard-shelled tortillas!', 'alskdalksjd')
item2 = Item('Hamburgers', 'Classic dish elivated with pretzel buns.', 'alskdalksjd')
item3 = Item('Mediterranean Chicken', 'Grilled chicken served with pitas, hummus, and sauted vegetables.', 'alskdalksjd')
db.session.add(item1)
db.session.add(item2)
db.session.add(item3)

# commit the changes
db.session.commit()
