# QA Pipeline SemArt

This README file will briefly describe the functionality of each folder within the pipeline. Each folder will contains a seperate README file to show how to run different module of the pipeline.

### Dataset

The dataset folder contains the machine generated QA dataset we use for our pipeline. We have divide the dataset into training set, validation set and test set based on the original division of SemArt dataset. Each set is saved in a JSON file which contains a list. Each item in the list contains one QA pair, as shown in the following,

```json
{
        "image": "23361-01lucret.jpg",
        "question": "who was frequently portrayed as a symbol of purity in the 16th and 17th century",
        "answer": "Lucretia",
        "need_external_knowledge": true
    }
```

The "need_external_knowledge" field indicate how the QA pair is generated. If it is true, then the QA pair is generated from the comment of the painting, we therefore need external knowledge to answer the question. Otherwise the question is generated from the painting directly. 

### iQAN

iQAN is the VQA model we use in our pipeline to answer visual-related question. It takes the question which  external knowledge classifier predicts that no external knowledge is needed as well as the painting as input,  and predicts an answer to the given question. Please refer to README in `iQAN` folder on how to run the code.

### External Knowledge Classifier

The external knowledge classifier will predict whether external knowledge is needed to answer a question given its corresponding painting. Please refer to README in `External Knowledge Classifier` folder on how to run the code.

### TF-IDF Comment Selection

If external knowledge classifier predicts that external knowledge is needed for a given question, then we will need to find the corresponding comment for the question. This module will predict top10 most possible comments for a given question. Please refer to README in `TF-IDF Comment Selection` folder on how to run the code.