# from Classes.MathTree import MathTree

class BinaryHashTable(dict):
    def __setitem__(self, key, value):
        # if not isinstance(value, MathTree):
        #     raise ValueError("CustomDict only accepts MathTree objects.")
        if key in self:
            self[key].update(value)
        else:
            super().__setitem__(key, value)

    def __getitem__(self, key):
        item = super().get(key, None)
        if item:
            return item
        return None
