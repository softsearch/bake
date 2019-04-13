# bake

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites 

```
 - python3
 - postgress
 - git
 - pip3
```

Clone the project to your local machine

```
git clone git@github.com:softsearch/bake.git
```


### Installing

Create a virtual environment using using the following command

```
 python3 -m venv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

You can use virtualenv to manage you envs

Install requirements

```
pip install -r requirements.txt
```

Install postgress and create a new database 

To load `.env` create a copy of the `.env_example` 

```
cp .env_example .env
```

The `.env` contains all the enviromentral variables neeed by the peoject.

Edit `DATABASE_URL` in the `.env` file to include your database creadentails. The format is as follows

```bash
DATABASE_URL=psql://username:password@host/dbname
```



