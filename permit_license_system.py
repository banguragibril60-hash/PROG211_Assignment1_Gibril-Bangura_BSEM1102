"""
Digital Permit & License Management System
Object-Oriented Programming 1 - Individual Assignment
Domain: Government
Aligned with Digital Public Goods (DPG) principles
"""

from datetime import datetime, timedelta

# ============================================================
# CLASS 1: Permit
# ============================================================
class Permit:
    """Represents a government permit (e.g., business, construction, trading)."""

    # Class attribute – shared by all Permit objects
    total_permits_created = 0

    def __init__(self, permit_id, permit_type, category, issue_date, expiry_date, status="Active"):
        """
        Initialize a Permit object.
        Privacy note: Only non-sensitive, anonymized data is stored.
        """
        self.permit_id = permit_id          # e.g. "PMT-2026-001"
        self.permit_type = permit_type      # e.g. "Business", "Construction"
        self.category = category            # e.g. "Retail", "Residential"
        self.issue_date = issue_date        # string "YYYY-MM-DD"
        self.expiry_date = expiry_date      # string "YYYY-MM-DD"
        self.status = status                # Active / Expired / Suspended

        Permit.total_permits_created += 1

    # ---------- Instance Methods ----------
    def display_info(self):
        """Display all details of this permit."""
        print(f"\n--- Permit Details ---")
        print(f"ID          : {self.permit_id}")
        print(f"Type        : {self.permit_type}")
        print(f"Category    : {self.category}")
        print(f"Issue Date  : {self.issue_date}")
        print(f"Expiry Date : {self.expiry_date}")
        print(f"Status      : {self.status}")

    def update_status(self, new_status):
        """Update the status of the permit (instance method)."""
        valid_statuses = ["Active", "Expired", "Suspended", "Revoked"]
        if new_status in valid_statuses:
            old = self.status
            self.status = new_status
            print(f"Status of {self.permit_id} changed from '{old}' to '{new_status}'.")
        else:
            print(f"Invalid status. Allowed: {valid_statuses}")

    def is_valid(self):
        """Check whether the permit is still valid based on expiry date."""
        today = datetime.now().date()
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        return today <= expiry and self.status == "Active"

    # ---------- Class Method ----------
    @classmethod
    def create_standard(cls, permit_type, category, validity_days=365):
        """
        Class method: Create a new Permit with auto-generated ID
        and standard validity period.
        """
        Permit.total_permits_created += 1
        new_id = f"PMT-{datetime.now().year}-{Permit.total_permits_created:03d}"
        issue = datetime.now().date()
        expiry = issue + timedelta(days=validity_days)

        return cls(
            permit_id=new_id,
            permit_type=permit_type,
            category=category,
            issue_date=str(issue),
            expiry_date=str(expiry),
            status="Active"
        )

    # ---------- Static Method ----------
    @staticmethod
    def validate_id_format(permit_id):
        """Static method: Check if a permit ID follows the expected format."""
        return permit_id.startswith("PMT-") and len(permit_id) >= 12


# ============================================================
# CLASS 2: License
# ============================================================
class License:
    """Represents a government license (e.g., driving, professional, trading)."""

    total_licenses_created = 0

    def __init__(self, license_id, license_type, category, issue_date, expiry_date, status="Active"):
        self.license_id = license_id
        self.license_type = license_type
        self.category = category
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.status = status

        License.total_licenses_created += 1

    def display_info(self):
        """Display all details of this license (instance method)."""
        print(f"\n--- License Details ---")
        print(f"ID          : {self.license_id}")
        print(f"Type        : {self.license_type}")
        print(f"Category    : {self.category}")
        print(f"Issue Date  : {self.issue_date}")
        print(f"Expiry Date : {self.expiry_date}")
        print(f"Status      : {self.status}")

    def update_status(self, new_status):
        """Update the status of the license (instance method)."""
        valid_statuses = ["Active", "Expired", "Suspended", "Revoked"]
        if new_status in valid_statuses:
            old = self.status
            self.status = new_status
            print(f"Status of {self.license_id} changed from '{old}' to '{new_status}'.")
        else:
            print(f"Invalid status. Allowed: {valid_statuses}")

    def is_valid(self):
        """Check whether the license is still valid."""
        today = datetime.now().date()
        expiry = datetime.strptime(self.expiry_date, "%Y-%m-%d").date()
        return today <= expiry and self.status == "Active"

    @classmethod
    def create_standard(cls, license_type, category, validity_days=730):
        """Class method: Create a new License with auto-generated ID."""
        License.total_licenses_created += 1
        new_id = f"LIC-{datetime.now().year}-{License.total_licenses_created:03d}"
        issue = datetime.now().date()
        expiry = issue + timedelta(days=validity_days)

        return cls(
            license_id=new_id,
            license_type=license_type,
            category=category,
            issue_date=str(issue),
            expiry_date=str(expiry),
            status="Active"
        )

    @staticmethod
    def validate_id_format(license_id):
        """Static method: Validate license ID format."""
        return license_id.startswith("LIC-") and len(license_id) >= 12


