#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let m = 0; m < this.height; m++) {
      let k = '';
      for (let n = 0; n < this.width; n++) {
        k += 'X';
      }
      console.log(k);
    }
  }

  rotate () {
    const l = this.width;
    this.width = this.height;
    this.height = l;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
