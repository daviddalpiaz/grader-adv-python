I'm exploring a Python class that has a built-in default return value without calling a class method. The goal of the class is to store multiple attributes about the state of data.

Consider the following bare-bones class definition:

```python
class TestDefaultReturn():
    # Initialize a class variable with a default value
    okay = False 

    # Create a constructor to set the okay value
    def __init__(self, okay:bool = True) -> None:
        self.okay = okay
    
    # Establish an accessor method for the `okay` class variable
    def is_okay(self) -> bool:
        return self.okay

# Initialize an object with the default `okay` value of False
my_instance = TestDefaultReturn(False)
```

Under usual OOP techniques, the `okay` field would be accessed via a getter method like `.is_okay()`.

```python
if my_instance.is_okay():
  print("Instance returned True")
else: 
  print("Instance returned False")

# "Instance returned False"
```

I'm interested in being able to return a single value from the `my_instance` class object without needing to use an accessor method. e.g.

```python
if my_instance:
  print("Instance returned True")
else: 
  print("Instance returned False")
```

As it stands now, the above `if-else` would return `True`. To me, this indicates that it's possible to return a _single_ value. 