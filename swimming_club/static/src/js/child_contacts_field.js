import { registry } from "@web/core/registry";
import { X2ManyField, x2ManyField } from "@web/views/fields/x2many/x2many_field";

/**
 * Children on the parent's Contacts tab:
 * - a child that is not saved yet opens in the simple popup (as in standard Odoo),
 * - an existing child opens in the full contact form (with breadcrumb back to the parent).
 */
export class ChildContactsField extends X2ManyField {
    async openRecord(record) {
        if (!this.canOpenRecord || record.isNew) {
            return super.openRecord(record);
        }
        return this.switchToForm(record, {});
    }
}

export const childContactsField = {
    ...x2ManyField,
    component: ChildContactsField,
};

registry.category("fields").add("swimming_club_child_contacts", childContactsField);
