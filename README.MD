# 🚀 Kyro SAAS

A demo how to make **SAAS Platform** using **Django**.
This demo is inspired from this django con section https://www.youtube.com/watch?v=BW9ju19u1zU&ab_channel=DjangoConUS.
Also it's have demo CRUD for simple blog module to get details how the authorization is implemented.

## 🛠️ Installation Guide

### 🔹 **Step 1: Clone the Repository**

```sh
git clone https://github.com/fahrurben/kyro-saas.git
cd kyro-saas
```

### 🔹 **Step 2: Install Backend**

```sh
cd kyro-saas
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 🔹 **API ENDPOINTS**
Also can check ```Kyro SAAS.postman_collection.json```

| HTTP Verbs | Endpoints                                   | Action                                |
|------------|---------------------------------------------|---------------------------------------|
| POST       | /api/register                               | To register new company and user      |
| POST       | /api/token                                  | To authenticate user                  |
| POST       | /api/companies/{company_id}/posts           | To create a new blog post             |
| PUT        | /api/companies/{company_id}/posts/{post_id} | To update a blog post                 |
| GET        | /api/companies/{company_id}/posts/{post_id} | To retrieve blog post                 |
| GET        | /api/companies/{company_id}/posts           | To retrieve all company blog pst      |



