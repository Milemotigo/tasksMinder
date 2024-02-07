
from ..api.app import db

def save(newItem):
    ''' save an item to the database'''
    if newItem is None:
        return 'Item to save not found'
    else:
        try:
            db.session.add(newItem)
            db.session.commit()
            
            return 'Item saved successfully'
        except Exception as e:
            return f'An error occured while saving item: {str(e)}'
