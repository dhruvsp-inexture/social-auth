from app import db


class User(db.Model):
    """model for storing user information and user id"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(120), nullable=False)
    platform = db.Column(db.String)

    def save_to_db(self) -> "User":
        db.session.add(self)
        db.session.commit()
        return self
