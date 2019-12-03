# External Knowledge Classifier

The external knowledge classifier will predict whether external knowledge is needed to answer a question given its corresponding painting. 

### Feature Extraction

For a given question and its corresponding painting. For the question, we use pretrained BERT to encode the question into a fixed length vector. 

First download pretrained model to the folder

```bash
wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-24_H-1024_A-16.zip
```

```bash
unzip uncased_L-24_H-1024_A-16.zip
```

Install the following packages (https://github.com/hanxiao/bert-as-service)

```bash
pip install bert-serving-server
```

```bash
pip install bert-serving-client
```

Then run BERT service in the backend

```bash
bert-serving-start -model_dir ./uncased_L-24_H-1024_A-16/ -num_worker=1
```

For the painiting, we use pretrained ResNet-152 for feature extraction and also encode each painting into a fixed length vector. The extracted features for the all the paintings within SemArt Dataset can be download here,

```bash
wget https://semart.s3.amazonaws.com/image_features.json
```

Once we have BERT service running in the backend and have the painting features downloaded, we can run feature extraction code to extract features and the extracted features will be saved to `Cache Data` folder.

```bash
python features.py
```



### Run Classifier

After feature extraction is done, we can then train the classifier and test its performance. First, make sure `train/val/test.npy` files are in `Cache Data` folder, then run

```
python classifier.py
```

It will train the classifier on training set, validation its performance on validation set and predict result on test set. The prediction result of test set is stored in `need_external_knowledge.json` and `not_need_external_knowledge.json`.
