import os
import random
import shutil


def make_dir(PATH):
    if not os.path.exists(PATH):
        os.mkdir(PATH)
        return PATH
    else:
        shutil.rmtree(PATH)
        os.mkdir(PATH)
        return PATH


def split_data(SOURCE="", TRAINING="", VALIDATION="", SPLIT_SIZE=0):
    data = os.listdir(SOURCE)
    random_data = random.sample(data, len(data))

    train_size = len(data) * SPLIT_SIZE

    for i, filename in enumerate(random_data):
        filepath = os.path.join(SOURCE, filename)
        if os.path.getsize(filepath) > 0:
            if i < train_size:
                shutil.copyfile(filepath, os.path.join(TRAINING, filename))
            else:
                shutil.copyfile(filepath, os.path.join(VALIDATION, filename))
    print(f"{SOURCE} splitted!")


base_dir = make_dir("dataset")
train_dir = make_dir(os.path.join(base_dir, "train"))
validation_dir = make_dir(os.path.join(base_dir, "val"))
test_dir = make_dir(os.path.join(base_dir, "test"))

fresh_train_dir = make_dir(os.path.join(train_dir, "fresh"))
rotten_train_dir = make_dir(os.path.join(train_dir, "rotten"))

fresh_val_dir = make_dir(os.path.join(validation_dir, "fresh"))
rotten_val_dir = make_dir(os.path.join(validation_dir, "rotten"))

fresh_test_dir = make_dir(os.path.join(test_dir, "fresh"))
rotten_test_dir = make_dir(os.path.join(test_dir, "rotten"))

print("ftrain images - ", len(os.listdir(fresh_train_dir)))
print("fval images - ", len(os.listdir(fresh_val_dir)))
print("ftest images - ", len(os.listdir(fresh_test_dir)))
print("\n")
print("rtrain images - ", len(os.listdir(rotten_train_dir)))
print("rval images - ", len(os.listdir(rotten_val_dir)))
print("rtest images - ", len(os.listdir(rotten_test_dir)))
print("\n\n")

dataset_train_dir = os.path.join("temp", os.path.join("dataset", "train"))
dataset_test_dir = os.path.join("temp", os.path.join("dataset", "test"))

fapples_train_dir = os.path.join(dataset_train_dir, "freshapples")
fbananas_train_dir = os.path.join(dataset_train_dir, "freshbanana")
foranges_train_dir = os.path.join(dataset_train_dir, "freshoranges")
rapples_train_dir = os.path.join(dataset_train_dir, "rottenapples")
rbananas_train_dir = os.path.join(dataset_train_dir, "rottenbanana")
roranges_train_dir = os.path.join(dataset_train_dir, "rottenoranges")

fapples_test_dir = os.path.join(dataset_test_dir, "freshapples")
fbananas_test_dir = os.path.join(dataset_test_dir, "freshbanana")
foranges_test_dir = os.path.join(dataset_test_dir, "freshoranges")
rapples_test_dir = os.path.join(dataset_test_dir, "rottenapples")
rbananas_test_dir = os.path.join(dataset_test_dir, "rottenbanana")
roranges_test_dir = os.path.join(dataset_test_dir, "rottenoranges")

print("fresh apple train images - ", len(os.listdir(fapples_train_dir)))
print("fresh banana train images - ", len(os.listdir(fbananas_train_dir)))
print("fresh orange train images - ", len(os.listdir(foranges_train_dir)))
print("rotten apple train images - ", len(os.listdir(rapples_train_dir)))
print("rotten banana train images - ", len(os.listdir(rbananas_train_dir)))
print("rotten orange train images - ", len(os.listdir(roranges_train_dir)))
print("\n")
print("fresh apple test images - ", len(os.listdir(fapples_test_dir)))
print("fresh banana test images - ", len(os.listdir(fbananas_test_dir)))
print("fresh orange test images - ", len(os.listdir(foranges_test_dir)))
print("rotten apple test images - ", len(os.listdir(rapples_test_dir)))
print("rotten banana test images - ", len(os.listdir(rbananas_test_dir)))
print("rotten orange test images - ", len(os.listdir(roranges_test_dir)))
print("\n\n")

SPLIT_SIZE = 0.7
split_data(fapples_train_dir, fresh_train_dir, fresh_val_dir, SPLIT_SIZE)
split_data(fbananas_train_dir, fresh_train_dir, fresh_val_dir, SPLIT_SIZE)
split_data(foranges_train_dir, fresh_train_dir, fresh_val_dir, SPLIT_SIZE)
split_data(rapples_train_dir, rotten_train_dir, rotten_val_dir, SPLIT_SIZE)
split_data(rbananas_train_dir, rotten_train_dir, rotten_val_dir, SPLIT_SIZE)
split_data(roranges_train_dir, rotten_train_dir, rotten_val_dir, SPLIT_SIZE)

SPLIT_SIZE = 1.0
split_data(fapples_test_dir, fresh_test_dir, fresh_val_dir, SPLIT_SIZE)
split_data(fbananas_test_dir, fresh_test_dir, fresh_val_dir, SPLIT_SIZE)
split_data(foranges_test_dir, fresh_test_dir, fresh_val_dir, SPLIT_SIZE)
split_data(rapples_test_dir, rotten_test_dir, rotten_val_dir, SPLIT_SIZE)
split_data(rbananas_test_dir, rotten_test_dir, rotten_val_dir, SPLIT_SIZE)
split_data(roranges_test_dir, rotten_test_dir, rotten_val_dir, SPLIT_SIZE)

print("\n\n")
print("ftrain images - ", len(os.listdir(fresh_train_dir)))
print("fval images - ", len(os.listdir(fresh_val_dir)))
print("ftest images - ", len(os.listdir(fresh_test_dir)))
print("\n")
print("rtrain images - ", len(os.listdir(rotten_train_dir)))
print("rval images - ", len(os.listdir(rotten_val_dir)))
print("rtest images - ", len(os.listdir(rotten_test_dir)))
