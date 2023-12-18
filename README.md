
## Описание тестов
1. Тест проверяет добавление двух книг - test_add_new_book_add_two_books 
2. Тест проверяет, что добавленная книга с жанром "Мультфильмы" находится в разделе для детей - test_get_books_for_children
3. Тест проверяет, что указанный жанр совпадает с тем, что мы задали - test_set_book_genre
4. Тест проверяет, что добавленная книга находится в списке этого жанра - test_get_books_with_specific_genre
5. Тест на проверку добавления несуществующей книги - test_get_book_genre_nonexistent_book
6. Тест проверяет добавлние книги без указания жанра - test_add_book_without_genre
7. Тест проверяет добавление книги в Избранное - test_add_book_from_favorites
8. Тест проверяет удаление книги из Избранного - test_delete_book_from_favorites 
9. Тест проверяет, что книга с жанром "Ужасы" не попала в раздел для детей - test_books_with_age_rating_not_for_children_books 
10. Тест на проверку добавления одной и той же книги - test_add_same_book_once
11. Тест на получение жанра книги по ее названию - test_get_book_genre 