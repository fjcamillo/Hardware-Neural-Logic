// import Cylon from 'cylon'
// import SerialPort from 'serialport'
import five from 'johnny-five'
// import linearmodel from './model'
// import cost from './costfunction'
// import data from './data.json'

// const port = new SerialPort('/dev/ttyACM0', {
//   baudRate: 9600
// })


// Cylon.robot({
//   connections: {
//     arduino: { adaptor: 'firmata', port: port }
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

const board  = new five.Board(
  // {
  //     port: '/dev/ttyACM0'
  // }
)

board.on('ready', () => {
  const led = new five.Led(13)
  led.blink(500)
})
