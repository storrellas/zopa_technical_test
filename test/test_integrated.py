import unittest

from loan_calculator import LoanCalculator
import main

class TestLoanCalculator(unittest.TestCase):

    def test_Given_Principal_When_Calculate_repayment_Then_Operation_ok(self):
        pair = \
            main.calculate_figures( 1000, "resources/market_data.csv")
        loan_calculator = pair[1]
        self.assertTrue(loan_calculator.get_repayment() > 0)
        self.assertTrue(loan_calculator.get_interest()*100 > 0)


    def test_Given_NonExisting_file_When_Calculate_repayment_Then_Operation_fails(self):
        pair = \
            main.calculate_figures( 1000, "not_found_data.csv")
        self.assertFalse(pair[0])

    def test_Given_Wrong_file_When_Calculate_repayment_Then_Operation_fails(self):
        pair = \
            main.calculate_figures( 1000, "resources/wrong_data.csv")
        self.assertFalse(pair[0])

if __name__ == '__main__':
    unittest.main()