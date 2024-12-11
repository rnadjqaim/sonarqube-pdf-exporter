SonarQube PDF Report Exporter
SonarQube PDF Report Exporter is a simple, client-facing open-source tool designed to export SonarQube project reports as PDF files. This tool empowers teams to generate high-quality, sharable, and comprehensive reports for stakeholders.

Features
Export SonarQube analysis reports as PDF.
Include project metrics like bugs, vulnerabilities, code smells, and more.
Customizable fields to suit client-facing needs.
Lightweight, easy to integrate, and extend.
Requirements
Python 3.x or above
SonarQube server with API access
Required Python libraries (see requirements.txt)
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/sonarqube-pdf-reporter.git
cd sonarqube-pdf-reporter
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Configuration:

Create a .env file in the project root:
bash
Copy code
touch .env
Add the following placeholders:
env
Copy code
SONARQUBE_URL=http://your-sonarqube-server.com
SONARQUBE_TOKEN=your_sonar_api_token
PROJECT_KEY=your_project_key
Usage
Run the script to generate a PDF report:

bash
Copy code
python export_pdf.py
The generated PDF will be available in the reports/ directory.

Configuration
Customize the following variables in the .env file:

SONARQUBE_URL: URL of the SonarQube server.
SONARQUBE_TOKEN: Your SonarQube API token.
PROJECT_KEY: Key of the project to export the report for.
Contribution Guide
We welcome contributions! Follow these steps:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature-name"
Push to your fork:
bash
Copy code
git push origin feature-name
Create a pull request.
Future Enhancements
Add support for exporting reports in other formats (e.g., Excel, Word).
Enhance customization options for PDF content.
Build a web interface for easier access.
Acknowledgments
Special thanks to the contributors and the open-source community for inspiring this project!
