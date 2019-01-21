comments = []

def edit_comment(comment_id, message):
    response = None
    for comment in comments:
        if comment['comment_id'] == comment_id:
            comment['message'] == message
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