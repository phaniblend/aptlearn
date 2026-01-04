import os

# ================= CONFIG =================

ROOT_DIR = os.getcwd()  # run from repo root
OUTPUT_FILE = "codebase_dump.txt"

IGNORE_DIRS = {
    "node_modules",
    ".git",
    ".vscode",
    "__pycache__",
    "dist",
    "build"
}

IGNORE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg",
    ".ico", ".exe", ".dll", ".zip", ".tar",
    ".gz", ".lock"
}

# =========================================


def should_ignore_dir(dir_name):
    return dir_name in IGNORE_DIRS


def should_ignore_file(file_name):
    _, ext = os.path.splitext(file_name)
    return ext.lower() in IGNORE_EXTENSIONS


def dump_codebase():
    with open(OUTPUT_FILE, "w", encoding="utf-8", errors="ignore") as out:
        for root, dirs, files in os.walk(ROOT_DIR):
            rel_root = os.path.relpath(root, ROOT_DIR)

            # Handle ignored directories
            ignored = [d for d in dirs if should_ignore_dir(d)]
            for d in ignored:
                ignored_path = os.path.join(rel_root, d)
                out.write(f"\n//{ignored_path.replace(os.sep, '/')}\n")

            # Remove ignored dirs from traversal
            dirs[:] = [d for d in dirs if not should_ignore_dir(d)]

            for file in files:
                if should_ignore_file(file):
                    continue

                file_path = os.path.join(root, file)
                rel_file_path = os.path.relpath(file_path, ROOT_DIR)
                normalized_path = rel_file_path.replace(os.sep, "/")

                out.write(f"\n//{normalized_path}\n\n")

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        out.write(content)
                        if not content.endswith("\n"):
                            out.write("\n")
                except Exception as e:
                    out.write(f"// ERROR READING FILE: {e}\n")


if __name__ == "__main__":
    dump_codebase()
    print(f"✅ Codebase dumped to {OUTPUT_FILE}")
