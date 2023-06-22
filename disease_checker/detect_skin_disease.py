import tensorflow as tf
import cv2
import numpy as np
disease = ['akiec',
           'bcc',
           'bkl',
           'df',
            'mel',
           'nv',
           'vasc']
dic = {
            'mel':['Melanoma',""" Melanoma is the most serious type of skin cancer, develops in the cells (melanocytes) that produce melanin — the pigment that gives your skin its color. Melanoma can also form in your eyes and, rarely, inside your body, such as in your nose or throat."""],
            'vasc':['Vascular Lesions',"""Vascular lesions are relatively common abnormalities of the skin and underlying tissues, more commonly known as birthmarks."""],
            'df':['Dermatofibroma',"""Dermatofibroma is a commonly occurring cutaneous entity usually centered within the skin's dermis. Dermatofibromas are referred to as benign fibrous histiocytomas of the skin, superficial/cutaneous benign fibrous histiocytomas, or common fibrous histiocytoma."""],
            'nv':['Melanocytic Nevi',"""melanocytic nevus is a skin condition characterized by an abnormally dark, noncancerous skin patch (nevus) that is composed of pigment-producing cells called melanocytes. It is present from birth (congenital) or is noticeable soon after birth."""],
            'bkl':['Solar Lentigines',"""Solar lentigo is a harmless patch of darkened skin. It results from exposure to ultraviolet (UV) radiation, which causes local proliferation of melanocytes and accumulation of melanin within the skin cells (keratinocytes). Solar lentigos or lentigines are very common, especially in people over the age of 40 years."""],
            'akiec':["Bowen's disease","""Bowen's disease is a very early form of skin cancer that's easily treatable. The main sign is a red, scaly patch on the skin. It affects the squamous cells, which are in the outermost layer of skin, and is sometimes referred to as squamous cell carcinoma in situ."""],
            'bcc':['Basal Cell Carcinoma',"""Basal cell carcinoma is a type of skin cancer that most often develops on areas of skin exposed to the sun, such as the face. On brown and Black skin, basal cell carcinoma often looks like a bump that's brown or glossy black and has a rolled border."""]
}


def detect_skin_disease_(img):
    model = tf.keras.models.load_model('disease_checker/Models/HM_skin_disease.h5')
    img = cv2.imread("./"+img)
    img = cv2.resize(img, (128, 128))
    img_ = np.expand_dims(img, axis=0)
    print(img_.shape)
    acc = model.predict(img_)
    print(np.argmax(acc))
    return dic[disease[np.argmax(acc)]]
