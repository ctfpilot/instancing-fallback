# Error page generation

In order to generate the error pages, run the `generator.py` script in `src`:

```sh
python3 src/generator.py
```

This will generate the error pages based on the layouts and content defined in the `layouts` and `content` folders respectively.

## Templating

A custom templating system is used to insert content into the layouts.  
Placeholders in the layout files are defined using the format `/**PLACEHOLDER_NAME**/`.  
The generator script replaces these placeholders with the corresponding content.

The placeholders used are:

- `/**CHALLENGE_HTML**/`: The main HTML content for the page. Inserted from `content`.
- `/**CHALLENGE_JS**/`: Any JavaScript code to be included in the page. Inserted from `js`.
- `/**CHALLENGE_CSS**/`: Any CSS styles to be included in the page . Inserted from `css`.

For `error` layout pages, an additional placeholder is used:

- `/**ERROR_CODE**/`: The error code for the error page (e.g., 404, 500). Replaced with the filename part of the content file.

The templating use multiple layouts, which are defined in the `layouts` folder.  
Each content file in the `content` folder should be prefixed with the layout name, followed by an underscore.  
For example, a content file named `error_404.html` will use the `error` layout, and produce a page named `404.html`.
