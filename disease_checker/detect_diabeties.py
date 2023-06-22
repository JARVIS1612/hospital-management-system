import pickle
import numpy as np

# age0 gender1 polyuria2 polydipsia3 sudden_weight_loss4 weakness5 polyphagia6
# genital_thrush7 visual_blurring8 Itching9
# delayed_healing10 partial_paresis11 muscle_paresis12 muscle_stiffness13
# Alopecia14 Obesity15-16

file = open('disease_checker/Models/HM_Diabetes.plk', 'rb')
clf = pickle.load(file)


def detect_diabeties_(lis):
    data = np.array(lis)
    data = data.reshape(1, -1)
    return clf.predict(data)[0]
