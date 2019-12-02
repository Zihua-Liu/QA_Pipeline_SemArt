import numpy as np
import json
import os
from sklearn.linear_model import LogisticRegression
import pickle

def train():
	train_features = np.load("Cache Data/train.npy")
	labels = []
	with open("../Dataset/train.json") as f:
		dataset = json.load(f)
	for item in dataset:
		if item["need_external_knowledge"]:
			labels.append(1.0)
		else:
			labels.append(0.0)
	labels = np.array(labels)
	classifier = LogisticRegression().fit(train_features, labels)
	return classifier

def validation(classifier):
	test_features = np.load("Cache Data/val.npy")
	labels = []
	with open("../Dataset/val.json") as f:
		dataset = json.load(f)
	for item in dataset:
		if item["need_external_knowledge"]:
			labels.append(1.0)
		else:
			labels.append(0.0)
	labels = np.array(labels)
	acc = classifier.score(test_features, labels)
	predict = classifier.predict(test_features)
	from sklearn.metrics import confusion_matrix
	print(confusion_matrix(labels, predict))
	print("Validation Accuracy: {}".format(acc))

def predict(classifier):
	test_features = np.load("Cache Data/test.npy")
	labels = classifier.predict(test_features)
	with open("../Dataset/test.json") as f:
		dataset = json.load(f)

	need_external_knowledge = []
	not_need_external_knowledge = []
	for i, item in enumerate(dataset):
		if labels[i] == 0.0:
			item["need_external_knowledge_predict"] = False
			not_need_external_knowledge.append(item)
		else:
			item["need_external_knowledge_predict"] = True
			need_external_knowledge.append(item)
	with open("need_external_knowledge.json", "w") as f:
		json.dump(need_external_knowledge, f, indent = 4)
	with open("not_need_external_knowledge.json", "w") as f:
		json.dump(not_need_external_knowledge, f, indent = 4)

if __name__ == "__main__":
	filename = 'model_save.pkl'

	classifier = train()
	pickle.dump(classifier, open(filename, 'wb'))

	classifier = pickle.load(open(filename, 'rb'))
	validation(classifier)

	predict(classifier)
