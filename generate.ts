import { mdToPdf } from 'md-to-pdf';
import { readFileSync } from 'fs';

const cssContent = readFileSync('./styles.css', 'utf-8');
const markdownContent = readFileSync('./resume.md', 'utf-8');

async function generatePDF() {
  const pdf = await mdToPdf(
    { content: markdownContent },
    {
      dest: 'resume.pdf',
      css: cssContent,
      pdf_options: {
        format: 'Letter',
        margin: {
          top: '20mm',
          right: '20mm',
          bottom: '20mm',
          left: '20mm',
        },
      },
    }
  );

  if (pdf) {
    console.log('PDF generated: resume.pdf');
  }
}

generatePDF().catch(console.error);
