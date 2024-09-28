odoo.define('point_of_sale.PaymentScreenNumpadCustom', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');

    class PaymentScreenNumpadCustom extends PosComponent {
        constructor() {
            super(...arguments);
            this.decimalPoint = this.env._t.database.parameters.decimal_point;
        }
    }
    PaymentScreenNumpadCustom.template = 'PaymentScreenNumpadCustom';

    Registries.Component.add(PaymentScreenNumpadCustom);

    return PaymentScreenNumpadCustom;
});
