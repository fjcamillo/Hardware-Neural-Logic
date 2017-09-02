'use strict'

const linearmodel = async (x, t0=0.1, t1, 0.1) => {
  return (t0 + x*t1)
}

const proto = {
  linearmodel,
}

export default function () {
  return Object.assign({}, proto)
}
