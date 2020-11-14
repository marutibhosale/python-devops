"""
author -Maruti Bhosale
date -14-11-2020
time -21:50
package -logical_programs
Statement -Get distinct random coupon number

"""

import random


class CouponNumbers:

    def inputNumberOfCoupons(self):
        try:
            numberOfCoupons = int(input("Enter number of distinct coupons"))
        except ValueError as e:
            print(e)
            self.inputNumberOfCoupons()
        return numberOfCoupons

    @staticmethod
    def distinctCoupons(totalCoupons):
        distinctNumbers = []
        while len(distinctNumbers) <= totalCoupons:
            rand = random.randint(1, totalCoupons)
            if rand not in distinctNumbers:
                distinctNumbers.append(rand)
        return distinctNumbers


if __name__ == "__main__":
    couponNumbers = CouponNumbers()
    numbersOfCoupons = couponNumbers.inputNumberOfCoupons()
    allDistinctCoupons = couponNumbers.distinctCoupons(numbersOfCoupons)
    print("All Distinct coupons are: ", allDistinctCoupons)
