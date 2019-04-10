from abc import ABCMeta, abstractmethod

from torch.utils.data import Dataset


class AbstractBaseDataSet(Dataset, metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def code(cls):
        raise NotImplementedError

    @classmethod
    def get_class_of_dataset(cls, code):
        for sub_cls in cls.__subclasses__():
            if sub_cls.code() == code:
                return sub_cls

        raise ValueError("DataSet Code {} is not supported.".format(code))
