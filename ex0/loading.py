import importlib

print("REAGENT STATUS: Loading reagents...")
print("Checking dependencies:")

packages = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
}

missing = False

for module_name in ("pandas", "numpy"):
    try:
        package = importlib.import_module(module_name)
        print(f"[OK] '{module_name}' ({package._version_}) - {package[module_name]}")
    except ImportError:
        print(f"[MISSING] {module_name}")
        missing = True

if missing:
    print("\nSome reagents are missing. From the repository's root folder, install with pip:")
    print(" python -m pip install -r ex0/requirements.txt")
    print("For Poetry, go into ex0 and run:")
    print(" poetry install")
    print(" poetry run python loading.py")

print("\npip vs Poetry:")
print("requirements.txt lists packages for pip to resolve during installation.")
print("pyproject.toml declares Poetry dependencies; poetry.lock records resolved versions.")

if not missing:
    print("\nAll reagents present and accounted for.")