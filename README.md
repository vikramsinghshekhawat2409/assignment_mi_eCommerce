# Assignment eCommerce Model

## Description
* A backend application for managing products based on sub-categories and categories.

* ### Skills Used:
    * Backend - Python/Django
    * Webpage - HTML/JS jQuery/Bootstrap/DataTable

## System Requirements
* python3
* web-browser

* ### Python Dependencies
    * asgiref==3.5.0
    * backports.zoneinfo==0.2.1
    * Django==4.0.4
    * djangorestframework==3.13.1
    * pytz==2022.1
    * sqlparse==0.4.2
    * tzdata==2022.1

---
**Note**
 Install app dependencies using pip install either directly or by first activating virtual environment. (venv is setup under ${project-directory}/virtual_env/~)

---
## Products Webpage:
* Can be accessed from http://127.0.0.1:8000/api/products
* Existing products can be viewed and new products can be added based on existing sub-categories and category

## Admin Details:
* username -  master_india
* password -  superuser

---
## API's Details
---
### 1. `get_all_categories` (url: http://0.0.0.0:8000/api/category/all)
#### Description
```buildoutcfg
api to fetch all categories from database
:method : GET
:return : response object containing all categories
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/category/all",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


### 2. `get_all_sub_categories` (url: http://0.0.0.0:8000/api/subcategory/all)
#### Description
```buildoutcfg
api to fetch all sub-categories from database
:method : GET
:return : response object containing all sub-categories
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/subcategory/all",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


### 3. `get_all_sub_categories_by_category` (url: http://0.0.0.0:8000/api/subcategory/by_category)
#### Description
```buildoutcfg
api to fetch all sub-categories for a specific category from database
:method : GET
:param objects: category
:return : response object containing all sub-categories
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/subcategory/by_category?category=Electronics",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


### 4. `get_all_products` (url: http://0.0.0.0:8000/api/products/all)
#### Description
```buildoutcfg
api to fetch all products from database
:method : GET
:return : response object containing all products
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/products/all",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


### 5. `get_all_products_by_category` (url: http://0.0.0.0:8000/api/products/by_category)
#### Description
```buildoutcfg
api to fetch all products for a specific category from database
:method : GET
:param objects: category
:return : response object containing all products
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/products/by_category?category=Electronics",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


### 6. `get_all_products_by_sub_category` (url: http://0.0.0.0:8000/api/products/by_sub_category)
#### Description
```buildoutcfg
api to fetch all products for a specific sub-category from database
:method : GET
:param objects: sub-category
:return : response object containing all products
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/products/by_sub_category?sub-category=Electronics",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


### 7. `add_product_for_sub_category` (url: http://0.0.0.0:8000/api/products/add)
#### Description
```buildoutcfg
api to fetch add a product for a specific sub-category into a database
:method : POST
:param objects: sub-category
:param objects: product
:return : response object containing all products
```
```javascript
var settings = {
  "url": "http://0.0.0.0:8000/api/products/add/?sub-category=2&product=Apple iPhone 13 Pro 128 GB",
  "method": "POST",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

---
End of the documentation
Copyright @2022 github repository owner