# Resistance against basic and sophisticated adversarial attacks
This level evaluates model's robustness based on a set of basic and sophisticated common adversarial attacks. IBM's ART library is used as a toolkit to conduct attacks and evaluation. More information about IBM ART library can be found in the README.

## Level 2: Test for resistance against basic adversarial attacks
- Basic adversarial attacks are categorized according to if they are gradient based (i.e. attack models based on gradient direction)
- Suggested attacks:
  1. Fast Gradient Sign method (FGSM) --> Very common and simple adversarial attack method. This is performed to evaluate if 
     the model to be tested contains any defence system in place to start with.
  2. DeepFool --> more advanced adversarial attack method that is gradient based. Used to test for more advanced but basic 
     adversarial attacks.
- Example includes DeepFool for whitebox and blackbox (using surrogate model) environment. also include FGSM for whitebox environment to compare accuracy to show that DeepFool is more advanced than FGSM as it DeepFool reduces model accuracy by a larger percentage (dropped to 2.57%) compared to FGSM (dropped to 21.78%).

## Level 3: Test for resistance against sophisticated adversarial attacks
- Sophisticated adversarial attacks are categorized according to non-gradient based attacks (e.g. decision based)
- Suggested attacks:
  1. Boundary attack --> 
