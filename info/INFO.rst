OOpen
=====
*Object-Oriented file and path handling.*
-----------------------------------------



The std lib file and path options aren't very pythonic.

I should be able to perform basic tasks directly on the file.

License: MIT
++++++++++++

Status:
  In development. The public API is not formally documented and may change at anytime.
  Please pin the version you're using to avoid breakage.

`Semantic Versioning <http://semver.org/>`_
  I will commit to not breaking the public API within major versions. (Non breaking API starts at 1.0.0)

Donations
  If you would like to support it's author, you may do so via `gittip <https://www.gittip.com/AJHekman/>`_.
  Thanks for your support!

Example usage:
--------------

>>> from oopen import OOpen
>>> oofile = OOpen('example_file.py')

Retrieve and set the name of a file:
++++++++++++++++++++++++++++++++++++
>>> oofile.name
'example_file.py'
>>> oofile.name = 'test.txt'
>>> oofile.name
'test.txt'
>>> oofile.path
'/Users/ajhekman/Projects/oopen/oopen/test.txt'
>>> oofile.location
'/Users/ajhekman/Projects/oopen/oopen/'

Retrieve other file information:
++++++++++++++++++++++++++++++++
>>> oofile.sha1 # all of the hashes within hashlib are supported (md5 to sha 512)
'e90296612f91b8adf498884b20c8356113c83a73'
>>> oofile.modified_time
datetime.datetime(2013, 1, 14, 9, 10, 31) # << file times are represented as native datetime objects

