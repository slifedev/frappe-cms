# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Reservation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		accommodation: DF.Data | None
		check_in: DF.Date | None
		check_out: DF.Date | None
		customer: DF.Data | None
		status: DF.Data | None
	# end: auto-generated types
	pass
