from datetime import datetime
import random

class Comment():

    def __init__(self, author_id, message, reply_to=None):
        self.comment_id = random.randint(10, 100)
        self.author_id = author_id
        self.message = message
        self.created_at = datetime.now()
        self.reply_to = reply_to


    def to_dict(self):
        comment_dict = {
            'comment_id': self.comment_id,
            'author_id': self.author_id,
            'message': self.message,
            'created_at': self.created_at,
            'reply_to': self.reply_to
        }

