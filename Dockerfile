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
COPY code_feedback.py /python_autograder/

# Run the Deep Learning package requirements
RUN /bin/bash /install.sh
