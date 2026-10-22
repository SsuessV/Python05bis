import os
import sys
import site

t_or_f = sys.prefix != sys.base_prefix
if t_or_f:
    print("LABORATORY STATUS: The laboratory is sealed")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys. prefix}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting\nthe global system.")
    print("Reagent installation path:\n", site.getsitepackage())
else:
    print("LABORATORY STATUS: You are working in the open")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print("Global package location:", site.getsitepackage())
    print("To seal the laboratory, run:")
    print("python3-m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env/Scripts/activate # On Windows")
    print()
    print("Then run this program again.")

