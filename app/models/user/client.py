from app.models.user import User

class Client(User):
    def __init__(self, id, name, email, category_id):
        super().__init__(id, name, email)
        self.category_id = category_id
