import requests
import json
import logging
import time

logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self, model="llama2-13b:latest"):
        self.base_url = "http://localhost:11434/api"
        self.model = model
        
    def generate(self, prompt, temperature=0.1):
        """
        Generate text using Ollama API
        """
        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "temperature": temperature,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            logger.error(f"Error calling Ollama API: {str(e)}")
            raise

def run_editor(submit_text, chunk_count):
    """Process text in chunks and apply editing"""
    try:
        client = OllamaClient(model="llama3.2-8b-instruct-128k:latest")
        with open("text_files/edited.txt", "w", encoding='utf-8', errors="ignore") as edited_text:
            run_count = 0
            chunks = chunk_text(submit_text)
            
            for chunk in chunks:
                edited_chunk = ollama_edit(client, chunk)
                edited_text.write(edited_chunk)
                
                run_count += 1
                progress = (run_count / chunk_count) * 100
                logger.info(f"Processing progress: {progress:.1f}%")
                print("Finished {:.0%}".format(run_count / chunk_count))
                
    except Exception as e:
        logger.error(f"Error in run_editor: {str(e)}")
        raise

def chunk_text(text, chunk_size=4000):
    """Split text into chunks while preserving paragraph integrity"""
    chunks = []
    current_chunk = ""
    current_size = 0
    
    paragraphs = text.split('\n')
    
    for paragraph in paragraphs:
        paragraph_size = len(paragraph) + 1  # +1 for newline
        
        if current_size + paragraph_size > chunk_size and current_chunk:
            chunks.append(current_chunk)
            current_chunk = paragraph + '\n'
            current_size = paragraph_size
        else:
            current_chunk += paragraph + '\n'
            current_size += paragraph_size
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

def ollama_edit(client, text):
    """Send text to Ollama for editing"""
    prompt = """Please act as a professional copy editor. Edit the following text according to these rules:
    1. Follow the Chicago Manual of Style for writing numbers, capitalization, headers, and punctuation
    2. Correct any obvious factual mistakes or inconsistencies
    3. Maintain the original voice and style of the writing
    4. Format quotes as ASCII directional quotes
    5. Fix spelling, grammar, and punctuation errors
    6. Only make necessary changes - do not rewrite content that is already correct

    Here is the text to edit:

    {text}

    Please provide only the edited text without any explanations or comments."""

    try:
        response = client.generate(
            prompt.format(text=text),
            temperature=0.1
        )
        return response.strip() + '\n\n'
    except Exception as e:
        logger.error(f"Error in ollama_edit: {str(e)}")
        raise