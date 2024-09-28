odoo.define('form_purchase.NumberBuffer', function(require) {
    'use strict';

    const { parse } = require('web.field_utils');
    const { Gui } = require('point_of_sale.Gui');
    const NumberBuffer = require('point_of_sale.NumberBuffer');
    const INPUT_KEYS = new Set(
        ['Delete', 'Backspace', '+1', '+2', '+5', '+10', '+20', '+50','+60','+10000','+50000','+100000'].concat('0123456789+-.,'.split(''))
    );

    const CONTROL_KEYS = new Set(['Enter', 'Esc']);
    const ALLOWED_KEYS = new Set([...INPUT_KEYS, ...CONTROL_KEYS]);

    // Function modify
    function _onInput(keyAccessor) {
            return () => {
                if (this.eventsBuffer.length <= 2) {
                    // Check first the buffer if its contents are all valid
                    // number input.
                    for (let event of this.eventsBuffer) {
                        if (!ALLOWED_KEYS.has(keyAccessor(event))) {
                            this.eventsBuffer = [];
                            return;
                        }
                    }
                    // At this point, all the events in buffer
                    // contains number input. It's now okay to handle
                    // each input.
                    for (let event of this.eventsBuffer) {
                        this._handleInput(keyAccessor(event));
                        event.preventDefault();
                        event.stopPropagation();
                    }
                }
                this.eventsBuffer = [];
            };      
    };

    function _handleInput(key) {
            if (key === 'Enter' && this.config.triggerAtEnter) {
                this.component.trigger(this.config.triggerAtEnter, this.state);
            } else if (key === 'Esc' && this.config.triggerAtEsc) {
                this.component.trigger(this.config.triggerAtEsc, this.state);
            } else if (INPUT_KEYS.has(key)) {
                this._updateBuffer(key);
                if (this.config.triggerAtInput)
                    this.component.trigger(this.config.triggerAtInput, { buffer: this.state.buffer, key });
            }
    };

    function _updateBuffer(input) {
            const isEmpty = val => {
                return val === '' || val === null;
            };
            if (input === undefined || input === null) return;
            let isFirstInput = isEmpty(this.state.buffer);
            if (input === ',' || input === '.') {
                if (isFirstInput) {
                    this.state.buffer = '0' + this.decimalPoint;
                } else if (!this.state.buffer.length || this.state.buffer === '-') {
                    this.state.buffer += '0' + this.decimalPoint;
                } else if (this.state.buffer.indexOf(this.decimalPoint) < 0) {
                    this.state.buffer = this.state.buffer + this.decimalPoint;
                }
            } else if (input === 'Delete') {
                if (this.isReset) {
                    this.state.buffer = '';
                    this.isReset = false;
                    return;
                }
                this.state.buffer = isEmpty(this.state.buffer) ? null : '';
            } else if (input === 'Backspace') {
                if (this.isReset) {
                    this.state.buffer = '';
                    this.isReset = false;
                    return;
                }
                const buffer = this.state.buffer;
                if (isEmpty(buffer)) {
                    this.state.buffer = null;
                } else {
                    const nCharToRemove = buffer[buffer.length - 1] === this.decimalPoint ? 2 : 1;
                    this.state.buffer = buffer.substring(0, buffer.length - nCharToRemove);
                }
            } else if (input === '+') {
                if (this.state.buffer[0] === '-') {
                    this.state.buffer = this.state.buffer.substring(1, this.state.buffer.length);
                }
            } else if (input === '-') {
                if (isFirstInput) {
                    this.state.buffer = '-0';
                } else if (this.state.buffer[0] === '-') {
                    this.state.buffer = this.state.buffer.substring(1, this.state.buffer.length);
                } else {
                    this.state.buffer = '-' + this.state.buffer;
                }
            } else if (input[0] === '+' && !isNaN(parseFloat(input))) {
                // when input is like '+10', '+50', etc
                const inputValue = parse.float(input.slice(1));
                const currentBufferValue = this.state.buffer ? parse.float(this.state.buffer) : 0;
                this.state.buffer = this.component.env.pos.formatFixed(
                    inputValue + currentBufferValue
                );
            } else if (!isNaN(parseInt(input, 10))) {
                if (isFirstInput) {
                    this.state.buffer = '' + input;
                } else if (this.state.buffer.length > 12) {
                    Gui.playSound('bell');
                } else {
                    this.state.buffer += input;
                }
            }
            if (this.state.buffer === '-') {
                this.state.buffer = '';
            }
            // once an input is accepted and updated the buffer,
            // the buffer should not be in reset state anymore.
            this.isReset = false;

            this.trigger('buffer-update', this.state.buffer);
    };
    
    NumberBuffer._onInput = _onInput
    NumberBuffer._handleInput = _handleInput
    NumberBuffer._updateBuffer = _updateBuffer
      
    return new NumberBuffer
  
});
