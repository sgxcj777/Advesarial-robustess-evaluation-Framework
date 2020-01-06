# Resistance against basic and sophisticated adversarial attacks
This level evaluates model's robustness based on a set of basic and sophisticated common adversarial attacks. IBM's ART library is used as a toolkit to conduct attacks and evaluation. More information about IBM ART library can be found in the README.

## Level 2: Test for resistance against basic adversarial attacks
- Basic adversarial attacks are categorized according to if they are gradient based (i.e. attack models based on gradient direction)
- Suggested attacks:
  1. Fast Gradient Sign method (FGSM) --> Very common and simple adversarial attack method. This is performed to evaluate if 
     the model to be tested contains any defence system in place to start with.
     Theory: ([Goodfellow et al., 2014](https://arxiv.org/abs/1412.6572))
  2. DeepFool --> more advanced adversarial attack method that is gradient based. Used to test for more advanced but basic 
     adversarial attacks.
     Theory: ([Moosavi-Dezfooli et al., 2015](https://arxiv.org/abs/1511.04599))
- Example includes DeepFool for whitebox and blackbox (using surrogate model) environment. also include FGSM for whitebox environment to compare accuracy to show that DeepFool is more advanced than FGSM as it DeepFool reduces model accuracy by a larger percentage (dropped to 2.57%) compared to FGSM (dropped to 21.78%).

## Level 3: Test for resistance against sophisticated adversarial attacks
- Sophisticated adversarial attacks are categorized according to non-gradient based attacks (e.g. decision based)
- Suggested attacks:
  1. Boundary attack --> Non gradient dependent on model, based on changing decision boundaries of model. Note that this 
     attack only requires model's predicted ouput.
     theory: [Wieland Brendel and Jonas Rauber and Matthias Bethge, 2017](https://arxiv.org/abs/1712.04248)
- Example includes Boundary Attack which is black box by nature (only need model's predicted output) and thus do not need white box environment. 

## Further testing
Although the above are a set of selected adversarial attacks, there can be addition of new attack types, as long as the adversarial attack fulfils the criteria of each level.
