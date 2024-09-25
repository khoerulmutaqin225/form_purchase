odoo.define('form_purchase.pos_inherit', function(require) {
    'use strict';

    const PosModel = require('point_of_sale.models');

    const _super_get_orderlines = PosModel.Order.prototype.get_orderlines;
    PosModel.Order = PosModel.Order.extend({
        get_orderlines: function() {
            const orderlines = _super_get_orderlines.apply(this, arguments);
            for (const line of orderlines) {
                if (line.price) {
                    line.price = line.price * 1000;  // Modify the displayed price
                }
            }
            return orderlines;
        },
    });
});
