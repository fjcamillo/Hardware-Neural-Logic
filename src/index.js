const Cylon = require('cylon');

const lm = (x, t0, t1) => {
      const output = t0 + t1*x
      return output
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
