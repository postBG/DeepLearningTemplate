# DeepLearningTemplate

This repository contains template for deep learning projects.

## Dependencies
To set up your python environment to run the code in this repository, follow the instructions below.

1. Create a new virtual environment with Python 3.6. If you use `virtualenvwrapper`, follow the instructions below.
```bash
$> mkvirtualenv body_parts_seg
$> workon body_parts_seg
```

2. Clone the repository and move to the folder.
```bash
$> git clone https://github.com/postBG/DeepLearningTemplate.git
$> cd BodyPartsSegmentation.pytorch
```

3. Install several dependencies using `requirements.txt`.
```bash
$> pip install -r requirements.txt
```

4. Run the code
```bash
$> python main.py --template=<Template Name>
```

## TODO
* Implement Yaml configs
