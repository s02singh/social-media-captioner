document.getElementById("upload-form").addEventListener("submit", function(event) {
  event.preventDefault();

  // Get the uploaded image file
  var imageFile = document.getElementById("image-upload").files[0];

  // Create a FileReader to read the image data
  var reader = new FileReader();

  reader.onload = function(event) {
    // Display the uploaded image
    var img = document.getElementById("uploaded-image");
    img.src = event.target.result;
  };

  reader.readAsDataURL(imageFile);
});

document.getElementById("generate-button").addEventListener("click", function() {
  var imageFile = document.getElementById("image-upload").files[0];

  generateCaption(imageFile)
    .then(caption => {
      document.getElementById("generated-caption").textContent = caption;
      console.log("Generated caption:", caption);
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

function generateCaption(imageFile) {
  // URL of the Chainer Image Captioning model

  const apiUrl = 'https://milhidaka.github.io/chainer-image-caption/';

  // Create a FormData object to send the image file
  var formData = new FormData();
  formData.append('file', imageFile);

  // Function to send the image and receive the caption
  return fetch(apiUrl, {
      method: 'POST',
      body: formData
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to generate caption');
      }
      return response.json();
    })
    .then(data => {
      const caption = data.caption;
      return caption;
    })
    .catch(error => {
      console.error('Error:', error);
      throw error;
    });
}
