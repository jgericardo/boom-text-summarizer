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
