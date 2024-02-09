from ..utils.save import save
from .models import Note
from flask import Blueprint, render_template, json
from ..auth_app.models import User
from flask import redirect, url_for, flash
from .forms import NoteForm

from flask_login import (
        login_required,
        current_user
        )

note = Blueprint('note', __name__)

@note.route('/addNote', methods=['POST'])
def add_note():
    '''render a note template'''
    form = NoteForm()
    return render_template('notes/add-note.html', user=current_user, form=form)

@note.route('/add-notes', methods=['POST', 'GET'])
def addNotes():
    '''Notes implimentation'''

    form = NoteForm()
    title = form.title.data
    content = form.content.data

    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    if form.validate_on_submit():
        try:
            newNote = Note(
            user_id = current_user.id,
            title = title,
            content = content,
            )
            save(newNote)
            #return redirect(url_for('note.list_notes'))
            flash(f'Note added successfull', 'success')
        except Exception as e:
            return f'An error occured while adding now note: {str(e)}'
    return json.dumps({
        'status': 'ok',
        'title': title,
        'content': content,
        })

@note.route('/notes', methods=['GET'])
def list_notes():
    '''query for all notes'''
    notes = Note.query.all()
    return render_template('notes/notes.html', notes=notes)


def delNotes():
    ''' delete a note '''

