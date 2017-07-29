'use strict'

let cylon = require('cylon')

cylon.robot({
  'connections': {
    'arduino': { 'adaptor': 'firmata', 'port': '/dev/ttyACM0' }
  },

  'devices': {
    'led': { 'driver': 'led', 'pin': 12}
  },

  work: (my) => {
    every((1).second(), () => {
      my.led.turnOn((err, val) => {
          if(err){
            console.log(err)
          }else{
            console.log(val)
          }
      })
      // console.log('1')
    })
  }
}).start()
