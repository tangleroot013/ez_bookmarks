import json
import csv
from pathlib import Path

# Paths
JSON_FILE = Path("useful_websites.json")
CSV_FILE = Path("useful_websites.csv")
HTML_FILE = Path("bookmarks.html")

CATEGORY_MAP = {
    "technical": "Dev & Technical",
    "learning": "Knowledge & Learning",
    "creative": "Creative & Media",
    "productivity": "Productivity & Utils",
    "security": "Security"
}

def load_data():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_csv(data):
    """Regenerates useful_websites.csv from JSON data."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Number", "Category", "URL", "Description"])
        
        for item in data:
            cat_name = CATEGORY_MAP.get(item["cat"], item["cat"].title())
            writer.writerow([item["id"], cat_name, item["url"], item["desc"]])
    print(f"✅ Generated {CSV_FILE}")

def generate_html(data):
    """Regenerates browser-importable bookmarks.html from JSON data."""
    # Group items by category
    grouped = {}
    for item in data:
        cat_name = CATEGORY_MAP.get(item["cat"], item["cat"].title())
        grouped.setdefault(cat_name, []).append(item)

    html_content = [
        "<!DOCTYPE NETSCAPE-Bookmark-file-1>",
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        "<TITLE>Bookmarks</TITLE>",
        "<H1>Bookmarks</H1>",
        "<DL><p>",
        '    <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">Master Resource Library</H3>',
        "    <DL><p>"
    ]

    for cat_name, items in grouped.items():
        html_content.append(f'        <DT><H3 ADD_DATE="0" LAST_MODIFIED="0">{cat_name}</H3>')
        html_content.append("        <DL><p>")
        for item in items:
            html_content.append(f'            <DT><A HREF="{item["url"]}">{item["name"]}</A>')
        html_content.append("        </DL><p>")

    html_content.extend([
        "    </DL><p>",
        "</DL><p>"
    ])

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(html_content))
    print(f"✅ Generated {HTML_FILE}")

if __name__ == "__main__":
    if not JSON_FILE.exists():
        print(f"❌ Error: {JSON_FILE} not found.")
    else:
        dataset = load_data()
        generate_csv(dataset)
        generate_html(dataset)
        print("🎉 Sync complete! Your repository files are up to date.")
