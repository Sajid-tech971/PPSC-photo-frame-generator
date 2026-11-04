PABNA PHOTO FRAME GENERATOR — AUTO-DETECT FRAME LIBRARY

HOW IT WORKS
The website automatically scans the project's frames/ folder through server.py.
Add a new supported frame file to that folder and it appears on the website within about 3 seconds.
No HTML editing or user frame upload is required.

SUPPORTED FILES
.png, .jpg, .jpeg, .webp, .gif, .svg
For best results use a transparent PNG or SVG overlay, with the photo opening transparent.

RUN ON WINDOWS
1. Extract the entire project folder.
2. Keep index.html, server.py, run_local_server.bat and frames/ together.
3. Install Python 3 if needed.
4. Double-click run_local_server.bat.
5. The browser opens http://127.0.0.1:8000.
6. Add your own designed frames into frames/. They appear automatically within about 3 seconds.
7. Select a frame, upload a photo, adjust it, and download the composed PNG.

FRAME NAMING
Names are generated from filenames:
  science_fair_2027.png -> Science Fair 2027
Use clear filenames to make the template list easy to understand.

IMPORTANT
- Do not open index.html directly as file://; use run_local_server.bat.
- Keep frame files in the frames/ folder beside index.html.
- The site only displays project-owned frames. It does not provide an end-user custom frame upload control.
- This is a local project server bound to 127.0.0.1; it is not a public hosting server.
