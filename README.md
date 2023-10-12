# condo-conta-test

Simulation of payment API done in 3 hours.

### Executing project

Install modules:

```
pip3 install -r requirements.txt
```

Run tests:

```
python3 manage.py
```

Run API locally:

```
python3 manage.py runserver 0.0.0.0:8000
```

### Architecture decision

Given that condo conta's looking for 'serverful' development, I wanted to execute this project using something such as Django, Flask or FastAPI. Django has a lot of features out of the box that would help me to develop fast and in a clean way, so this was my way to go. For scalability other options would perform better.

I also think that it would be great to set up the environment inside a docker container, but since there was not too much time to create it and it would need to execute tests inside the container, which would need to be configured, I decided to not use it at the moment.

The database used is django's default sqlite, even tough it's an obvious decision to change it to postgres in almost every production environment.

### DB Modeling

I decided to use django's default users to assign two accounts each, a saving and a checking one. They should be binded on user creation. Accounts share the same table with a column to categorize them. For transactions, there is another table that will store payer, receiver and other informations.

Django has a very powerful functionality to display easily relationships such that it is possible to list the expenses or revenues of accounts without much effort.

### API Endpoints

Since I'm using DRF's viewsets, there's plenty REST endpoints available. The most important ones being:

#### New user - POST /users/

This is where all starts, by creating one user which automatically creates their two accounts. Send username in the body.

#### List User - GET /users/

Lists all the users. Here, it is possible to obtain the account ID to create transactions.

#### New Transaction - POST /transactions/

Create a new transaction between accounts. Send payer (payer ID), receiver (receiver ID), amount and description on body,

#### List Accounts - GET /accounts/

Lists all accounts with their respectives expenses and revenues.

#### List Transactions - GET /transactions/

List all transactions.

### Testing

Test cases cover both a success case and a failure case. They have a lot of room for improvement. Due to the time limit, instead of creating the models by itself, I used endpoints to create them, which is a bad practice in terms of isolating testings. It also should be noticed that due to time reasons also, there are no validations in the endpoints so, for example, one could transfer negative money and earn money from an account.
