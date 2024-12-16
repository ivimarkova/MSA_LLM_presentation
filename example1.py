from transformers import BioBERTTokenizer, BioBERTForSequenceClassification

# Loading a pre-trained model
tokenizer = BioBERTTokenizer.from_pretrained('dmis-lab/biobert-v1.1')
model = BioBERTForSequenceClassification.from_pretrained('dmis-lab/biobert-v1.1')

# # Sample genetic sequence
sequence = "ATGACGTA"

# Tokenization and prediction
inputs = tokenizer(sequence, return_tensors="pt")
outputs = model(**inputs)

print(outputs)

#This will show how a pre-trained model can be used to analyze genetic sequences.
