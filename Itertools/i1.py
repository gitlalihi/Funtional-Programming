#Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator.
class CombinedIterator:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.current_iterable = iter(self.iterables[0])
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.current_iterable)
        except StopIteration:
            self.current_index += 1
            if self.current_index < len(self.iterables):
                self.current_iterable = iter(self.iterables[self.current_index])
                return next(self.current_iterable)
            else:
                raise StopIteration

def create_and_display_iterator(*iterables):
   
    combined_iterator = CombinedIterator(*iterables)
    print(f"Type of the iterator: {type(combined_iterator).__name__}")
    print("Elements of the iterator:")
    for element in combined_iterator:
        print(element)


list1 = [1, 2, 3]
tuple1 = ('a', 'b', 'c')
set1 = {4, 5, 6}
create_and_display_iterator(list1, tuple1, set1)
