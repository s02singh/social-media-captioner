from django.shortcuts import render
from transformers import AutoProcessor, AutoModelForCausalLM
import openai
from PIL import Image
import os


image_path = os.path.join('static', 'images', 'image.jpeg')



# Set OpenAI API credentials
openai.api_key = 'YOUR API KEY'

# Initialize the model and processor
processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")

def generate_caption(request):
    
    if request.method == 'POST':
        # Get the uploaded image from the request
        image_file = request.FILES.get('image')
        
        # Save the image locally
        
        with open(image_path, 'wb') as f:
            f.write(image_file.read())
        
        # Open the image
        image = Image.open(image_path)
        
        # Process the image
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        
        # Generate caption
        generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        # Generate rhyming caption using OpenAI API
        
        prompt = "Generate a short, catchy, engaging, hype Instagram caption using the prompt: " + generated_caption
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )
        rhyming_caption = response.choices[0].text.strip()
        
       
        # Render the result template
        return render(request, 'result.html', {
            'image_path': image_path,
            'generated_caption': generated_caption,
            'rhyming_caption': rhyming_caption
        })
    else:
        # Render the form template
        return render(request, 'index.html')
