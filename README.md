# Adversarial-robustess-evaluation-Framework


## IBM ART
This library contains all the functions that is required for this framework. This includes a diverse set of adversarial attacks, defences, and metrics that we can use, much like a toolbox. More importantly, it is active and updated constantly by the IBM team and open community. Tools that ART provides currently:

## Supported Machine Learning Libraries and Applications
* TensorFlow (v1 and v2) (www.tensorflow.org)
* Keras (www.keras.io)
* PyTorch (www.pytorch.org)
* MXNet (https://mxnet.apache.org)
* Scikit-learn (www.scikit-learn.org)
* XGBoost (www.xgboost.ai)
* LightGBM (https://lightgbm.readthedocs.io)
* CatBoost (www.catboost.ai)
* GPy (https://sheffieldml.github.io/GPy/)
* Tesseract (https://github.com/tesseract-ocr/tesseract)

## Implemented Attacks, Defences, Detections, Metrics, Certifications and Verifications

**Evasion Attacks:**
* HopSkipJump attack ([Chen et al., 2019](https://arxiv.org/abs/1904.02144))
* High Confidence Low Uncertainty adversarial examples ([Grosse et al., 2018](https://arxiv.org/abs/1812.02606))
* Projected gradient descent ([Madry et al., 2017](https://arxiv.org/abs/1706.06083))
* NewtonFool ([Jang et al., 2017](http://doi.acm.org/10.1145/3134600.3134635))
* Elastic net attack ([Chen et al., 2017](https://arxiv.org/abs/1709.04114))
* Spatial transformations attack ([Engstrom et al., 2017](https://arxiv.org/abs/1712.02779))
* Query-efficient black-box attack ([Ilyas et al., 2017](https://arxiv.org/abs/1712.07113))
* Zeroth-order optimization attack ([Chen et al., 2017](https://arxiv.org/abs/1708.03999))
* Decision-based attack ([Brendel et al., 2018](https://arxiv.org/abs/1712.04248))
* Adversarial patch ([Brown et al., 2017](https://arxiv.org/abs/1712.09665))
* Decision tree attack ([Papernot et al., 2016](https://arxiv.org/abs/1605.07277))
* Carlini & Wagner (C&W) `L_2` and `L_inf` attacks ([Carlini and Wagner, 2016](https://arxiv.org/abs/1608.04644))
* Basic iterative method ([Kurakin et al., 2016](https://arxiv.org/abs/1607.02533))
* Jacobian saliency map ([Papernot et al., 2016](https://arxiv.org/abs/1511.07528))
* Universal perturbation ([Moosavi-Dezfooli et al., 2016](https://arxiv.org/abs/1610.08401))
* DeepFool ([Moosavi-Dezfooli et al., 2015](https://arxiv.org/abs/1511.04599))
* Virtual adversarial method ([Miyato et al., 2015](https://arxiv.org/abs/1507.00677))
* Fast gradient method ([Goodfellow et al., 2014](https://arxiv.org/abs/1412.6572))

**Poisoning Attacks:**
* Poisoning Attack on SVM ([Biggio et al., 2013](https://arxiv.org/abs/1206.6389))

**Defences:**
* Thermometer encoding ([Buckman et al., 2018](https://openreview.net/forum?id=S18Su--CW))
* Total variance minimization ([Guo et al., 2018](https://openreview.net/forum?id=SyJ7ClWCb))
* PixelDefend ([Song et al., 2017](https://arxiv.org/abs/1710.10766))
* Gaussian data augmentation ([Zantedeschi et al., 2017](https://arxiv.org/abs/1707.06728))
* Feature squeezing ([Xu et al., 2017](http://arxiv.org/abs/1704.01155))
* Spatial smoothing ([Xu et al., 2017](http://arxiv.org/abs/1704.01155))
* JPEG compression ([Dziugaite et al., 2016](https://arxiv.org/abs/1608.00853))
* Label smoothing ([Warde-Farley and Goodfellow, 2016](https://pdfs.semanticscholar.org/b5ec/486044c6218dd41b17d8bba502b32a12b91a.pdf))
* Virtual adversarial training ([Miyato et al., 2015](https://arxiv.org/abs/1507.00677))
* Adversarial training ([Szegedy et al., 2013](http://arxiv.org/abs/1312.6199))

**Robustness metrics, certifications and verifications**:
* Clique Method Robustness Verification ([Hongge et al., 2019](https://arxiv.org/abs/1906.03849))
* Randomized Smoothing ([Cohen et al., 2019](https://arxiv.org/abs/1902.02918))
* CLEVER ([Weng et al., 2018](https://arxiv.org/abs/1801.10578))
* Loss sensitivity ([Arpit et al., 2017](https://arxiv.org/abs/1706.05394))
* Empirical robustness ([Moosavi-Dezfooli et al., 2015](https://arxiv.org/abs/1511.04599))

**Detection of adversarial samples:**
* Basic detector based on inputs
* Detector trained on the activations of a specific layer
* Detector based on Fast Generalized Subset Scan ([Speakman et al., 2018](https://arxiv.org/pdf/1810.08676))

**Detectoion of poisoning attacks:**
* Detector based on activations analysis ([Chen et al., 2018](https://arxiv.org/abs/1811.03728))


More information about IBM ART library:
[Github](https://github.com/IBM/adversarial-robustness-toolbox)
[Documentation](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/index.html)

## Setup of IBM ART

### Installation with `pip`

The toolbox is designed and tested to run with Python 3. 
ART can be installed from the PyPi repository using `pip`:

```bash
pip install adversarial-robustness-toolbox
```

### Manual installation

The most recent version of ART can be downloaded or cloned from this repository:

```bash
git clone https://github.com/IBM/adversarial-robustness-toolbox
```

Install ART with the following command from the project folder `art`:
```bash
pip install .
```

ART provides unit tests that can be run with the following command:

```bash
bash run_tests.sh
```
## Citing ART

If you use ART for research, please consider citing the following reference paper:
```
@article{art2018,
    title = {Adversarial Robustness Toolbox v1.0.1},
    author = {Nicolae, Maria-Irina and Sinn, Mathieu and Tran, Minh~Ngoc and Buesser, Beat and Rawat, Ambrish and Wistuba, Martin and Zantedeschi, Valentina and Baracaldo, Nathalie and Chen, Bryant and Ludwig, Heiko and Molloy, Ian and Edwards, Ben},
    journal = {CoRR},
    volume = {1807.01069},
    year = {2018},
    url = {https://arxiv.org/pdf/1807.01069}
}
```
