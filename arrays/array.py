import ctypes

class Array:
    def __init__(self, size):
        self.size = size
        self._capacity = max(16, 2*size)
        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()
        self.memory = [None]*self._capacity
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        return self.memory[idx]
    
    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result

    
    def expand_capacity(self):
        array_data_type = ctypes.py_object * 2*self.size
        new_memory = array_data_type()
        new_memory[:self.size] = self.memory
        del self.memory
        self.memory = new_memory
        self._capacity *= 2
    
    def append(self, value):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = value
        self.size += 1
    
    def insert(self, idx, value):
        if idx < 0 or idx >= self.size:
            raise ValueError(
                "idx is out of range"
            )
        if self.size >= self._capacity - 1:
            self.expand_capacity()
        self.memory[idx+1 : self.size+1] = self.memory[idx : self.size]
        self.memory[idx] = value
        self.size += 1


if __name__ == '__main__':

    array = Array(0)
    array.append(56)
    array.append('hello')
    print(array)
    #56, hello,

    array.insert(0, 'A0')
    print(array)
    # A0, 56, hello,

    array.insert(2, 'A2')
    print(array)
    # A0, 56, A2, hello,

    array.insert(1, -9)
    print(array)
    # A0, -9, 56, A2, hello,