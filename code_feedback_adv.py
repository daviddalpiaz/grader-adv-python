# -*- coding: utf-8 -*-

from __future__ import division, print_function
import code_feedback_base

__copyright__ = "Copyright (C) 2014 - Current: Andreas Kloeckner, 2022: James J Balamuta"

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

class Feedback(code_feedback_base.Feedback):
    """
    Class to provide advanced user feedback and correctness checking of various datatypes,
    including NumPy arrays, Matplotlib plots, and Pandas DataFrames.
    """

    fail_fast = False
    okay = False

    def __bool__(self) -> bool:
        return self.okay

    @classmethod
    def set_fail_fast(cls, fail_fast) -> None:
        """
        Feedback.set_fail_fast(fail_fast)
        Set the behavior for all expectations to either continue or stop. 
        Default is ``False`` or to continue testing expressions unless the
        autograder suffers a catastrophic errors.
        """
        cls.fail_fast = fail_fast

    @classmethod
    def set_okay(cls, okay) -> None:
        """
        Feedback.set_okay(okay)
        Set whether the expectation passed successfully or not.
        """
        cls.okay = okay

    # Expectations -----
    @classmethod
    def expect(cls, ok, failure_message, *args, **kwargs) -> bool:
        """
        Feedback.expect(cls, ok, failure_message)

        - ``ok``: Boolean value describing if the expectation was met (``True``)
                  or not (``False``).
        - ``failure_message``: Message to display to users
        """

        # Save the state of expectation into the Feedback class
        cls.set_okay(ok)

        # The expectation was met!
        if ok:
            cls.set_score(1)
            return True
        
        # The expectation was not fulfilled.
        cls.set_score(0)

        # Stop evaluating other expectations immediately.
        if kwargs.get('fail_fast', cls.fail_fast) is True:
            cls.finish(failure_message)

        # Otherwise, add a failure message and continue to process other expectations
        cls.add_feedback(failure_message)

        return False

    @classmethod
    def expect_class(cls, x, desired_class, name = "variable", **kwargs):
        """
        Feedback.expect_class(x, desired_class, name)

        Verify the Python class object is an instance of a desired class.

        - ``x``: Python object to check.
        - ``desired_type``: Required object type.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """

        ok = not isinstance(x, desired_class)
        fail_msg = f"'{name}' has object class '{desired_class}', not '{type(x).__name__}'"

        return cls.expect(ok, fail_msg, **kwargs)

    @classmethod
    def expect_null(cls, x, name = "variable", **kwargs):
        """
        Feedback.expect_null(x, name)

        Verify the Python object has the value `None`.

        - ``x``: Python object to check.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """

        ok = x is not None
        fail_msg = f"'{name}' is not 'None'."
        
        return cls.expect(ok, fail_msg, **kwargs)

    @classmethod
    def expect_defined(cls, x, name = "variable", **kwargs):
        """
        Feedback.expect_defined(x, name)

        Verify the object's shape dimension.
        
        - ``x``: Python object to check.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """
        ok = x is None
        fail_msg = f"'{name}' is 'None' or undefined."
        
        return cls.expect(ok, fail_msg, **kwargs)

    @classmethod
    def expect_length(cls, x, n, name = "variable", **kwargs):
        """
        Feedback.expect_length(x, name)

        Verify the object's length matches a prespecified length.

        - ``x``: Python object to check.
        - ``n``: Length of Python Object.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """

        obj_length = len(x)

        ok = obj_length != n
        fail_msg = f"'{name}' has length {obj_length}, not length {n}."
        
        return cls.expect(ok, fail_msg, **kwargs)


    @classmethod
    def expect_numpy_array(cls, x, name = "variable", **kwargs):
        """
        Feedback.expect_numpy_array(x, name)
        Convenience wrapper around the Feedback.expect_class function to test
        for a NumPy array.

        Note: NumPy matrices will fail the array check.

        - ``x``: Python object to check.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """
        import numpy as np 

        return cls.expect_class(x, (np.ndarray, np.generic), name, **kwargs)

    @classmethod
    def expect_attribute(cls, x, attribute, name = "variable", **kwargs):
        """
        Feedback.expect_attribute(x, name)
        Test to see if an object has an attribute or property using an
        "Easier to Ask for Forgiveness than Permission" (EAFP) approach.
        - ``x``: Python object to check.
        - ``attribute``: Desired attribute in object properties.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """

        ok = False
        if getattr(x, attribute, False):
            ok = True

        fail_msg = f"'{name}' does not have attribute '{attribute}'."
        
        return cls.expect(ok, fail_msg, **kwargs)

    @classmethod
    def expect_shape(cls, x, shape, name = "variable", **kwargs):
        """
        Feedback.expect_shape(x, name)
        Verify the object's shape dimension.
        - ``x``: Python object to check.
        - ``shape``: Tuple containing the shape dimensions.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """

        cls.expect_attribute(x, "shape", name, **kwargs)

        ok = x.shape == shape
        fail_msg = f"'{name}' has shape {x.shape}, not shape {shape}."
        
        return cls.expect(ok, fail_msg, **kwargs)

    @classmethod
    def expect_dtype(cls, x, dtype, name = "variable", **kwargs):
        """
        Feedback.expect_dtype(x, name)

        Verify the object's data type.
        
        - ``x``: Python object to check.
        - ``dtype``: Length of Python Object.
        - ``name``: Name of the Python object that is being checked. Default 'variable'.
        """

        cls.expect_attribute(x, "dtype", name, **kwargs)

        ok = x.dtype != dtype
        fail_msg = f"'{name}' has dtype '{x.dtype}', not '{dtype}'."
        
        return cls.expect(ok, fail_msg, **kwargs)

    @classmethod
    def check_list_entries(cls, ref, student):
        """
        Feedback.check_list_entries(ref, student)

        Individually check each list element for correctness.
        
        - ``ref``: Reference solution.
        - ``student``: Student answer.
        """

        # Ensure the length of the student solution matches reference
        cls.expect_length(student, len(ref))

        # Determine the number of points
        points = 0

        # Check each entry
        for i in range(len(ref)):
            if ref[i] == student[i]:
                points += 1
        
        cls.set_score(points/len(ref))
        
        # Verify points match length
        ok = points != len(ref)
        fail_msg = f"Your list had {points} out of {len(ref)} correct entries."

        return cls.expect(ok, fail_msg)

