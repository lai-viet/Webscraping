var store = require('app-store-scraper');
var os = require("os");
var res;
var fs = require('fs');

store.app({ id: 553834731 })
.then(function(result) {
    res = result; 
    console.log(res);

    var data = JSON.stringify(res, null, 2);
    fs.writeFileSync("output.json", data + os.EOL + os.EOL);
    fs.appendFileSync("output.json", data);
});

