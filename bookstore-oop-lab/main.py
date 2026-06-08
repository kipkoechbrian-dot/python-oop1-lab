# ==========================================
# Book Class
# ==========================================

class Book:

    # Constructor
    def __init__(self, title, page_count):

        # Public attribute
        self.title = title

        # Property setter validation
        self.page_count = page_count

    # Property getter
    @property
    def page_count(self):
        return self._page_count

    # Property setter
    @page_count.setter
    def page_count(self, value):

        # Ensure page_count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Method
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


# ==========================================
# Coffee Class
# ==========================================

class Coffee:

    # Constructor
    def __init__(self, size, price):

        # Property setter validation
        self.size = size

        # Public attribute
        self.price = price

    # Property getter
    @property
    def size(self):
        return self._size

    # Property setter
    @size.setter
    def size(self, value):

        # Ensure size is Small, Medium, or Large
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Method
    def tip(self):
        print("This coffee is great, here's a tip!")

        # Increase price by 1
        self.price += 1


# ==========================================
# User Input Section
# ==========================================

# Book Object

book_title = input("Enter book title: ")
book_pages = int(input("Enter page count: "))

book = Book(book_title, book_pages)

print("\nBook Details")
print("Title:", book.title)
print("Pages:", book.page_count)

book.turn_page()


# Coffee Object

coffee_size = input("\nEnter coffee size (Small, Medium, Large): ")
coffee_price = float(input("Enter coffee price: "))

coffee = Coffee(coffee_size, coffee_price)

print("\nCoffee Details")
print("Size:", coffee.size)
print("Price:", coffee.price)

coffee.tip()

print("New Price:", coffee.price)