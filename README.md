- Commands ud in the  DVC tutorial

``` bash
conda create -n basic_dvc_demo python=3.11.5 -y

conda init bash

conda activate basic_dvc_demo

pip install dvc

touch stage_01.py stage_02.py

git init

dvc init

touch dvc.yaml

dvc repro

git add . && git commit -m "git commands in one line" && git push origin main
```




