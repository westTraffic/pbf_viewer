# pbf_viewer

This project is a Django-based application.
This web app could execute SQLs against PBFs directing using DuckDB python.
Key select fields and condition fields are pre-set, and you can also add your statements.

## Index

- [Background](#Background)
- [使い方](#使い方)
- [ライセンス](#ライセンス)
- [貢献](#貢献)

## Background

Recently I bumped into a library DuckDB. From my local machine, I confirmed it is easy to execute SQLs towards my local PBF files.
I wanted to study how to build Python-Django app and also would like to help users who wish to see the PBF data easily.

## Installation Steps

1. Clone the repository.

    ```bash
    git clone https://github.com/westTraffic/pbf_viewer.git
    ```

2. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

1. Start the development server.

    ```bash
    python manage.py runserver
    ```

2. In your browser, go to the following URL.

    ```
    http://127.0.0.1:8000/
    ```

