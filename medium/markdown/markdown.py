import re


def parse(markdown):
    lines = markdown.split("\n")
    result = ""
    in_list = False

    for line in lines:
        line = line.strip()

        # Header
        header = re.match("(#+).*", line)
        if header:
            header = len(header.group(1))
            line = f"<h{header}>" + line[header + 1 :] + f"</h{header}>"

        # Listing start
        listing = re.match(r"\* (.*)", line)
        if listing:
            current = listing.group(1)
            line = "<li>" + current + "</li>"
            if not in_list:
                line = "<ul>" + line
                in_list = True

        # Plain text
        if not re.match("<h|<ul|<p|<li", line):
            line = "<p>" + line + "</p>"

        # Bold
        bold = re.match("(.*)__(.*)__(.*)", line)
        if bold:
            line = (
                bold.group(1) + "<strong>" + bold.group(2) + "</strong>" + bold.group(3)
            )

        # Italic
        italic = re.match("(.*)_(.*)_(.*)", line)
        if italic:
            line = (
                italic.group(1) + "<em>" + italic.group(2) + "</em>" + italic.group(3)
            )

        # Listing end
        if not listing and in_list:
            line = "</ul>" + line
            in_list = False

        result += line

    if in_list:
        result += "</ul>"

    return result
