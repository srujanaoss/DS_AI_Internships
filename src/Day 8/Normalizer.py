import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))

print("Original Scores:")
print(scores)

subject_mean = np.mean(scores, axis=0)

print("\nSubject-wise Mean:")
print(subject_mean)

centered_scores = scores - subject_mean

print("\nCentered Scores (After Mean Subtraction):")
print(centered_scores)


