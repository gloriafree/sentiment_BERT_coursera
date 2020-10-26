# calculate F1-score
F1-score is a function of both precision and recall, and so it seeks good balance between these two measures.
F1 = 2 * (precision * recall) / (precision + recall)

* precision ( TP/(TP + FP) ) is how many correct positive cases out of all predicted positive cases (or what patient cares from result perspective)
* recall ( TP/(TP + FN) ) is how many correct positive cases out of all actual positive cases (or what doctor cares from methodology perspective)

# multiple-class targets [scikit doc](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
none
micro
binary
macro
samples
weighted: weighted average by support/true instance number for each label
