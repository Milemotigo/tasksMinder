from ..api.app import db
from .models import Note
from flask import Blueprint, render_template

note = Blueprint('note', __name__)

@note.route('/notes')
def addNotes():
    '''Notes inplimentation'''
    newNote = Note(
            user_id = 1,
            title = 'First note',
            content = 'First note for taskminder'
            )
    db.session.add(newNote)
    db.session.commit()
    return render_template('notes/note.html', newNote=newNote)

def delNotes():
    ''' delete a note '''
