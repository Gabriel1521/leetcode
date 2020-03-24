#Tokenizer/Embedding
#BERT Tokenization


#Method 1
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

tokenized_text = tokenizer.tokenize(pad_text)

indexed_tok = tokenizer.convert_tokens_to_ids(tok_text)

tokenized_text = [tokenizer.tokenize(i) for i in train_samples]
input_ids = [tokenizer.convert_tokens_to_ids(i) for i in tokenized_text]
input_labels = get_dummies(train_labels)  # 使用 get_dummies 函数转换标签

train_set = TensorDataset(torch.LongTensor(input_ids),
                          torch.FloatTensor(input_labels))
train_loader = DataLoader(dataset=train_set,
                          batch_size=4,
                          shuffle=True)

#Embedding Matrix
list(tokenizer.vocab.keys())[5000:5020]

def embedding_bert():
    model = BertModel.from_pretrained('bert-base-uncased')
    bert_embeddings = list(model.children())[0]
    bert_word_embeddings = list(bert_embeddings.children())[0]
    mat = bert_word_embeddings.weight.data.numpy()
    return mat
