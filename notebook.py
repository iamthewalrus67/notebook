'''
Module for working with notes.
https://github.com/iamthewalrus67/notebook
'''

import datetime


last_id = 0


class Notebook:
    '''
    Class which represents a notebook.
    '''

    def __init__(self):
        '''
        Initialize a notebook with an empty list.
        '''
        self.notes = []

    def search(self, filter: str) -> list:
        '''
        Find all notes that match the given filter string.
        '''
        return [note for note in self.notes if note.match(filter)]

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.
        '''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its
        memo to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True

        return False

    def modify_tags(note_id, tags):
        '''
        Find the note with the given id and change its
        tags to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True

        return False

    def _find_note(self, note_id):
        '''
        Find note by id.
        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None


class Note:
    '''
    Class which represent a note.
    '''

    def __init__(self, memo, tags):
        '''
        Initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and unique id.
        '''
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        global last_id
        last_id += 1
        self.id = last_id

    def match(search_filter: str) -> bool:
        '''
        Check if note matches the filter.
        '''
        return search_filter in self.memo or search_filter in self.tags
