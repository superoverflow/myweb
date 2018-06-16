//ref: https://codereview.stackexchange.com/questions/121802/a-reusable-ajax-polling-function

function Request() {
  this.pollTimer = null;
  this.interval = 1000;
  this.url = './request.php';
  this.func = response => console.log(response)
}

Request.prototype.disablePoll = function () {
  clearInterval(this.pollTimer);
  this.pollTimer = null;
};

Request.prototype.activatePoll = function () {
  this.pollTimer = setInterval(() => {
    $.getJSON(this.url).then(this.func)
  }, this.interval);
};