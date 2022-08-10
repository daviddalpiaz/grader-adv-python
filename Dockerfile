# Borrow the leg work done by the PrairieLearn project
FROM prairielearn/grader-python:latest

# Set a new label for the image
LABEL org.label-schema.license="AGPL-3.0" \
      org.label-schema.vcs-url="stat-prairielearn-uiuc/grader-adv-python" \
      org.label-schema.vendor="PrairieLearn Autograder for Python with Extended Feedback" \
      maintainer="James Joseph Balamuta <balamut2@illinois.edu>"

# Add layer for any additional Python packages
COPY install.sh /

# Add a modified version of code_feedback.py
COPY code_feedback_adv.py /python_autograder/

# Extend the PrairieLearn grader by:
# Added new expectations to the existing class
# (renaming the existing version on disk & copying the extended expectations in)
# and run install
RUN mv /python_autograder/code_feedback.py /python_autograder/code_feedback_base.py && \
    mv /python_autograder/code_feedback_adv.py /python_autograder/code_feedback.py && \
    /bin/bash /install.sh
