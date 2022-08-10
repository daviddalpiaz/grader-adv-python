# %%

import pathlib 

# Create grading routine directory
#p = pathlib.Path("/grade/run/")
#p.mkdir(mode=0o777, parents=True, exist_ok=True)

# Import code file using absolute path 
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from code_feedback_adv import Feedback

# %%

# Establish setup done by PLTest
Feedback.set_main_output()
Feedback.set_test("Hello")

# %%

# Test code
import numpy as np 

x = np.matrix([0])

Feedback.expect_numpy_array(x, 'x')
