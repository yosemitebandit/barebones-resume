pdf resumes from markdown

#### usage
* write your resume in a markdown file, see `resume.md` for an example
* make it html `poetry run python compose.py resume.md > index.html`
to send your html-ified resume into a basic template
* adjust `styles.css` to your liking
* view the output page with `python3 -m http.server`
and maybe export it as a pdf via your browser -- see `resume.pdf` for an example
