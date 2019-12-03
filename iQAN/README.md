# iQAN

iQAN is the VQA model we use in our pipeline to answer visual-related question. It takes the question which  external knowledge classifier predicts that no external knowledge is needed as well as the painting as input,  and predicts an answer to the given question.

### Prepare Training, Validation and Test Set

In order to train and evaluate the performance of the model, first prepare the training, valiadation and test. Copy training and validation set from `../Dataset` to the target folder.

```bash
cp ../Dataset/train.json ./data/SemArt/extract/arch,resnet152_size,448/
cp ../Dataset/val.json ./data/SemArt/extract/arch,resnet152_size,448/
```

The test set is those questions which external knowledge classifier predicts that no external knowledge is needed. The classifier will generate `not_need_external_knowledge.json` and `need_external_knowledge.json`. Please refer to `../External Knowledge Classifier` on how to generate these two files. `not_need_external_knowledge.json` is the test set for this module.

```bash
cp ../External\ Knowledge\ Classifier/not_need_external_knowledge.json ./data/SemArt/extract/arch,resnet152_size,448/
```

### Prepare Features for Painings

We use pretrained ResNet to extract feature for each painting. In order to train and validate the model, the extracted features are needed as well. The features and the index of the paintings can be downloaded here

```
wget https://semart.s3.amazonaws.com/all.hdf5 -P ./data/SemArt/extract/arch,resnet152_size,448/
```

```
wget https://semart.s3.amazonaws.com/all.txt -P ./data/SemArt/extract/arch,resnet152_size,448/
```

The `hdf5` file is about 30GB and may take some time to download.

### Run the model

Once all the preparation work is done, we can then train and test the model.

Train the model:

```bash
CUDA_VISIBLE_DEVICES=0 python train_dual_model.py --path_opt options/dual_model/dual_model_MUTAN_skipthought.yaml --dir_logs logs/dual_model/iQAN_Mutan_skipthought_dual_training/ --share_embeddings -b 8
```

Test the model:

```bash
CUDA_VISIBLE_DEVICES=0 python train_dual_model.py --path_opt options/dual_model/dual_model_MUTAN_skipthought.yaml --dir_logs logs/dual_model/iQAN_Mutan_skipthought_dual_training/ --resume best -e --share_embeddings -b 8
```

The model will load a checkpoint which has best validation performance and do the predicion on test set. The prediction result can be seen in `logs/dual_model/iQAN_Mutan_skipthought_dual_training/evaluate`.
