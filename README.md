Akatama's Slice of the Internet
===============================

Just a simple webapp that I can write some blog posts, have a page with my resume and an about me.

This is designed in Django. I did follow [this guide](https://realpython.com/build-a-blog-from-scratch-django/) to get started. I have drifted from that tutorial a bit, but its a great starting point.

Quick Start
-----------

No one but me should really be running it, but in case you really want to.

1. Clone the repo
2. Create a virtual environment

  ```bash
  uv venv
  ```

3. Source the virtual environment

  ```bash
  source .venv/bin/activate
  ```

4. Download the dependenices

  ```bash
  uv sync
  ```

5. Set up the Django migrations

  ```bash
  uv run manage.py migrate
  ```

6. Run the server on your local

  ```bash
  uv run manage.py runserver
  ```

7. Open localhost:8000 in a browser
