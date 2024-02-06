class Sort:
    def quick_sort(self,set_of_items):
        arr = list(set_of_items)
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]

        return self.quick_sort(less) + equal + self.quick_sort(greater)