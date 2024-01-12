from transformers import AutoModel, AutoTokenizer


def main():
    # Model name to use for text summarization
    # model_name = "facebook/bart-large-cnn"
    model_name = "sshleifer/distilbart-cnn-12-6"

    # If model files exist locally, load them from disk.
    # Otherwise, download them from HuggingFace's model hub.
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("[INFO] Model files have been downloaded.")

    # Save the model files locally if they haven't been saved yet.
    model.save_pretrained(model_name)
    tokenizer.save_pretrained(model_name)


if __name__ == "__main__":
    main()
