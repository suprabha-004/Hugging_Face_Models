from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key="",
)

result = client.question_answering(
	inputs={
	"question": "What is my name?",
	"context": "My name is Clara and I live in Berkeley."
},
	model="distilbert/distilbert-base-cased-distilled-squad"
)

print(result)
