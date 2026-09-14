/**
 * Problem Link : https://leetcode.com/problems/customers-who-never-order/
 * Platform     : LeetCode
 * Difficulty   : Easy
 */

#include <bits/stdc++.h>
using namespace std;

# Write your MySQL query statement below
SELECT customers.name as Customers
FROM customers
LEFT JOIN orders
ON customers.id = orders.customerId
WHERE orders.id is NULL AND orders.customerId is NULL
