"""Text summarizer class"""
import torch
from transformers import AutoTokenizer, BartForConditionalGeneration
from unidecode import unidecode


class TextSummarizer(object):
    def __init__(self, model_name="sshleifer/distilbart-cnn-12-6"):
        self.model = BartForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def preprocess_text(self, text):
        text = text.replace("\n", "")
        text = unidecode(text)
        return text

    def summarize(self, input_text):
        input_text = self.preprocess_text(input_text)
        inputs = self.tokenizer(
            input_text,
            max_length=1024,
            truncation=True,
            return_tensors="pt",
        )
        summary_ids = self.model.generate(inputs["input_ids"])
        summary = self.tokenizer.batch_decode(
            summary_ids,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=True,
        )
        return summary[0]
