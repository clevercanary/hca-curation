#!/usr/bin/env python3
"""
Simple script to validate h5ad files with HCA schema.

Usage:
    poetry run python validate_file.py <path/to/file.h5ad>
    poetry run python validate_file.py <path/to/file.h5ad> --with-labels
"""
import sys
from hca_schema_validator import HCAValidator

def main():
    # Parse command-line arguments
    if len(sys.argv) < 2:
        print("Error: Please provide a file path")
        print("\nUsage:")
        print("  poetry run python validate_file.py <path/to/file.h5ad>")
        print("  poetry run python validate_file.py <path/to/file.h5ad> --with-labels")
        sys.exit(1)
    
    h5ad_file = sys.argv[1]
    ignore_labels = "--with-labels" not in sys.argv
    
    print(f"\n{'='*70}")
    print(f"HCA Schema Validator")
    print(f"{'='*70}")
    print(f"File: {h5ad_file}")
    print(f"Ignore Labels: {ignore_labels}")
    print(f"{'='*70}\n")
    
    validator = HCAValidator(ignore_labels=ignore_labels)
    is_valid = validator.validate_adata(h5ad_file)
    
    print(f"\n{'='*70}")
    if is_valid:
        print("✅ VALID - File passes HCA schema validation")
    else:
        print("❌ INVALID - File has validation errors")
    print(f"{'='*70}\n")
    
    if validator.errors:
        print(f"ERRORS ({len(validator.errors)}):")
        print("-" * 70)
        for i, error in enumerate(validator.errors, 1):
            print(f"{i}. {error}")
        print()
    
    if validator.warnings:
        print(f"WARNINGS ({len(validator.warnings)}):")
        print("-" * 70)
        for i, warning in enumerate(validator.warnings, 1):
            print(f"{i}. {warning}")
        print()
    
    if not validator.errors and not validator.warnings:
        print("No errors or warnings! 🎉\n")

if __name__ == "__main__":
    main()
