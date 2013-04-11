var express = require('express');
var http = require('http');

// Set up express

var app = express();

// var options = {
//   host: 'https://fed.princeton.edu/',
//   path: 'cas/login?service=http://localhost',
//   method: 'GET'
// };

var options = {
  host: 'http://google.com/',
  method: 'GET'
};

app.get('/validate', function(req, res){

var options = {
  host: 'https://fed.princeton.edu/',//cas/login?service=http://localhost
  port: 80,
  path: '/'
};

http.get(options, function(resp){
  resp.setEncoding('utf8');
  resp.on('data', function(chunk){
    res.send(chunk);
  });
}).on("error", function(e){
  console.log("Got error: " + e.message);
});

});


app.listen(3000);