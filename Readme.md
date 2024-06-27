# Django-daily-quotes

A Django application that displays a "Quote of the Day" on the home page, randomly chosen from a JSON file containing 1000 quotes. The quote changes daily.

## Features

- Displays a new quote every day
- Easy to integrate with other Django apps
- Quotes are stored in a JSON file

## Usage

The application will display a new quote every day below the header on the home page.

### Adding More Quotes

To add more quotes, edit the `data.json` file located in the `quotes/static/` directory and add your quotes in the following format:

```json
[
    {
        "text": "Your new quote text",
        "author": "Author Name"
    },
    ...
]