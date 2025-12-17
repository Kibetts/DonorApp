"""
Verification script to check if all blueprints are properly set up
Run this before starting the application
"""

import os
import sys

def check_file(filepath, expected_bp_name):
    """Check if a file contains the expected blueprint name"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            if f"Blueprint('{expected_bp_name}'" in content:
                print(f"✓ {filepath}: Correct blueprint name '{expected_bp_name}'")
                return True
            else:
                print(f"✗ {filepath}: Incorrect or missing blueprint name")
                print(f"  Expected: Blueprint('{expected_bp_name}', __name__)")
                return False
    except FileNotFoundError:
        print(f"✗ {filepath}: File not found")
        return False

def main():
    print("Verifying Blueprint Setup...\n")
    
    routes_dir = "app/routes"
    checks = [
        (f"{routes_dir}/donations.py", "donations_bp"),
        (f"{routes_dir}/programs.py", "programs_bp"),
        (f"{routes_dir}/stories.py", "stories_bp"),
        (f"{routes_dir}/newsletter.py", "newsletter_bp"),
        (f"{routes_dir}/volunteers.py", "volunteers_bp"),
        (f"{routes_dir}/contact.py", "contact_bp"),
    ]
    
    all_passed = True
    for filepath, bp_name in checks:
        if not check_file(filepath, bp_name):
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("✓ All blueprints are properly configured!")
        print("You can now run: flask db init")
    else:
        print("✗ Some blueprints need to be fixed")
        print("\nTo fix, ensure each route file has:")
        print("bp = Blueprint('<name>_bp', __name__)")
    print("="*50)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())