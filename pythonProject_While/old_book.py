searched_book = input()
books_count = 0
books_checked = 0
current_book = input()

while searched_book != current_book:

    if current_book =='No More Books':
        break
    current_book = input()
    books_checked += 1

if searched_book ==current_book:
    print(f'You checked {books_checked} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_checked} books.')