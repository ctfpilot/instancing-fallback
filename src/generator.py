
import os
from pathlib import Path

LAYOUTS = []
CONTENTS = []
JS_SCRIPTS = ""
CSS_STYLES = ""

def load_layouts():
    layouts_path = Path(__file__).parent.absolute() / "layouts"
    print("Loading layouts from:", layouts_path)
    for layout_file in os.listdir(layouts_path):
        if layout_file.endswith(".html"):
            filename = layout_file.split(".")[0]
            with open(layouts_path / layout_file, "r") as f:
                layout_content = f.read()
                LAYOUTS.append((filename, layout_content))

def load_contents():
    contents_path = Path(__file__).parent.absolute() / "content"
    print("Loading contents from:", contents_path)
    for content_file in os.listdir(contents_path):
        if content_file.endswith(".html"):
            filename = content_file.split(".")[0]
            with open(contents_path / content_file, "r") as f:
                content_data = f.read()
                CONTENTS.append((filename, content_data))

def load_js_scripts():
    filename = "./js/main.js"
    js_path = Path(__file__).parent.absolute() / filename
    print("Loading JS scripts from:", js_path)
    global JS_SCRIPTS
    with open(js_path, "r") as f:
        JS_SCRIPTS = f.read()

def load_css_styles():
    filename = "./css/main.css"
    css_path = Path(__file__).parent.absolute() / filename
    print("Loading CSS styles from:", css_path)
    global CSS_STYLES
    with open(css_path, "r") as f:
        CSS_STYLES = f.read()

def replace_indented_placeholder(template, placeholder, content):
    """
    Replaces a placeholder in a template string with the given content, preserving indentation.

    For each line in the template containing the placeholder, the function determines the indentation
    (the substring before the placeholder) and applies this indentation to each line of the replacement content.
    The placeholder line is replaced by the content lines, each indented to match the original placeholder's indentation.

    Args:
        template (str): The template string containing the placeholder.
        placeholder (str): The placeholder text to replace.
        content (str): The content to insert at the placeholder location.

    Returns:
        str: The modified template with the placeholder replaced and indentation preserved.
    """
    
    lines = template.splitlines()
    new_lines = []
    for line in lines:
        if placeholder in line:
            indent = line[:line.index(placeholder)]
            content_lines = content.splitlines()
            for c_line in content_lines:
                new_lines.append(indent + c_line)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

def generate():
    for content_name, content_data in CONTENTS:
        content_filename = content_name
        
        layout, filename = content_filename.split("_", 1)
        
        layout_template = next((l for l_name, l in LAYOUTS if l_name == layout), None)
        if layout_template is None:
            print(f"Layout '{layout}' not found for content '{content_name}'")
            continue
        
        final_html = replace_indented_placeholder(layout_template, "/**CHALLENGE_HTML**/", content_data)
        final_html = replace_indented_placeholder(final_html, "/**CHALLENGE_JS**/", JS_SCRIPTS)
        final_html = replace_indented_placeholder(final_html, "/**CHALLENGE_CSS**/", CSS_STYLES)
        
        if layout == "error":
            final_html = final_html.replace("/**ERROR_CODE**/", filename)
        
        output_path = (Path(__file__).parent.absolute() / ".." / "public" / f"{filename}.html").resolve()
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(final_html)
        print(f"Generated: {output_path}")
            
            

load_layouts()
load_contents()
load_js_scripts()
load_css_styles()
generate()

