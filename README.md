# Portfolio Project

Welcome to the Portfolio project! This repository contains a professional portfolio web application built with Django and Tailwind CSS.

## 🎨 Design System: Home Page Button Colors

The home page utilizes a cohesive button color system to ensure a premium user experience and consistent aesthetic across all interactive elements.

- **Primary Buttons (e.g., Download CV, Send Message, Active Filters):**
  - **Background:** Brand color (`bg-brand-600`)
  - **Text:** White (`text-white`)
  - **Hover State:** Darker brand color (`hover:bg-brand-700`) with subtle shadow or lift animations.

- **Secondary Buttons (e.g., Contact Me, Outline Links, Inactive Filters):**
  - **Background:** White (`bg-white`)
  - **Border:** Slate (`border-slate-200` or `border-2 border-slate-200`)
  - **Text:** Slate (`text-slate-700` or `text-slate-600`)
  - **Hover State:** Brand border (`hover:border-brand-500`) and light brand background (`hover:bg-brand-50`).

- **Special/Dark Buttons (e.g., Live Demo):**
  - **Background:** Dark Slate (`bg-slate-900`)
  - **Text:** White (`text-white`)
  - **Hover State:** Brand color (`hover:bg-brand-600`).

## ⚙️ Installation & Requirements Setup

Follow these instructions to set up the project locally and install all dependencies listed in `requirements.txt`.

### 1. Prerequisites
Ensure you have Python 3.x installed on your system.

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage your project's dependencies separately.
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### 3. Install Requirements
Install all necessary packages via pip using the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the root directory and add any necessary environment variables (such as Django Secret Key, Debug status, Database configurations, etc.).

### 5. Apply Migrations
Set up your local SQLite database (or whichever database you configure).
```bash
python manage.py migrate
```

### 6. Tailwind CSS Setup (django-tailwind)
This project uses `django-tailwind`. Ensure Node.js is installed since it's required to build the Tailwind output.
```bash
# Install tailwind dependencies
python manage.py tailwind install

# Start the tailwind development server
python manage.py tailwind start
```
*(Leave this running in a separate terminal window)*

### 7. Run the Development Server
In your main terminal, start the Django development server:
```bash
python manage.py runserver
```

You can now visit `http://127.0.0.1:8000` in your browser to view the application!
