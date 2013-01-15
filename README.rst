=====
OOpen
=====

***************************************
Object-Oriented file and path handling.
***************************************

The std lib file and path options aren't very pythonic. I should be able to perform basic tasks directly on the file.

**Status: In development.** Small part of a larger (and unshared) project.

License: Mit

Example usage:
==============

>>> from oopen import OOpen
>>> a = OOpen('example_file.py')
>>> a.name
'example_file.py'
>>> a.path
'/Users/ajhekman/Projects/oopen/oopen/example_file.py'
>>> a.location
'/Users/ajhekman/Projects/oopen/oopen'
>>> a.name = 'test'
>>> a.path
'/Users/ajhekman/Projects/oopen/oopen/test'
>>> a.name = 'example_file.py'
>>> a.sha1
'e90296612f91b8adf498884b20c8356113c83a73'
>>> a.modified_time
datetime.datetime(2013, 1, 14, 9, 10, 31)

