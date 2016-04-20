"""Injects markdown into a small template.
"""

import markdown


input_filepath = 'resume.md'
template_filepath = 'template.html'
output_filepath = 'index.html'

# Parse the markdown.
with open(input_filepath) as input_file:
  resume_data = input_file.read()
resume_html = markdown.markdown(resume_data)

# Load the template.
with open(template_filepath) as template_file:
  template_string = template_file.read()

# Inject the resume data.
output = template_string % resume_html

# Save the output file.
with open(output_filepath, 'w') as output_file:
  output_file.write(output)
