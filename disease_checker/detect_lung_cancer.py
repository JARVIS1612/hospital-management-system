import tensorflow as tf
import cv2
import numpy as np
cancer = ['large_cell', 'adenocarcinoma', 'squamous_cell', 'normal']
dic_cancer = {
    'large_cell': ["Large cell carcinoma", """ Large-cell undifferentiated carcinoma: Large-cell undifferentiated carcinoma lung cancer 
                            grows and spreads quickly and can be found anywhere in the lung. This type of lung cancer 
                            usually accounts for 10 to 15 percent of all cases of NSCLC.
                            Large-cell undifferentiated carcinoma tends to grow and spread quickly."""],

    'adenocarcinoma': ["Adenocarcinoma", """ Lung adenocarcinoma is the most common form of lung cancer
                                            accounting for 30 percent of all cases overall and about 40 percent of all non-small cell 
                                            lung cancer occurrences.Adenocarcinomas are found in several common cancers, including breast,
                                            prostate and colorectal. Adenocarcinomas of the lung are found in the outer region of the 
                                            lung in glands that secrete mucus and help us breathe. Symptoms include coughing, 
                                            hoarseness, weight loss and weakness."""],
    'squamous_cell': ["Squamous cell carcinoma", """ Squamous cell: This type of lung cancer is found centrally in the lung,
                                                where the larger bronchi join the trachea to the lung,
                                                or in one of the main airway branches.
                                                Squamous cell lung cancer is responsible for about 30 percent of all non-small
                                                cell lung cancers, and is generally linked to smoking."""],
    'normal': ["No Cancer Detected", """ If you don't satisfied with this test. Cansult our doctors"""],
}


def detect_lung_cancer_(img):
    model = tf.keras.models.load_model('disease_checker/Models/HM_lung_cancer.h5')
    img = cv2.imread("./"+img)
    img = cv2.resize(img, (180, 180))
    img_ = np.expand_dims(img, axis=0)
    print(img_.shape)
    acc = model.predict(img_)
    print(np.argmax(acc))
    return dic_cancer[cancer[np.argmax(acc)]]
