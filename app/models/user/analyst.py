from app.models.user import User

class Analyst(User):
    def __init__(self, id, name, email, category_id, ranking="D"):
        super().__init__(id, name, email)
        self.category_id = category_id
        self.ranking = ranking