# ============================================================
# DATA STRUCTURE + HELPER FUNCTIONS (Task 2)
# ============================================================
# We use a DICTIONARY to store multiple objects.
# Key = unique ID, Value = the Permit or License object
registry = {}


def add_record(record):
    """Add a Permit or License object to the registry dictionary."""
    if isinstance(record, Permit):
        key = record.permit_id
    elif isinstance(record, License):
        key = record.license_id
    else:
        print("Error: Only Permit or License objects can be added.")
        return

    if key in registry:
        print(f"Record with ID {key} already exists.")
    else:
        registry[key] = record
        print(f"Record {key} added successfully.")


def display_all_records():
    """Display every record currently stored in the registry."""
    if not registry:
        print("\nNo records found in the system.")
        return

    print("\n========== ALL RECORDS IN REGISTRY ==========")
    for key, record in registry.items():
        record.display_info()
    print("=============================================")


def display_record_by_id(record_id):
    """Display a single record by its ID."""
    record = registry.get(record_id)
    if record:
        record.display_info()
    else:
        print(f"No record found with ID: {record_id}")


def count_records():
    """Return how many records are currently stored."""
    return len(registry)


# ============================================================
# DEMONSTRATION / MAIN PROGRAM
# ============================================================
def main():
    print("=" * 60)
    print("   DIGITAL PERMIT & LICENSE MANAGEMENT SYSTEM")
    print("   (Aligned with Digital Public Goods Principles)")
    print("=" * 60)

    # ----- Create objects using class methods -----
    print("\n[1] Creating standard permits and licenses...")

    permit1 = Permit.create_standard("Business", "Retail Shop", validity_days=365)
    permit2 = Permit.create_standard("Construction", "Residential Building", validity_days=180)
    license1 = License.create_standard("Professional", "Electrician", validity_days=730)
    license2 = License.create_standard("Trading", "Market Stall", validity_days=365)

    # ----- Demonstrate object interaction & adding to data structure -----
    print("\n[2] Adding records to the registry (dictionary)...")
    add_record(permit1)
    add_record(permit2)
    add_record(license1)
    add_record(license2)

    # ----- Display all records -----
    print("\n[3] Displaying all records...")
    display_all_records()

    # ----- Instance method usage -----
    print("\n[4] Updating status of a permit (instance method)...")
    permit1.update_status("Suspended")

    print("\n[5] Checking validity of records (instance method)...")
    print(f"{permit1.permit_id} is valid? → {permit1.is_valid()}")
    print(f"{license1.license_id} is valid? → {license1.is_valid()}")

    # ----- Static method usage -----
    print("\n[6] Validating ID formats (static methods)...")
    print(f"Is 'PMT-2026-001' valid format? → {Permit.validate_id_format('PMT-2026-001')}")
    print(f"Is 'XYZ-999' valid format?      → {Permit.validate_id_format('XYZ-999')}")

    # ----- Class attribute usage -----
    print(f"\n[7] Total permits created (class attribute): {Permit.total_permits_created}")
    print(f"    Total licenses created (class attribute): {License.total_licenses_created}")
    print(f"    Total records in registry: {count_records()}")

    # ----- Lookup by ID -----
    print("\n[8] Looking up a specific record...")
    display_record_by_id("PMT-2026-001")

    print("\n" + "=" * 60)
    print("Demonstration completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()