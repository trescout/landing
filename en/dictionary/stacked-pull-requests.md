# What is Stacked Pull Requests?

It is a method of introducing major software changes into the system sequentially in small, manageable pieces that are interconnected.

## Overview
When developing software, instead of submitting a huge change all at once, you divide this change into logical parts and submit them one after the other. Each piece builds on the previous one. In this way, people reviewing your code can approve small and focused steps more quickly, instead of trying to understand a complex structure all at once.

*Analogy: It is like moving forward by sending each chapter to the editor as it is finished and getting approval, instead of writing a book all at once and sending it to the editor. This way, if you make a mistake, you only need to correct that section, not the entire book.*

## How it works
Break your changes into logical blocks. Submit the first block and start building the next one on top of it before it gets approved. This process ensures that the code remains cleaner and errors are detected earlier.

## Where it is used
It is used in internal team code review processes on platforms like GitHub or GitLab, especially when developing large features.

## Commonly confused with
It can be confused with a single large 'Pull Request'; however, this method offers a fragmented and sequential approach.

## Frequently asked questions
**Why don't we send it all at once?**
Large changes are more prone to errors and make it harder for others to review the code.

**If everything is connected, what happens if one part breaks?**
Since it is sequential, you need to manage your changes carefully to avoid breaking the chain.


## Related terms
- [Code Review](/en/dictionary/code-review/)
- [Git Push](/en/dictionary/git-push/)
- [Checkout](/en/dictionary/checkout/)

## Related tools
- [Gh Stack](/en/discover/gh-stack/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/stacked-pull-requests/
