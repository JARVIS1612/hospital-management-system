# Hospital Management System

## How to set-up
1. Clone the git hub repo
<code>git clone https://github.com/JARVIS1612/hospital-management-system.git</code>
2. Create a virtual environment
<code> python -m venv <b>vertual-environment-name</b></code>
3. Install python dependencies mentioned in requirements.txt
<code>pip install -r requirements.txt</code>
4. Add deep learning models
<code>URL: https://drive.google.com/drive/folders/1iA8gntNtYeoxFqrURcl8ViEQ-D_VHTMn?usp=sharing
download these files and store them in disease_checker/Models</code>
5. Run migration commands in given order
<code>python manage.py makemigrations</code>
<code>python manage.py migrate</code>

## Start application
<code>python manage.py runserver</code>
