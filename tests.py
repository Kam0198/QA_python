from main import BooksCollector
import pytest


class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Принцесса")
        collector.set_book_genre("Принцесса", "Мультфильмы")
        books_for_children = collector.get_books_for_children()
        assert "Принцесса" in books_for_children

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("12 стульев")
        collector.set_book_genre("12 стульев", "Комедии")
        assert collector.get_book_genre("12 стульев") == "Комедии"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        books_with_genre = collector.get_books_with_specific_genre("Ужасы")
        assert "Сияние" in books_with_genre

    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        genre = collector.get_book_genre("NonexistentBook")
        assert genre is None

    def test_add_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Голодные игры")
        assert collector.get_book_genre("Голодные игры") == ""

    def test_add_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Источник")
        collector.add_book_in_favorites("Источник")
        favorites = collector.get_list_of_favorites_books()
        assert "Источник" in favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Зелёный свет")
        collector.add_book_in_favorites("Зелёный свет")

        collector.delete_book_from_favorites("Зелёный свет")
        favorites_after_delete = collector.get_list_of_favorites_books()
        assert "Зелёный свет" not in favorites_after_delete

    def test_books_with_age_rating_not_for_children_books(self):
        collector = BooksCollector()
        collector.add_new_book("Мгла")
        collector.set_book_genre("Мгла", "Ужасы")
        books_for_children = collector.get_books_for_children()
        assert "Мгла" not in books_for_children

    def test_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book("Одноэтажная Америка")
        collector.add_new_book("Одноэтажная Америка")
        assert len(collector.get_books_genre()) == 1

    def test_get_book_genre(self, sample_collector):
        genre_book1 = sample_collector.get_book_genre("Звёздные войны")
        genre_book2 = sample_collector.get_book_genre("Смерть на Ниле")
        assert genre_book1 == "Фантастика"
        assert genre_book2 == "Ужасы"
