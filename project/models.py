from project import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_title = db.Column(db.String, nullable=False)
    item_description = db.Column(db.String, nullable=False)
    item_comment = db.Column(db.String, nullable=True)

    def __init__(self, title, description, comment):
        self.item_title = title
        self.item_description = description
        self.item_comment = comment

    def __repr__(self):
        return '<title {}'.format(self.name)
