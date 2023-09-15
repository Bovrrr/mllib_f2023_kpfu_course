import numpy as np
from abc import ABC, abstractmethod


class BaseDataset(ABC):

    def __init__(self,train_set_percent,valid_set_percent):
        # TODO
        # добавить ассерты на положительность
        # проверку на сумму между 0 и 1
        self.train_set_percent = train_set_percent
        self.valid_set_percent = valid_set_percent

    @property
    @abstractmethod
    def targets(self):
        # targets variables
        pass

    @property
    @abstractmethod
    def inputs(self):
        # inputs variables
        pass

    def _divide_data(self, collection_a, collection_b):
        # проверяю равенство длин
        assert len(collection_a) == len(collection_b), f"длина колелкций различается"

        n = len(collection_a)
        idxs = np.arange(n)
        np.random.shuffle(idxs)

        return collection_a[idxs], collection_b[idxs]


    def _divide_into_sets(self):
        # TODO define self.inputs_train, self.targets_train, self.inputs_valid, self.targets_valid,
        #  self.inputs_test, self.targets_test
        
        # шафлим исходные выборки
        n = len(self.inputs)
        idxs = np.arange(n)
        np.random.shuffle(idxs)

        self.inputs = self.inputs[idxs]
        self.targets = self.targets[idxs]

        n_train_right = int(n * self.train_set_percent)
        n_val_right = int(n * (self.train_set_percent + self.val_set_percent))

        self.inputs_train, self.targets_train = self.inputs[:n_train_right], self.targets[:n_train_right]
        self.inputs_valid, self.targets_valid = self.inputs[n_train_right: n_val_right], self.targets[n_train_right:n_val_right]
        self.inputs_test, self.targets_test = self.inputs[n_val_right:], self.targets[n_val_right:]

