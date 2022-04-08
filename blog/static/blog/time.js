function updateTime(){
  const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  const weekdayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  var date = new Date()
  var hours = date.getHours()
  var minutes = date.getMinutes()
  var seconds = date.getSeconds()
  var d_str = weekdayNames[date.getDay()] + ", " + monthNames[date.getMonth()] + " " + date.getDate() + ", " + date.getFullYear() + ", MST.";

  var old_hours = hours;
  if (hours > 12) {
    hours = hours - 12
  } else if (hours == 0) {
    hours = 12
  }

  if (minutes < 10) {
    minutes = "0" + minutes
  }

  if (seconds < 10) {
    seconds = "0" + seconds
  }

  var t_str = hours + ":" + minutes + ":" + seconds + " ";
  if (old_hours > 11) {
    t_str += "p.m.";
  } else {
    t_str += "a.m.";
  }

  document.getElementById('date').innerHTML = d_str;
  document.getElementById('time').innerHTML = t_str;
}
setInterval(updateTime, 1);