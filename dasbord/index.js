const express = require('express');
var app = express();
let status = 1;
let service = 'sds';
app.get('/getStatus', function (req, res) {
  res.send(getFile(status, service));
});

app.post('/status/:status', (req, res) => {
  console.log(req.params);
  status = req.params.status;
  service = req.headers.service;
  res.send('ok');
});

app.listen(9000, function () {
  console.log('Server started on port 9000');
});

function getFile(status, txt) {
  return `<html>
  <head>
    <style>
      div {
        background-color: rgb(230, 14, 14);
        width: 300px;
        padding: 50px;
        margin: 20px;
      }
      .green {
        background-color: rgb(0, 255, 0);
        width: 100px;
        padding: 100px;
        margin: 20px;
      }
      .red {
        background-color: rgba(255, 30, 0, 0.959);
        width: 100px;
        padding: 100px;
        margin: 20px;
      }
    </style>
  </head>
  <body>
    <h2>test ping</h2>
    <!-- <div> -->
    <!-- <green>   -->
    <p id="cube">${txt}</p>
    <script>
      // let color = 'red';
      document.getElementById('cube').className += ' ${status == 1 ? ' green' : ' red'}';
      setTimeout(() => {
        window.location = 'http://52.170.32.128:9000/getStatus';
      }, 1000);
    </script>
  </body>
</html>
`;
}