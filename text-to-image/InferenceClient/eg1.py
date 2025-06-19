from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="together",
    api_key="",
)

# output is a PIL.Image object
image = client.text_to_image(
	"Pirate ship",
	model="black-forest-labs/FLUX.1-dev",
)

image.show()