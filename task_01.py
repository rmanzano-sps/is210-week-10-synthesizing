#!/bin/env python
# -*- coding: utf-8 -*-
"""Correlating two related data sets"""

def sum_orders(customers, orders):
    """This function keeps customers as a constant
and runs through orders, matching customer ids with orders and
adding the total number of orders and add cost of each order"""
    dictionary = {}
    dictionary.update(customers)

    for customer_id in customers.keys():
        total = 0
        orders_sum = 0
        for details in orders.itervalues():
            if details['customer_id'] == customer_id:
                orders_sum += 1
                total += details['total']
        dictionary[customer_id].update({'total': total, 'orders': orders_sum})
    return dictionary
