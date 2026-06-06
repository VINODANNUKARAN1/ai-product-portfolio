
import json

with open("../dataset/evaluation_dataset.json") as f:
    data = json.load(f)

scores = [item["score"] for item in data]

print("Evaluation Results")
print("-------------------")
print("Average Accuracy:", sum(scores) / len(scores))
