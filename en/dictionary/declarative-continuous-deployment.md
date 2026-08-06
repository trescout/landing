# What is Declarative Continuous Deployment?

It is the method that defines the final state of the system and ensures that updates automatically reach this goal.

## Overview
You are not interested in how to update the system, but what the result should be. You just say 'let the system be in this state' and the tools will take all the necessary steps to capture this state. This prevents erroneous manual updates.

*Analogy: It's like saying 'bring me a pizza' at a restaurant instead of 'cook me these ingredients in this order'; You are interested in what the result will be, not how it will occur.*

## How it works
You prepare a configuration file. The automatic system reads this file, compares it with the current situation and makes the necessary adjustments to close the gap.

## Where it is used
It is used in cloud-based applications and large-scale server management.

## Commonly confused with
It can be confused with imperative (command-oriented) methods; In that method, you tell each step one by one.

## Frequently asked questions
**Why should we choose this method?**
It minimizes human error and ensures that the system always remains in the desired state.

**What happens if I make a mistake?**
The system realizes that you have defined the wrong state and usually reverts back to the old, working state.


## Related terms
- [Cloud Native](/en/dictionary/cloud-native/)
- [Deployment](/en/dictionary/deployment/)

## Related tools
- [Argo Cd](/en/discover/argo-cd/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/declarative-continuous-deployment/
