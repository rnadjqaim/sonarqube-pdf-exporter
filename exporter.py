import requests
from fpdf import FPDF
import json

def get_sonarqube_data(url, project_key, auth_token):
    """
    Fetch SonarQube project data using the REST API.

    :param url: SonarQube server URL
    :param project_key: Key of the project to fetch data for
    :param auth_token: Authentication token
    :return: JSON data from SonarQube
    """
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(f"{url}/api/measures/component", params={
        'component': project_key,
        'metricKeys': 'bugs,vulnerabilities,code_smells,coverage,duplicated_lines_density'
    }, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def generate_pdf_report(data, output_file):
    """
    Generate a PDF report from SonarQube data.

    :param data: JSON data from SonarQube
    :param output_file: Path to save the generated PDF report
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="SonarQube Project Report", ln=True, align='C')

    if 'component' in data:
        project_name = data['component']['name']
        pdf.cell(200, 10, txt=f"Project: {project_name}", ln=True, align='L')

        measures = data['component'].get('measures', [])
        for measure in measures:
            metric = measure['metric']
            value = measure['value']
            pdf.cell(200, 10, txt=f"{metric}: {value}", ln=True, align='L')
    else:
        pdf.cell(200, 10, txt="No data available for the project.", ln=True, align='L')

    pdf.output(output_file)

if __name__ == "__main__":
    SONARQUBE_URL = "https://your-sonarqube-url.com"
    PROJECT_KEY = "your-project-key"
    AUTH_TOKEN = "your-auth-token"

    try:
        print("Fetching SonarQube data...")
        sonarqube_data = get_sonarqube_data(SONARQUBE_URL, PROJECT_KEY, AUTH_TOKEN)

        print("Generating PDF report...")
        generate_pdf_report(sonarqube_data, "sonarqube_report.pdf")

        print("Report generated successfully: sonarqube_report.pdf")
    except Exception as e:
        print(f"Error: {e}")
