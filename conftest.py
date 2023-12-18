import pytest

from main import BooksCollector
@pytest.fixture
def sample_collector():
    collector = BooksCollector()
    collector.add_new_book("Звёздные войны")
    collector.add_new_book("Смерть на Ниле")
    collector.set_book_genre("Звёздные войны", "Фантастика")
    collector.set_book_genre("Смерть на Ниле", "Ужасы")
    return collector