"""Injects markdown into a small template.
"""

import markdown


input_filepath = 'resume.md'
template_filepath = 'template.html'

# Parse the markdown.
with open(input_filepath) as input_file:
  resume_data = input_file.read()
resume_html = markdown.markdown(resume_data)

# Load the template.
with open(template_filepath) as template_file:
  template_string = template_file.read()

# Inject the resume data and print it out.
print template_string % resume_html
