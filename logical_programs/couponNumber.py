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
        """
         taking input from user for number of coupons
        :return:
        """
        while True:
            try:
                numberOfCoupons = int(input("Enter number of distinct coupons: "))
                if numberOfCoupons < 1:
                    print("number of coupons should be positive integer")
                    continue
                break
            except Exception as e:
                print(e)
        return numberOfCoupons

    def distinctCoupons(self, totalCoupons):
        """
         finding distinct coupons from random numbers
        :param totalCoupons:count of coupons which want to distinct
        :return: return all distinct coupon numbers
        """
        distinctNumbers = []
        while len(distinctNumbers) < totalCoupons:
            rand = random.randint(1, totalCoupons)
            if rand not in distinctNumbers:
                distinctNumbers.append(rand)
        return distinctNumbers


if __name__ == "__main__":
    couponNumbers = CouponNumbers()
    numbersOfCoupons = couponNumbers.inputNumberOfCoupons()
    allDistinctCoupons = couponNumbers.distinctCoupons(numbersOfCoupons)
    print("All Distinct coupons are: ", allDistinctCoupons)
