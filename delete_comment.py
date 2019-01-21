comments = []

def delete_comment(comment_id):
    deleted = False
    for comment in comments:
        if comment['comment_id'] == comment_id:
            comments.remove(comment)
            deleted = True
        break
    
    if deleted:
        print(f"Comment with ID:{comment_id} deleted.")
        
    else:
        print(print(f"Comment with ID:{comment_id} not found."))