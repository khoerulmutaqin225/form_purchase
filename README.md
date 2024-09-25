# Odoo 14 POS Customization Tasks

This document outlines the additional tasks for customizing the Odoo 13 Point of Sale (POS) module. The enhancements include disabling price and discount buttons, modifying displayed values, automating email receipts, and customizing form behavior.

## Tasks Overview

1. **Disable Price and Discount Buttons**
   - Inherit the POS module to disable the Price and Discount buttons via code, rather than through configuration.

2. **Modify Displayed Values**
   - Change the displayed values of +10, +20, +50 to +10.000, +50.000, +100.000 in the POS interface.

3. **Automate Email Receipt**
   - Implement functionality to send an automatic email receipt to customers who are registered and have an email address. Display a message: "Email sudah dikirim / Email sent" upon successful sending.

4. **Chat Widget Customization**
   - Inherit the chat widget in the form view to set the background color to yellow when focused. Additionally, focus on a specific text input when the form is opened or loaded.

## Installation

1. Ensure the `form purchase` module is installed in your Odoo environment.
2. Add the provided JavaScript and Python code snippets to the relevant files within your module.
3. Restart the Odoo server.
4. Update the module in the Odoo Apps menu.

## Contribution

For any issues or suggestions regarding these tasks, please open Issues or submit Pull Requests on our GitHub repository: [repository-link](https://github.com/khoerulmutaqin225/pos-custom.git).

## License

This module is licensed under the MIT License. See the `LICENSE` file for details.
