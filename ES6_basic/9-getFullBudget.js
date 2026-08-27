import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    // eslint-disable-next-line no-shadow, space-in-parens
    getIncomeInDollars: ( income ) => `$${income}`,
    // eslint-disable-next-line no-shadow, space-in-parens
    getIncomeInEuros: ( income ) => `${income} euros`,
  };

  return fullBudget;
}
