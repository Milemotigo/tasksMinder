from ..utils.save import save
from .models import Note
from flask import Blueprint, render_template
from ..auth_app.models import User
from flask import redirect, url_for, flash
from .forms import NoteForm

from flask_login import (
        login_required,
        current_user
        )

note = Blueprint('note', __name__)

@note.route('/add-notes', methods=['POST', 'GET'])
def addNotes():
    '''Notes inplimentation'''

    form = NoteForm()
    title = form.title.data
    content = form.content.data

    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if form.validate_on_submit():
        try:
            newNote = Note(
            user_id = current_user.id,
            title = title,
            content = content,
            )
        except Exception as e:
            return f'An error occured while adding now note: {str(e)}'
        save(newNote)
        return redirect(url_for('note.list_notes'))
    flash(f'Note added successfull', 'success')
    return render_template('notes/add-note.html', form=form, user=current_user)

@note.route('/notes', methods=['GET'])
def list_notes():
    '''query for all notes'''
    notes = Note.query.all()
    return render_template('notes/notes.html', notes=notes)


def delNotes():
    ''' delete a note '''
