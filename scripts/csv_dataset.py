from pathlib import Path
import pandas as pd
import tensorflow as tf

AUTOTUNE = tf.data.AUTOTUNE

def decode_img(path, image_size=(224, 224), training=False):
    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)

    if training:
        img = tf.image.resize(img, [256, 256])
        img = tf.image.random_crop(img, [image_size[0], image_size[1], 3])
        img = tf.image.random_flip_left_right(img)
    else:
        img = tf.image.resize(img, image_size)

    return img

def make_regression_dataset(csv_path, target_col, image_size=(224, 224), batch_size=32, training=False, shuffle=True):
    df = pd.read_csv(csv_path)

    paths = df["image_path"].astype(str).tolist()
    targets = df[target_col].astype("float32").tolist()

    ds = tf.data.Dataset.from_tensor_slices((paths, targets))

    if training and shuffle:
        ds = ds.shuffle(min(len(df), 10000), reshuffle_each_iteration=True)

    def _map_fn(path, target):
        img = decode_img(path, image_size=image_size, training=training)
        return img, target

    ds = ds.map(_map_fn, num_parallel_calls=AUTOTUNE)
    ds = ds.batch(batch_size).prefetch(AUTOTUNE)
    return ds
