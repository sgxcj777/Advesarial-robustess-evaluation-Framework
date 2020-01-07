import numpy as np
import keras
from keras import backend as K
import tensorflow as tf
from skimage.transform import resize
from art import metrics
from art.classifiers import KerasClassifier

class modelSurrogate:
    IMAGE_SIZE = 96
    BATCH_SIZE = 32

    def __init__(self, x_train, x_test, y_train, y_test,_min,_max):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test
        self.clip_values = (_min,_max)
        
        num_train = len(x_train)
        num_val = len(x_test)
        
        # preprocess data
        def process_data(x,y):
            def _parse_fn(img,label):
                image_normalized = (tf.cast(img, tf.float32)/127.5) - 1
                image_resized = tf.image.resize(image_normalized, (self.IMAGE_SIZE, self.IMAGE_SIZE))
                return image_resized,label
            preprocessed=tf.data.Dataset.from_tensor_slices(
                (tf.constant(x),tf.constant(y))).map(_parse_fn).shuffle(buffer_size=10000).batch(self.BATCH_SIZE)
            return preprocessed
        
        x_train = process_data(x_train, y_train)
        x_test = process_data(x_test, y_test)
        
        # Pre-trained model with MobileNetV2
        IMG_SHAPE = (self.IMAGE_SIZE, self.IMAGE_SIZE, 3)
        base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                       include_top=False, 
                                                       weights='imagenet')

        # Freeze the pre-trained model weights
        base_model.trainable = False

        # Trainable classification head  
        maxpool_layer = tf.keras.layers.GlobalMaxPooling2D()
        prediction_layer = tf.keras.layers.Dense(y_train.shape[1], activation='sigmoid')
        
        # Layer classification head with feature detector
        model = tf.keras.Sequential([
            base_model,
            maxpool_layer,
            prediction_layer
        ])
        learning_rate = 0.0001
        
        # Compile the model
        self.model = model.compile(optimizer=tf.keras.optimizers.Adam(lr=learning_rate), 
                    loss='binary_crossentropy',
                    metrics=['accuracy']
        )

        # training the model
        """
        num_epochs = 1
        steps_per_epoch = round(num_train)//self.BATCH_SIZE
        val_steps = 20
        model.fit(x_train.repeat(),
                            epochs=num_epochs,
                            steps_per_epoch = steps_per_epoch,
                            validation_data=x_test.repeat(), 
                            validation_steps=val_steps)
        """
        print(np.stack(list(x_train)))
        #classifier = KerasClassifier(model=model, clip_values=self.clip_values)
        #classifier.fit(x_train.repeat()[0], y_train, nb_epochs=1, batch_size=32)
        
    """    
    def get_weight_grad(self,inputs, outputs):
        
        def process_data(x,y):
            def _parse_fn(img,label):
                image_normalized = (tf.cast(img, tf.float32)/127.5) - 1
                image_resized = tf.image.resize(image_normalized, (self.IMAGE_SIZE, self.IMAGE_SIZE))
                return image_resized,label
            preprocessed=tf.data.Dataset.from_tensor_slices(
                (tf.constant(x),tf.constant(y))).map(_parse_fn).shuffle(buffer_size=10000).batch(self.BATCH_SIZE)
            return preprocessed
        
        grads = self.model.optimizer.get_gradients(self.model.total_loss, self.model.trainable_weights)
        symb_inputs = (self.model._feed_inputs + self.model._feed_targets + self.model._feed_sample_weights)
        f = K.function(symb_inputs, grads)
        processed_inputs = process_data(inputs, outputs)
        x, y, sample_weight = self.model._standardize_user_data(processed_inputs)
        output_grad = f(x + y + sample_weight)
        return x.numpy()
    
    def preprocess_raw(self,data):
        def _parse_fn(img):
            image_normalized = (tf.cast(img, tf.float32)/127.5) - 1
            image_resized = tf.image.resize(image_normalized, (self.IMAGE_SIZE, self.IMAGE_SIZE))
            return image_resized
        preprocessed=tf.data.Dataset.from_tensor_slices(
            (tf.constant(data))).map(_parse_fn).shuffle(buffer_size=10000).batch(self.BATCH_SIZE)
        return preprocessed
    
    def predict(self,img):
        preprocessed = self.preprocess_raw(img)
        return self.model.predict(preprocessed)
    
    """
    