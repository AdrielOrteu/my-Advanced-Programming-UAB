import numpy as np

### THIS ISN'T THE CORRECT VECTOR CLASS USED IN THE EXERCISE ###
### IT'S JUST MY (FAILED) ATTEMPT A CREATING IT ###

class Vector:
    
    def __init__(self, v):
        self._v = np.array(v)
    
    def __str__(self):
        return f"{self._v.tolist()}"
    
    def __add__(self, other):
        if len(self._v) == len(other):
            return self._v + other.v
        else:
            raise AssertionError
    def __sub__(self, other):
        if len(self._v) == len(other):
            return np.linalg.norm(self._v - other.v)
        else:
            raise AssertionError
    def __mul__(self, other):
        return np.dot(self._v, other.v)
    
    def __len__(self):
        return len(self._v)
    
    @property
    def v(self):
        return self._v