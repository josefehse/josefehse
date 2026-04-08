- 👋 Hi, I'm @josefehse.
- 👀 I'm interested in IT, coding, IoT, music, running and reading!
- 🌱 I'm currently learning French and Italian!
- 💞️ I'm looking to collaborate on any Azure related coding, PowerShell, CLI, Bicep, ARM Templates, Terraform.

---

## 🎸 Open Jam Management System

A lightweight Python/Flask web app for managing an open jam session — sign up, view the lineup, and remove yourself when you're done!

### Features

- **Join the Jam** — enter your name and 1–2 songs you want to perform.
- **Live Lineup** — see all participants in order with their songs.
- **Remove Entry** — remove any participant from the list with one click.
- **Persistent** — the list is saved to a local `jam_list.json` file so it survives restarts.

### Quick Start

```bash
# 1. Install dependencies (Python 3.8+ required)
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open your browser
#    http://127.0.0.1:5000
```

### Project Structure

```
├── app.py              # Flask application
├── templates/
│   └── index.html      # Jinja2 HTML template
├── requirements.txt    # Python dependencies
└── jam_list.json       # Auto-created; stores the jam list
```

### Notes

- No database or login required — prototype-quality and intentionally simple.
- Delete `jam_list.json` to reset the list.

---

<!---
josefehse/josefehse is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
