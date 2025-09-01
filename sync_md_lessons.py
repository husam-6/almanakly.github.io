# %% 
import os

template = """
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
	<link rel="stylesheet" href="../assets/css/slides.css">
  <script src="https://remarkjs.com/downloads/remark-latest.min.js"></script>

</head>
<body>

<textarea id="source">
{file_contents}
</textarea> <script> var slideshow = remark.create(); </script> </body> </html>
"""

directory = "/Users/husam/cs102/almanakly.github.io/md"
output_dir = "/Users/husam/cs102/almanakly.github.io/lessons"
for root, dirs, files in os.walk(directory):
    for file_name in files:
        if not file_name.endswith(".md"):
            continue
        
        # Read markdown file
        file_path = os.path.join(root, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            contents = f.read()

        # Compute title (strip .md extension)
        title = os.path.splitext(file_name)[0]

        # Build HTML with template
        html_content = template.format(
            title=title,
            file_contents=contents
        )

        # Compute destination path (same name but .html)
        html_name = f"CS102 {title}.html"
        output_path = os.path.join(output_dir, html_name)

        # Write output file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Converted: {file_name} → {html_name}")