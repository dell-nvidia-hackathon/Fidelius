## Fidelius  
This project is a data masking and obfuscation tool designed to enhance privacy and security by intelligently handling Personally Identifiable Information (PII).  
   
## Description  
Fidelius is a localized data masking tool utilizing Generative AI. It allows users to upload files and select between two methods of data protection: redaction or obfuscation. The tool is currently compatible with two types of files: CSV/Excel and PDF/Text documents. It is designed to protect sensitive information while maintaining the integrity and usability of the data.  
   
## How To Use  
1. **Clone this repository:**  
   ```bash  
   git clone [repository-url]  
   ```  
2. **Run the application:**  
   ```bash  
   python run.py  
   ```  
3. **Upload your files:** The tool currently supports CSV/Excel and PDF/Text formats.  
4. **Select the desired operation:** Choose either to obfuscate or redact the identified PII.  
5. **Generate the new file:** The system will process your file and provide a new version with the masked data.  
   
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
