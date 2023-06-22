# Hospital Management System

## Setup Instructions

Follow these steps to set up the Hospital Management System:

1. **Clone the Repository:** Open a terminal and run the following command to clone the GitHub repository:

   ```bash
   git clone https://github.com/JARVIS1612/hospital-management-system.git
   ```

2. **Create a Virtual Environment:** Navigate to the project's root directory and create a virtual environment using the following command:

   ```bash
   python -m venv virtual-environment-name
   ```

   Replace `virtual-environment-name` with the desired name for your virtual environment.

3. **Install Python Dependencies:** Activate the virtual environment and install the required Python dependencies mentioned in the `requirements.txt` file:

   ```bash
   source virtual-environment-name/bin/activate  # Activate the virtual environment
   pip install -r requirements.txt
   ```

4. **Add Deep Learning Models:** Download the deep learning models from [this URL](https://drive.google.com/drive/folders/1iA8gntNtYeoxFqrURcl8ViEQ-D_VHTMn?usp=sharing). Once downloaded, move the model files to the `disease_checker/Models` directory within the project.

5. **Run Migrations:** Apply the database migrations using the following commands:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Application:** Launch the Hospital Management System by running the following command:

   ```bash
   python manage.py runserver
   ```

   This will start the development server, and you can access the application in your web browser at `http://localhost:8000`.

Make sure to replace `virtual-environment-name` with your preferred virtual environment name.

These instructions provide a comprehensive guide to setting up the Hospital Management System.
