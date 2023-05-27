# python-web-tornado-async-api-mysql-tortoise-pop

## Description
Simple web app that serves an api
for a tornado project as a frontend 
and remote calling a fastapi backend.

Uses async functions and tortoise oem to query a table `pop`.

Remotely tested with *testify*.

## Tech stack
- python
  - tornado
  - fastapi
  - sqlalchemy
  - testify
  - requests
- mysql

## Docker stack
- python:latest
- mariadb:latest

## To run
`sudo ./install.sh -u`
- Get all pops: http://localhost/pop

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [HTTPServer config](https://phrase.com/blog/posts/tornado-web-framework-i18n/)
- [Code based on](https://www.tornadoweb.org/en/stable/)
- [Sqlalchemy code](https://medium.com/swlh/tornado-and-sqlalchemy-847eecbc0445)