from training_and_baseline import random_output, load_models

vectorizer, model = load_models()

print(random_output("I love donald trump", vectorizer, model))
