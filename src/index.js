import Cylon from 'cylon'
import linearmodel from './model'
import cost from './costfunction'
import data from './data.json'
// Cylon.robot({
//   connections: {
//     arduino: { adaptor: 'firmata', port: '/dev/ttyACM0' }
//   },
//
//   devices: {
//     led: { driver: 'led', pin: 13 }
//   },
//
//   work: function(my) {
//     every((1).second(), my.led.toggle);
//   }
// }).start();
