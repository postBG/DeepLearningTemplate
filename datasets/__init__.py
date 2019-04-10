import numpy as np

from torch.utils.data import DataLoader, Subset
from datasets.bases import AbstractBaseDataSet


def get_transforms(transform_type):
    transformations = {
        'none': None,
        'none_val': None,
    }
    return transformations[transform_type]


def dataset_factory(code, transform_type, is_train=True):
    dataset_cls = AbstractBaseDataSet.get_class_of_dataset(code)
    transform = get_transforms(transform_type)
    return dataset_cls(transform=transform, is_train=is_train)


def dataloaders_factory(args):
    train_dataset = dataset_factory(args.train_transform_type, is_train=True)
    val_dataset = dataset_factory(args.val_transform_type, is_train=False)

    if args.test:
        train_dataset = Subset(train_dataset, np.random.randint(0, len(train_dataset), args.batch_size * 5))
        val_dataset = Subset(val_dataset, np.random.randint(0, len(val_dataset), args.batch_size * 5))

    train_dataloader = DataLoader(train_dataset, batch_size=args.batch_size, num_workers=32, shuffle=True,
                                  pin_memory=True)
    val_dataloader = DataLoader(val_dataset, batch_size=args.batch_size, num_workers=16, shuffle=False, pin_memory=True)

    return {
        'train': train_dataloader,
        'val': val_dataloader,
    }
