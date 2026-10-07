# What is BLAS?

> Basic Linear Algebra Subprograms

They are standard library rules that enable computers to perform fundamental linear algebra operations, such as matrices and vectors, at maximum speed.

## Overview
BLAS is a standard application programming interface that forms the basis of mathematical computations in computer science. It optimizes, at the processor level, the massive matrix multiplications running in the background, especially during the training and execution of artificial intelligence models. Hardware manufacturers develop custom BLAS libraries for their own processors to ensure these calculations are completed within milliseconds.

*Analogy: In a very large construction project, it is similar to using a special transport robot that arranges bricks at maximum speed and with minimal energy instead of carrying them manually one by one.*

## How it works
Instead of writing BLAS codes directly, you include libraries that use these standards in your projects. Your processor processes the incoming mathematical commands in parallel, in the way most suited to its architecture, and utilizes memory most efficiently.

## Where it is used
It runs silently in the background in artificial intelligence libraries, scientific simulation tools, 3D graphics engines, and data analysis software.

## Commonly confused with
It is confused with an ordinary math library. BLAS does not just contain mathematical formulas; it directly manages how these formulas are executed on computer hardware with the highest performance.

## Frequently asked questions
**Why is BLAS so important for artificial intelligence?**
Because modern artificial intelligence and data analytics rely on billions of matrix multiplications. Without BLAS, these operations would take much longer using standard processor instructions.

**Is BLAS written directly by developers?**
It is generally not written directly. As developers, when you use high-level artificial intelligence libraries in Python or similar languages, this system runs automatically in the background.


## Related terms
- [GPU](/en/dictionary/gpu/)
- [CPU](/en/dictionary/cpu/)
- [Array Operations](/en/dictionary/array-operations/)
- [Neural Networks](/en/dictionary/neural-networks/)

## Related tools
- [DeepGEMM](/en/discover/deepgemm/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/blas/
