//ref: https://codereview.stackexchange.com/questions/121802/a-reusable-ajax-polling-function

function Poll() {
  this.pollTimer = null;
  this.interval = 1000;
  this.url = './request.php';
  this.func = response => console.log(response)
}

Poll.prototype.disablePoll = function () {
  clearInterval(this.pollTimer);
  this.pollTimer = null;
};

Poll.prototype.activatePoll = function () {
  this.pollTimer = setInterval(() => {
    $.getJSON(this.url).then(this.func)
  }, this.interval);
};