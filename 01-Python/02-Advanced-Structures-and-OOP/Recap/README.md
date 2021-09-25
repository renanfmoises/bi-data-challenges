# Livecode

Let's model a [Multimedia Library](https://www.google.com/search?q=multimedia+library). Here are our hypothesis:

The library contains **4 types of media**:

- **BOOKS**
- **MOVIES**
- **CDS**
- **COMICS**

The library has a storage software allowing a few basic actions:

- To add a new media
- To borrow a media
- To return a media

The library use a dictionary to store its medias and an `interface` function allows to perform the actions.

Try to use functions for atomic actions, it's best practice.

Optional:

_Note: Some of those options can imply a change in the functions' signatures and other data structures._

- Handle the quantity of objects
- Associate a borrow to an user
- Specify a date of retrieval and fines on returns

## Scenarios

```python
# Library's storage
medias = {'BOOKS': {}, 'MOVIES': {'SW - Empire strikes back': True}, 'CDS': {}, 'COMICS': {}}

# Can add a new media
interface(medias, 'add', 'Harry Potter 1', 'BOOKS')
# => "Add completed"
# If the media type exists, else a message should be printed
interface(medias, 'add', 'Harry Potter 1', 'MANGAS')
# => "We do not have any MANGAS."

# Can borrow a media
interface(medias, 'borrow', 'Harry Potter 1', 'BOOKS')
# => "Borrow completed"
# If the media type exists, the title exists and is not already borrowed else a message should be printed
interface(medias, 'borrow', 'Harry Potter 1', 'BOOKS')
# => "The BOOK is already borrowed."
interface(medias, 'borrow', 'Harry Potter 2', 'BOOKS')
# => "The BOOKS you're looking for is not in our BOOKS."

# Can return a media
interface(medias, 'return', 'Harry Potter 1', 'BOOKS')
# => "Return completed"
# If the media type exists, the title exists and is borrowed else a message should be printed
interface(medias, 'return', 'Harry Potter 1', 'BOOKS')
# => "The BOOK was not borrowed."

```
