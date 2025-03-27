# CopyeditGPT
A Flask app that uses Ollama's local LLM for copy editing. 

## Welcome to CopyeditGPT!
This project helps you utilize Ollama's LLM capabilities to copy edit your documents. Submit a .txt or .docx file with writing of any kind, and the site will return a document that has been edited for spelling, grammar, punctuation, syntax, and other specifications of the Chicago Manual of Style. 

The web app handles documents of any reasonable length by breaking them down into chunks of about 4000 characters, processing them sequentially using Ollama, then returning the results in one file. Be mindful that this app breaks documents down by paragraph, so if your document has huge paragraphs (specifically, two successive paragraphs totaling more than about 1500 words), then it may result in an error. 

### How to Use
You will need:
1. Ollama installed and running on your system
2. The llama3.2-8b-instruct-128k:latest model installed
3. Your writing in a .txt or .docx file
4. Patience (especially with long documents)

Currently, this code functions only in a local Flask environment. Run the flask app and navigate to http://localhost:5000/ in order to try it out!

### Setup Instructions

1. Install Ollama from the official website if you haven't already
2. Install the required model:
```bash
ollama pull llama3.2-8b-instruct-128k:latest
```
3. Start the Ollama server:
```bash
ollama serve
```
4. Install Python requirements:
```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python app.py
```

### Supported File Types
Currently this editor accepts:
- .txt files
- .docx files

Support for additional formats like .doc and LaTeX files is planned for future updates.

### Processing Time
Processing time depends on your system's capabilities and the size of the text. The application processes text in chunks of approximately 4000 characters each. Processing speed will vary based on your hardware and the specific model configuration.

### How to Process Your Results
You will get back a file with corrections made at the LLM's discretion. You can download the results in either .txt or .docx format. You will want to compare this to your old document and choose which changes to keep or reject. For that, you can use Microsoft Word's compare tool, under the review panel.

### How to Contribute to this Project
Please contribute!

This project still has a lot of room for improvement, and I hope to see it through. So if you're looking for an open source Flask project that will be easy to jump into, this is a great choice! 

#### Aspects that need to be implemented or improved:
#### More modern frontend framework and design 
The site has a little bit of Bootstrap usage. Otherwise this is just plain HTML and needs a lot of work. We need more robust error message feedback for incorrect entries, including incorrect files, exceeding limitations, etc.

#### Progress bar and real-time updates
An interim page to provide feedback on the progress as the document is processing. The groundwork for WebSocket support is in place but needs to be implemented.

#### Additional file format support
Support for additional file formats like .doc, LaTeX, and RTF.

#### Ability to customize prompts and processing parameters
Currently, the settings for the LLM processing are fixed, but it would be beneficial to implement a frontend panel which lets the client alter some of the settings. They may want to alter the prompt, change which style guide to follow, adjust the temperature parameter, or modify other settings.

#### User registration and file storage
The user should be able register a username and navigate to the results page and download their edited files at anytime from a database. SQLAlchemy needs to be built in for storing files generated in the results section.

#### Ensure consistency and accuracy of results
Experiment with the prompt and other parameters to ensure optimal results. With the current settings, it may tend to over-edit. With the current method of splitting up text, the model may be confused by sentences abruptly ending and starting.

### Thanks for reading!
Please give the app a try and review the code! Constructive criticism and contributions are welcome to help improve the project.

Thank you to everyone who has contributed!