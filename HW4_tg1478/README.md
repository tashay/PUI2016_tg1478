# PUI 2016 HW 4.

## Assignment 1: Review of a classmate's Citibike project proposal

To complete this assignment, I reviewed Zhaohong Niu (zn352)'s Citibike project proposal.

I forked Zhaohong's repository that contained the Citibike proposal and completed the following tasks:

- Verified that her Null and Alternative hypotheses were formulated correctly

- Verified that the data supported the project: i.e. whether the data had the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values 

- Chose an appropriate test to test H0 given the type of data, and the question asked. 

- Wrote my comments, suggestions, and suggested statistical test, in a markdown named CitiBikeReview_tg1478.md.

- Submitted a pull request to the original repository.

CitiBikeReview_tg1478.md can be found here: (https://github.com/tashay/PUI2016_zn352/blob/master/CitiBikeReview_tg1478.md).


## Assignment 2: Literature choices of statistical tests

For this assignment I worked with Francis Ko and Anastasia Shegay to find scientific journals and identify information about the statistical anaylses performed. 
  
| Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper | 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Path Analysis	| 1, Whether a household had experienced maternal death | dichotomous | 2, Annual Income and Expenditure per Capita in the Household| continuous | 1, maternal age | continuous (could also be categoridcal) | Does maternal death impact household economic status after the event? | Maternal death either increases or does not change annual income and expenditure per capita | 0.041,0.001 | [Impact of Maternal Death on Household Economy in Rural China: A Prospective Path Analysis](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134756) |
*t*-test	| 3, Gender, age, educational level | dichotomous, categorical | 1, Cognitive score| continuous | 1, Normal cognitive ability | continuous | 	Do the cognitive functions of the healthy elderly change over time? | Cognitive function in the healthy elderly declines over time | 0.05 | [Does Cognitive Function Increase over Time in the Healthy Elderly?](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078646) |

## Assignment 3: Reproduce the analysis of the 'Hard to Employ' program in NY

For this assignment I worked with Jordan Vani to reproduce the analysis of the 'Hard to Employ' program in NY. To reproduce the analysis we completed the following tasks: 

- Formulated Null and Alternative Hypotheses and established a significance level of 0.05.
- Performed Z-test on the data, which resulted in us accepting the Null Hypothesis. 
- Performed chi-square test on the data, which resulted in us accepting the Null Hypothesis. 

## Assignment 4: Tests of correlation using the scipy package

The purpose of this assignment was to use a subset of CitiBike trip data to determine whether the distribution of male and female riders were the same. 

I performed the following tests on the data: 
- Pearson's Test
- Spearman's Test
- K-S Test
