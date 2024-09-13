# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AccommodationUnit(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		accommodation: DF.Link | None
		max_occupancy: DF.Int
		unit_name: DF.Data | None
		unit_type: DF.Data | None
	# end: auto-generated types
	pass
