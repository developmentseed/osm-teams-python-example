# OSM Teams API - Python/Flask

This app demonstrates how to integrate with [mapping.team](https://dev.mapping.team), the index of OpenStreetMap teams. It uses Python/Flask and [authlib](https://authlib.org) to create the connection. `mapping.team` is an instance of the [OSM Teams API](https://github.com/developmentseed/osm-teams)

## Requirements

- Python 3 and pip

## App structure

On the front-end,

    stati/client.js contains the API code
    static/style.css and templates/index.html show the teams

On the back-end,

    your app starts at app.js
    secret configuration goes in .env

## Installation

### Clone the repo

Clone this repo with git:

```
git clone https://github.com/developmentseed/osm-teams-python-example.git
```

Change directory into the repo:

```
cd osm-teams-python-example
```

### Create your app on [auth.mapping.team](https://auth.mapping.team)

To run this project you'll need a `TEAMS_CLIENT_ID` and `TEAMS_CLIENT_SECRET` from [auth.mapping.team](https://auth.mapping.team). There you'll log in using your OpenStreetMap account, then visit the [create client page](https://auth.mapping.team/teams/create) and follow these instructions:

1. Add a name for your app
2. The callback will be `http://127.0.0.1:5000/auth` or whatever URL this example is running on
3. Click on "Add new App" to receive your credentials
4. The TEAMS_CLIENT_ID is the `client_id` returned by the site
5. The TEAMS_CLIENT_SECRET is the `client_secret`returned by the site

### Create the .env file

Create a .env file following the structure in `.env.sample`

```sh
TEAMS_CLIENT_ID=<your app client id>
TEAMS_CLIENT_SECRET=<your app client secret>
```

You can copy `.env.sample` to get started:

```
cp .env.sample .env
```

### Install the dependencies

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Run the example

```sh
flask run
```

Now you should be able to see the example app in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)!

From here you can:

- create teams on mapping.team and see them in a list on the example app
- join other teams on mapping.team and see them in the list as well
- [check out the api docs](https://dev.mapping.team/api/) and experiment with the api to get a better idea of how you can integrate mapping.team with your application
