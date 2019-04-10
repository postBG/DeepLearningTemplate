from datasets.bases import AbstractBaseDataSet

DEFAULT_ROOT = None


class TrivagoDataSet(AbstractBaseDataSet):
    def __init__(self, root=DEFAULT_ROOT, transform=None, is_train=False):
        pass

    def __len__(self):
        pass

    def __getitem__(self, idx):
        pass

    @classmethod
    def code(cls):
        return 'trivago'
