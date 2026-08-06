# What is Code Splitting?

In order to increase the loading speed of the website, it is a method of dividing large code files into small pieces and loading them only when needed.

## Overview
When the user enters your site, instead of downloading all the codes, he downloads only the codes required for the page he is currently viewing. The codes of other pages are loaded in the background when the user clicks on those pages.

*Analogy: It's like being in a restaurant where the plates come one by one as you order, instead of having all the dishes on the menu brought to the table at the same time.*

## How it works
The developer makes marks in the code such as 'load this part now, load the rest later'.

## Where it is used
It is used in large-scale web applications and sites that care about user experience.

## Commonly confused with
Can be confused with bundling; bundling dosyaları birleştirirken, code splitting bunları akıllıca parçalara ayırır.

## Frequently asked questions
**Will there be a delay when the user clicks on the page?**
It may be a very small time but the overall experience is better as the initial loading speed is much faster.


## Related terms
- [Bundler](/en/dictionary/bundler/)
- [Frontend Stack](/en/dictionary/frontend-stack/)

## Related tools
- [Webpack](/en/discover/webpack/)

---
Source: TreScout Dictionary · https://trescout.com/en/dictionary/code-splitting/
