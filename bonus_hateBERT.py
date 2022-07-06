from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("GroNLP/hateBERT")

model = AutoModelForMaskedLM.from_pretrained("GroNLP/hateBERT")