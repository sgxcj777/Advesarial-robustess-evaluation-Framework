# Evaluating CLEVER metric in Black box environment

## Surrogate model
A surrogate model is required to obatin gradients from model that is evaluated in black box environment
[Prior-based RBF](https://papers.nips.cc/paper/9275-improving-black-box-adversarial-attacks-with-a-transfer-based-prior.pdf) is used to create a surrogate model. The surrogate model is then used in a white box environment to compute CLEVER score.



## Required packages

- Tensorflow 2.0 (note that eager evaluation needs to be disabled as ART library does not support this feature yet)


