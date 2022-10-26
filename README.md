# django_pokemon

Repo for django_pokemon

## Overview
------

django_pokemon is an app that allows users to capture, release & see a detail view of each individual Pokemon

### Technologies used

* Django 4.1
* VueJS 2.0
* Bootstrap v5.1

## Features
------

- User System
  - [x] User sign up form
  - [x] User log out
  - [ ] Update profile
  - [ ] Delete Profile
- Pokemon
  - [ ] Create a Pokemon
  - [ ] Delete a Pokemon
  - [x] Public homepage listing all Pokemon
  - [x] Detail page for each individual Pokemon

## Data Model
----
* Pokemon
  * number (IntegerField)
  * name (charfield)
  * height (FloatField)
  * weight (FloatField)
  * image_front (URLField)
  * image_back (URLField)
  * caught_by (ManyToManyField to User)
* Type
  * type (charfield)
  * pokemon (ManyToManyField to Pokemon)
  * city (foreignkey to City)
* User (extends built-in user)

## Pages
-------
- Index
  - list of Pokemon
  - button for catching Pokemon
  - button for releasing Pokemon (if caught already)
  - header
    - log-in link if not logged in
    - log-out link if logged in
- Pokemon Detail
  - stats of Pokemon
- Registration
  - user registration form using django forms
- Login
  - login form
  - redirect to index page after logging in
## Schedule
----
* Week 1
    * ~~create models for Pokemon~~
    * ~~create models for Users~~
    * ~~create index template and view~~
    * ~~show test Pkemon on page~~
    * add forms for new Pokemon, photos & signup
* Week 2
    * fix issues from week 1
    * add ability to sort Pokemon
    * ~~begin styling for readability~~
* Week 3
    * Fix recurring issues from weeks 1/2
    * finish any styling on app
