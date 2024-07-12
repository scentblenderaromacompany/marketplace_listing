from transformers import BertTokenizer, TFBertModel
import tensorflow as tf

def train_text_extraction_model(train_data_path, model_save_path):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = TFBertModel.from_pretrained('bert-base-uncased')

    # Dummy data for example purposes
    texts = ["example sentence 1", "example sentence 2"]
    inputs = tokenizer(texts, return_tensors='tf', padding=True, truncation=True)
    
    outputs = model(inputs)
    print(outputs)

    model.save_pretrained(model_save_path)

if __name__ == "__main__":
    train_data_path = '/workspaces/marketplace_listing/train_data/text_data.csv'
    model_save_path = '/workspaces/marketplace_listing/models/text_extraction_model'
    train_text_extraction_model(train_data_path, model_save_path)
