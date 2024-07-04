import frappe

@frappe.whitelist(allow_guest=True)
def get_all_members():
    members = frappe.db.sql(f"""SELECT * FROM `tabLibrary Member`;""", as_dict=True)
    return members


def get_member(id):
    pass
