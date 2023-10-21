import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Гарри Поттер')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Гордость и предубеждение и зомби','Ужасы')
    collector.set_book_genre('Гарри Поттер', 'Фантастика')
    collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    return collector
