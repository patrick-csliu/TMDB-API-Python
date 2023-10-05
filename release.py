"""Release setup

Check change log, version, and path.
"""

CHANGELOG_TEMPLATE = """
"""

INSERTS = [
    (
        "github_release",
        "[Release {version}](https://github.com/patrick-csliu/TMDB-API-Python/releases/tag/{version})",
    ),
    ("version", "{version}"),
]


class Insert:
    """Replace file content"""

    def __init__(self, file_content):
        self.content = file_content

    def insert_content(self, insert_point, content):
        """Insert the content to insert point"""
        anchor = f"{{{{insert_point.{insert_point}}}}}"
        self.content = self.content.replace(anchor, content)

    def get_content(self):
        """return file content"""
        return self.content


if __name__ == "__main__":
    import tomllib
    from os import mkdir
    from os.path import exists

    # get version from pyproject.toml
    with open("pyproject.toml", "rb") as f:
        parsed_toml = tomllib.load(f)
    version = parsed_toml["project"]["version"]

    # check change log
    log_dir = "./docs/changelogs"
    filepath = f"{log_dir}/changelog_{version}.md"
    if not exists(log_dir):
        mkdir(log_dir)
    if not exists(filepath):
        with open(filepath, "x", encoding="utf-8") as f:
            f.write(CHANGELOG_TEMPLATE)

    # Create README.md
    with open("docs/README_template.md", "r", encoding="utf-8") as f:
        readme_file = Insert(f.read())
    # point 0
    content_p0 = INSERTS[0][1].format(version=version)
    readme_file.insert_content(INSERTS[0][0], content_p0)
    # point 1
    content_p1 = INSERTS[1][1].format(version=version)
    readme_file.insert_content(INSERTS[1][0], content_p1)
    # save the file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_file.get_content())

    # returns
    print(version, filepath)
