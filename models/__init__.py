#!/usr/bin/python3
"""
Creates an instance of the FileStorage class
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()