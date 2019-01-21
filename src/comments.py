from datetime import datetime
import random
comments = []
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

    def save_comment(**comment):

        comments.append(comment)
    def edit_comment(comment_id):
        response = None
        for comment in comments:
            if comment['comment_id'] == comment_id:
                response = {
                    'id' : comment_id,
                    'message' : "Comment Updated"
                }
            break
        
        if response:
            print(response)
            
        else:
            response = {
                'id' : comment_id,
                'message' : "No comment found"
            }
            print(response)