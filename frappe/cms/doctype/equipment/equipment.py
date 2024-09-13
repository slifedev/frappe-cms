# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Equipment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		accommodation_unit: DF.Link | None
		equipment_type: DF.Literal["Unit", "Kitchen", "Bedroom", "Bethroom", "Safety"]
		label: DF.Data
	# end: auto-generated types
	pass
