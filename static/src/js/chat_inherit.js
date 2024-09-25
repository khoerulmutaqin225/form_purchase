odoo.define('form_purchase.chat_inherit', function(require) {
    'use strict';

    const FormView = require('web.FormView');

    FormView.include({
        render: function() {
            this._super.apply(this, arguments);
            this.$('.o_chat_input').focus(function() {
                $(this).css('background-color', 'yellow');
            });
        },
        start: function() {
            this._super.apply(this, arguments);
            this.$('.o_chat_input').focus();
        }
    });
});
