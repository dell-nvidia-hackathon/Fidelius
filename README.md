# Fidelius  

This project is a data masking and obfuscation tool designed to enhance privacy and security by intelligently handling Personally Identifiable Information (PII).  

## Description  

Fidelius is a localized data masking tool utilizing Generative AI. It allows users to upload files and select between two methods of data protection: redaction or obfuscation. The tool is currently compatible with two types of files: CSV/Excel and PDF/Text documents. It is designed to protect sensitive information while maintaining the integrity and usability of the data.  

## How To Use in NVIDIA AI Workbench

1. **Clone this repository:**
   ```bash
   git clone [repository-url]
   ```

2. **Set Up the Application in Workbench:**

    - **Name:** Fidelius
    - **Class:** Web Application
    - **Icon URL:** Leave blank
    - **Start Command:** `python run.py`
    - **Port:** 5000 (ensure it's not used by another application)
    - **Health Check Command:** `curl -f "http://localhost:5000"`
    - **Stop Command:** `pkill -f "python run.py"`
    - **Auto Launch:** Selected
    - **URL:** `http://localhost:5000`
    - **URL Command:** Leave blank
    - **User Message:** Leave blank

3. **Run the Application:**
   Once you have configured the application in the NVIDIA AI Workbench, click start in your Workbench environment to run Fidelius.

4. **Upload your files:** The tool currently supports CSV/Excel and PDF/Text formats.

5. **Select the desired operation:** Choose to obfuscate or redact the identified PII.

6. **Generate the new file:** The system will process your file and provide a new version with the masked data.

## Features  

- **Data Masking:** Securely masks sensitive data using advanced AI techniques.  
- **File Support:** Handles CSV/Excel and PDF/Text files effectively.  
- **User Customization:** Allows users to specify additional PII fields for masking according to their needs.  
- **Local Processing:** Ensures that all data processing is done locally, enhancing security.  

## Future Enhancements  

- Support for more file types and formats.  
- Improved AI models for more accurate PII detection and masking.  
- Enhanced user interface for easier interaction and customization.  

---

This README provides a clear and structured explanation of the Fidelius project, its functionality, usage instructions, and future development plans, making it easy for users to understand and start using the tool.
