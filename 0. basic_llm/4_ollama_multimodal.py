from PIL import Image
from io import BytesIO
import base64
from langchain_ollama import OllamaLLM  # Import the updated OllamaLLM

# Open image and convert to base64 string
buffered = BytesIO()
pil_image = Image.open("../data/test2.jpg")
pil_image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

# Initialize OllamaLLM (new name after moving to langchain-ollama)
llm = OllamaLLM(model="llava")

# Prepare the input text and image as a formatted string
input_text = "Tell me if there is an emergency event in this picture."
formatted_input = f"{input_text}\n{img_str}"  # Combine text and image base64

# Invoke the model
response = llm.invoke(formatted_input)

# Output the response from the model
print(response)
