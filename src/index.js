'use strict'

const cylon = require('cylon')

cylon.robot({
  connections: {
    arduino: { adaptor: 'firmata', port: '/dev/ttyACM0' }
  },

  devices: {
    led: { driver: 'led', pin: 13}
  },

  work: (my) => {
    every((.5).second(), () => {
      my.led.toggle()
      console.log('1')
    })
  }
}).start()
