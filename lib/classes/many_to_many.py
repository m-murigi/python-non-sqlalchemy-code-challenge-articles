class Article:
    # stores all the article objects created (all =[]
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title

        # Validation for title
        if not isinstance(self._title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(self._title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")

        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        # Validation for name
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")

        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category

        # Validation for name and category
        if not isinstance(self._name, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(self._name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if not isinstance(self._category, str):
            raise TypeError("Category must be a string")
        if len(self._category) == 0:
            raise ValueError("Category must be longer than 0 characters")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author not in authors:
                authors[article.author] = 0
            authors[article.author] += 1
        return [author for author, count in authors.items() if count > 2]
