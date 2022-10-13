<h1 align="center"> Dockerized Django Ecommerce - Django Rest framework API</h1> <br>


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [APIs](#apis)

## Introduction

Ecommerce Backend API. Built with Python - Django /Django Rest Framework and Docker.
- Prequesites: Docker and docker compose

## Features
* Categories, Products are seeded
* Superadmin and his billing profile is seeded
* Using both swagger and DRF browable API as API documentation
* Users can Register/ Login
* Admin can do CRUD to Categories/ Category
* Admin can do CRUD to Products/ Product
* Admin can do CRUD to Billing Profiles
* Admin can do CRUD to Orders
* Authenticated Users can make POST requests to Product Category & Product
* Unauthenticated Users can only make GET requests to Product Category & Product
* Authorized Users can create Billing profile, add to cart, checkout
* Authorized Users can view his orders and cancel an order

## Installation

**Installation Process (Linux/ Windows WSL)**

1. Create a working directory, go to working directory and clone this repo into it
2. Inside working directory. Run docker:  `docker-compose up`
3. Wait some times for docker up and running, then Go to http://localhost:8000

## Usage
- App settings and urls are in ecommerce directory
- API modules are in api directory
- We have 2 running containers: webm (web container) and dbm (postgres container). run `docker ps` to see containers, ports...
- Admin page: http://localhost:8000/admin
- Superadmin User: admin@site.com/ 123456 (You can change this in api/migrations/0001_initial.py)
- Seed data for Billing profiles, Categories, Products is in fixture.json

## APIs
1. Register: use swagger or:
`curl -X POST "http://localhost:8000/api/user/" -H  "accept: application/json" -H  "Content-Type: application/json" -H  "X-CSRFToken: {Token string}" -d "{  \"name\": \"string\",  \"email\": \"user@example.com\",  \"password\": \"string\",  \"phone\": \"string\",  \"gender\": \"string\",  \"is_active\": true,  \"is_staff\": true,  \"is_superuser\": true}"`
2. Login: use swagger login or access this url: http://localhost:8000/auth/login/
3. Logout: use swagger logout or access this url: http://localhost:8000/auth/logout/
4. Product list: http://localhost:8000/api/product/
5. Billing profiles: http://localhost:8000/api/profiles/
6. Cart's products and add-to-cart: http://localhost:8000/api/cart/
  - For demo purpose, we added random product to cart each time you make post request/ press post button. view codes in api/cart/views.py at line 26
7. Checkout: http://localhost:8000/api/order/. Order is fulfilled with current cart and current user's profile. Press Post button to create order
8. User's orderlist: http://localhost:8000/api/accounts/orders/
9. Cancel an order: http://localhost:8000/api/order/{order_id}/cancel/



