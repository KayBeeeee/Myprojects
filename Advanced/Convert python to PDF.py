import PyPDF2
import pyttsx3

def pdf_to_speech(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            
            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text()
            
            if not text.strip():
                print("The PDF does not contain readable text.")
                return

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()
            
            # Set voice properties (optional)
            rate = engine.getProperty('rate')  # Speed of speech
            engine.setProperty('rate', rate - 50)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  # Choose a voice (0 for male, 1 for female)
            
            # Speak the extracted text
            print("Reading the PDF content...")
            engine.say(text)
            engine.runAndWait()
    
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Specify the path to the PDF file
    pdf_path = input("Enter the path to the PDF file: ").strip()
    pdf_to_speech(pdf_path)
