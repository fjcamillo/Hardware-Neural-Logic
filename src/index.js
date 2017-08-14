const Cylon = require('cylon');

const lm = (x, t0, t1) => {
      const output = t0 + t1*x
      return output
  }

const softmax = (model) => {
      const z = 1 + math.e**-model
      const logit = 1/z
      return z
      }




Cylon.robot({
  connections: {
    arduino: { adaptor: 'firmata', port: '/dev/ttyACM0' }
  },

  devices: {
    led: { driver: 'led', pin: 13 }
  },

  work: function(my) {
    every((1).second(), my.led.toggle);
  }
}).start();
