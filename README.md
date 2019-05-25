# OLX

This is django based website, a replica of OLX site. It is under progress.



# Abstract



It allows the user to sell their unused item.Objective is to design this site for college purpose. Students who leave college after completion of their studies need to sell of their belongings. Like Bed-matrices, tables, chair, cooler, washing machine etc and etc. Instead of giving aways their belongings to anyone at any price, they could put it on this website with reasonable prices.This would help both the seller and buyer.Sellers can sell their product with reasonable price and buyer can get a trusted product with almost zero transportation(same college).



# What does it do?



It is django designed website which allows user to sign up and login.It also allows user mobile authentication through OTP. In case user forgets the password, it can be reset through email.

Once user is logged in, it allows user to add product and it's information. Once user post his/her product, it add to pending list of admin.

Admin is special login which verifies whether the product posted by any normal user is an authentic one.

Once admin verifies the product, it will be posted on the main page for others to view in different categories(like bedmatrices, washing machine, phone etc)

Users are allowed to view the products even when logged out but they can view the contact details only when logged in - this would prevent the users to gain info without logging in.

There is availability of "Delete/Sold product" so that user can remove the product once sold.



# How does it do?



1. It used django forms for registration and login, styles using crisp_forms, html,css, bootstrap and JS.

2. Login phone authentication is done using API from 2factor - "https://2factor.in/" 

3. Password reset and email authentication is done using django inbuilt modules.

4. Special care has been taken to avoid any unauthorised user to get access to pages through manipulating urls.

5. Two different database in use - 1st contains "verified by admin products" and 2nd "contains pending to verify products".

