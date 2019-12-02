# TF-IDF Comment Selection

If external knowledge classifier predicts that external knowledge is needed for a given question, then we will need to find the corresponding comment for the question. This module will predict top10 most possible comments for a given question. 

### Preprocessing

In order to improve the performance, we need some preprocessing of the questions as well as the comments. The `comments` folder contains `semart_train/semart_val/semart_test.csv`, which are obtained from the original SemArt dataset. The `questions` folder contains `need_external_knowledge.json`, which is the output of the external knowledge classifier. First, run

```bash
python preprocess.py
```

to get the preprocessed questions and comments. It will generate two output file, `preprocessed_comments.json` and `preprocessed_need_external_knowledge.json`

### TF-IDF

After preprocessing, we can run tf-idf algorithm to get the top10 possible comments for each question. Here we use N-gram TF-IDF algorithm, where N = 3. (We concatenate the adjacent 2 words and 3 words and add them to the original text.)

```bash
python tf_idf.py
```

It will generate `need_external_knowledge_comment_prediction.json` which contains the top 10 comments prediction result for each question.